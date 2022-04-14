from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os, sys
from time import sleep
from random import randint
import pickle


def login(login_driver,login_link,login_username, login_password):
    login_driver.get(login_link)
    sleep(randint(1,3))
    login_driver.find_element(by=By.XPATH, value="//input[@placeholder='Nomor Telepon Anda']").send_keys(login_username)
    login_driver.find_element(by=By.XPATH, value="//input[@placeholder='Kata Sandi Anda']").send_keys(login_password)
    login_driver.find_element(by=By.XPATH, value='//*[@id="__layout"]/div/div[2]/button').click()
    sleep(4)

if __name__ == '__main__':
    username = '6281223334444'
    password = 'password'
    link_popular = 'https://evermos.com/browse?orderBy=1&navSource=homepage_product_list_terbaru'
    login_link = 'https://evermos.com/login'
    driver = webdriver.Edge()
    login(driver,login_link,username,password)
    driver.get(link_popular)
