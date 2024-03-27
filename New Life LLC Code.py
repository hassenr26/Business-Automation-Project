import webbrowser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# login for dashboard
username = 'user1@newlifecare.com '
password = '******'

# sets location of Chrome Driver
s = Service('usr/local/bin/chromedriver')

# sets some selenium chrome options
chromeOptions = Options()
driver = webdriver.Chrome(service=s,options=chromeOptions)

# opens browser to MCCP Dashboard
driver.get('https://mnopenings.org/login/')

'''
logs into account using email and password and clicks login 
'''
# finds username input and fills with email 
uname = driver.find_element("name","username")
uname.send_keys(username)

# finds password input and fills with password
pword = driver.find_element("name","password")
pword.send_keys(password)

# clicks login
click_login = driver.find_element(by=By.CLASS_NAME, value="btn.btn-block")
click_login.click()

# goes to update page of first house 
driver.get("https://mnopenings.org/dashboard/provider/edit-listing/?profile=5244")
    
i = True
while i:
    
    # goes to update page of first house
    driver.get("https://mnopenings.org/dashboard/provider/edit-listing/?profile=5244")

    # updates first house
    click_update2 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[1]/div/form/div[7]/input')
    click_update2.click()


    # goes to update page of second house
    driver.get("https://mnopenings.org/dashboard/provider/edit-listing/?profile=5243")

    # updates second house
    click_update4 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div[1]/div/form/div[7]/input")
    click_update4.click()

