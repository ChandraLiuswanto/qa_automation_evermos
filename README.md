### qa_automation_evermos
Automation QA case for first time buyer on berikhtiar.com to buy an item. berikhtiar.com is personal reseller store to accomodate user to buy an item directly to evermos.com.

The project use Selenium 4 webdriver on **Edge** webdriver using **Python** languague. There are still known bug for example the scraping price data sometimes is the price without discount, for a proof of concept, the sleep is added to wait the page is fully loaded. For each loop, the program takes estimated 45 to 60 second. The time can be reduce by reducing the sleep and add function to wait the page is fully loaded

The expected result is the total value that customer price on third party website is match to the expected price 


### Project requiremment
The project use multiple open source library: Python:3.8.10, Selenium, pandas

### How to use this script?
1. First download python with version 3.8.10
2. Install the required library `pip install Selenium pandas`
3. Download this repo by download as zip or using `git clone https://github.com/ChandraLiuswanto/qa_automation_evermos.git` on git cli
4. Extract the folder and navigate to the extracted folder
5. Using cmd or terminal on the extracted folder run  `python main.py `
6. The output is generated on  `output.csv `

### Data demo
There are two demo data, output.csv that create table state of the automation and a video that showing the demo
