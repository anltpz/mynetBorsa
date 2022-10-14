
from http.cookiejar import Cookie
from re import S
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth
from selenium.common.exceptions import NoSuchElementException

canli_borsa ="/canliborsa/?plist=finans-canliborsa-button"


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
        # reklam1 =driver.find_element(By.XPATH,'//*[@id="tagon--2bBbyQqLuj"]/div[2]/a')
        # reklam1.click()
    
        wait= WebDriverWait(driver, 10)
        # cookie wait 
        reklam1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"icon--1x4EzqLa5P")))
        # cookie =driver.find_element(By.CLASS_NAME,'icon--1x4EzqLa5P')
        reklam1.click()
    except NoSuchElementException:
        print("reklama tıklamadı tagon")
        try:
            reklam2 =driver.find_element(By.XPATH,'//*[@id="MynetAds_Gravity_CloseButtonImage"]')
            reklam2.click()
        except NoSuchElementException:
            print("reklama tıklamadı MynetAds")
            try:
                reklam3 =driver.find_element(By.CLASS_NAME,'icon--1x4EzqLa5P')
                reklam3.click()
            except NoSuchElementException:
                print("reklama tıklamadı Models")
                try:
                    wait= WebDriverWait(driver, 10)
                    reklam4 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"adm-close-btn-01")))
                    reklam4.click()
                except NoSuchElementException:
                  print("reklama tıklamadı Models")
                    
                
def row():

    try:
        wait =WebDriverWait(driver, 10)
        row_name =wait.until(EC.visibility_of_all_elements_located(((By.XPATH,'//tbody/tr/td[2]/h3/a'))))
    except NoSuchElementException:
        print("row_name yok")
        
    for i in row_name:
        sleep(1)
        href =i.get_attribute("href")
        print(i.text)
        driver.get(href)
        get_data_page()
        sleep(5)
        
        

def get_data_page():
    try:
        wait= WebDriverWait(driver, 10)
        cookie = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'icon--1x4EzqLa5P')))
        cookie.click() 
    except NoSuchElementException:
        print("cookie yok")
        try:
            wait= WebDriverWait(driver, 10)
            cookie = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'adm-close-btn-01')))
            cookie.click() 
        except NoSuchElementException:
            print("cookie yok")
        
    try:
      
        wait =WebDriverWait(driver, 10)
        get_data =wait.until(EC.visibility_of_all_elements_located(((By.XPATH,'//ul/li/span'))))
        for i in get_data:
                sleep(1)
                print(i.text)
    except NoSuchElementException:
        print("get_data yok")
        
      
    

def run():
    
    driver.get("https://finans.mynet.com/borsa"+canli_borsa)
    WebDriverWait(driver, 10)
    reklamEngelleme()
    sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(3)
    row()
    

run()

if __name__ == "__main__":
    run()
    
                


 
    



