
from http.cookiejar import Cookie
from operator import le
from re import S
from secrets import choice
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth
from selenium.common.exceptions import NoSuchElementException
import requests
from bs4 import BeautifulSoup
import re
import json

canli_borsa ="/canliborsa/?plist=finans-canliborsa-button"
baseUrl="https://finans.mynet.com/"

# chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option('useAutomationExtension', False)

hrefList =[]
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

def reklamEngelleme():
    try:
        reklam2 =driver.find_element(By.CSS_SELECTOR,"#tagon--2bBbyQqLuj > div.content--1Pp0zxWHoo > a > span")
        reklam2.click()
        
    except NoSuchElementException:
        print("reklama tıklamadı tagon")
        try:
            reklam2 =driver.find_element(By.XPATH,'//*[@id="MynetAds_Gravity_CloseButtonImage"]')
            reklam2.click()
        except NoSuchElementException:
            print("reklama tıklamadı MynetAds")
            try:
                
                reklam3 =driver.find_element(By.CLASS_NAME,"close_button--1pDkCqh17C fadeIn--OT-fkX5hvK")
                reklam3.click()
            except NoSuchElementException:
                print("reklama tıklamadı adm-close-btn-01") 
                             
def row():
    try:
        print("row")
        row_name =driver.find_elements(By.XPATH,'//tbody/tr/td[2]/h3/a')
        for i in row_name:
            sleep(0.1)
            href =i.get_attribute("href")
            print(href)
            hrefList.append(href)
            
        print(hrefList.count)  
    except NoSuchElementException:
        print("row_name yok")
   
def cookie_data():
     
        try:
            cookie =driver.find_element(By.CLASS_NAME,'adm-close-btn-01')
            cookie.click()
        except NoSuchElementException:
            print("cookie yok")  
        
def get_data_page():
    print("get_data_page")
    cookie_data()
    
    i=0
    while True:
        page = requests.get(hrefList[i-1])
        sleep(5)
        soup = BeautifulSoup(page.content, 'html.parser')
        count =hrefList.count
        for ultag in soup.find_all('li', {"class":"flex align-items-center justify-content-between"}):
            sleep(0.2)
            for litag in ultag.find_all('span'):
             print(litag.text)
             i+=1
   
        
   


def run():
    print("run")
    driver.get("https://finans.mynet.com/borsa"+canli_borsa)
    WebDriverWait(driver, 10)
    reklamEngelleme()
    sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(3)
    row()
    get_data_page()
    



if __name__ == "__main__":
    run()
    
                


 
    



