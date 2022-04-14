from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementClickInterceptedException
import sys
from time import sleep
from time import time
from random import randint
import pandas as pd

def wait_element(val,timeout=20):
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, val)))
    
def run_click(val):
    wait_element(val)
    driver.find_element(by=By.XPATH, value=val).click()
    sleep(1)

def input_text(val,text):
    wait_element(val)
    driver.find_element(by=By.XPATH, value=val).send_keys(text)
    sleep(0.5)
            
def spam_end(val):
    for _ in range(val):
        driver.find_element(by=By.TAG_NAME, value='html').send_keys(Keys.END)
        sleep(0.5)

def read_val(val):
    sleep(0.5)
    return driver.find_element(by=By.XPATH, value=val).text
    
if __name__ == '__main__':
    data_x = []
    home_page = 'https://berikhtiar.com/huhuhuh.ce6'

    for i in range(1,9):
        t0 = time()
        driver = webdriver.Edge()
        driver.get(home_page)
        driver.implicitly_wait(30)
        while True:
            try:
                run_click(f'//*[@id="__layout"]/div/div[5]/div[{i}]/div/a') #click object
                break
            except ElementClickInterceptedException:
                spam_end(1)
        ## On object page
        price_val = '//*[@id="__layout"]/div/div[4]/div[6]/div/div[1]/div[2]/div/div[2]'
        driver.implicitly_wait(5)
        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, price_val)))
        except:
            price_val = '//*[@id="__layout"]/div/div[4]/div[6]/div/div[1]/div[2]/div/div'
        driver.implicitly_wait(30)
        price = int(read_val(price_val).replace('.','').replace('Rp',''))
        stock = int(read_val('//*[@id="__layout"]/div/div[4]/div[6]/div/div[2]/div[2]'))
        link = driver.current_url
        run_click('//*[@id="__layout"]/div/div[6]/div/button') # click to buy
        run_click('//*[@id="__layout"]/div/div[7]/div/div[3]/button[1]') # click to cart

        # To cart page
        addr = ['TESTING','Ibu ABC DEF ','08765765765','Jalanan rumah orang nomor 123 RT 99 LV 999']
        stock_selected = abs(int(stock*0.5+1))
        if stock_selected > 10:
            stock_selected = 10
        wait_element('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div/div/div[1]/select')
        Select(driver.find_element(by=By.XPATH, value='//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div/div/div[1]/select')).select_by_index(stock_selected-1)
        sleep(2)
        # Di address page
        run_click('//*[@id="__layout"]/div/div[2]/button[1]') # click alamat
        sleep(1)
        driver.find_element(by=By.XPATH, value='//*[@id="__layout"]/div/div[3]/div/div/div[2]/form/div/label/a').click()
        input_text('//*[@id="__layout"]/div/div[3]/div/div/div[2]/form/div/div/div/div[2]/form/input','jak')
        random_number = randint(1,5)
        run_click(f'//*[@id="__layout"]/div/div[3]/div/div/div[2]/form/div/div/div/div[2]/div/a[{random_number}]/span')
        for j in range(1,5):
            input_text(f'//*[@id="__layout"]/div/div[3]/div/div/div[2]/form/label[{j}]/span[2]/input',addr[j-1]) 

        run_click('//*[@id="__layout"]/div/div[3]/div/div/div[3]/div/button')
        alert_obj = driver.switch_to.alert
        alert_obj.accept()
        wait_element('//*[@id="__layout"]/div/div[2]/button')
        ongkir_price = int((read_val('//*[@id="__layout"]/div/div[2]/div[3]/div[5]/div').replace('.','')).replace('Rp',''))
        spam_end(1)
        run_click('//*[@id="__layout"]/div/div[2]/button')
        run_click('//*[@id="__layout"]/div/div[6]/div/div[3]/button[1]')
        final_price = int((read_val('//*[@id="application"]/div[4]/div/div/div/div[1]/div[1]/div[2]/span[2]').replace(',','')).replace('Rp',''))
        val_correct =final_price==stock_selected*price+ongkir_price
        data_x.append([int(time()-t0),link,stock,price,stock_selected,ongkir_price,final_price,val_correct])
        driver.close()
    df = pd.DataFrame(data_x)
    df.columns=('ts','link','Stock Max', 'Price', 'Stock Selected',
                'Delivery Price','Total Price', 'Data Correct')
    print(df)