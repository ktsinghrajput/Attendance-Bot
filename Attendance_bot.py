from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import datetime
import time
import os
import keyboard

opt =Options()
opt.add_argument('start-maximized')

opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 0,
"profile.default_content_setting_values.notifications": 1
})

str = input("Enter the google meet code  : ")

url = "https://meet.google.com/?hs=193&pli=1"
chrome_options = Options()

opt.add_argument('start-maximized')

opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 0,
"profile.default_content_setting_values.notifications": 1
})

driver=webdriver.Chrome(chrome_options=opt, executable_path='C:\\Users\\bhaga\\Desktop\\Python_Work\\chromedriver.exe')
driver.get(url)

x = driver.find_element_by_xpath('//*[@id="drawer"]/div/div[3]/div[1]/div/span[1]/a')
x.click()
time.sleep(5)

user_email = driver.find_element_by_xpath('//*[@id="identifierId"]')
user_email.click()
user_email.send_keys('//email')
next = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
next.click()
time.sleep(5)

pass_word = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
pass_word.click()
pass_word.send_keys('//password')

next = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span')
next.click()
time.sleep(15)

code = driver.find_element_by_xpath('//*[@id="i3"]')
code.click()
code.send_keys(str)

join = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[2]/div[2]/button/span')
join.click()
time.sleep(10)

join_now = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
join_now.click()
time.sleep(5)

caption = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[3]/div/span/button/span[2]')
caption.click()
time.sleep(2)

attendance = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[3]/div/div/div[3]/span/button/i[1]')
attendance.click()
time.sleep(2)

b = driver.find_element_by_xpath('//*[@id="bfTqV"]')
b.click()
time.sleep(1)
b.send_keys('20JE0846 Sambhrant Dora')

ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)

students=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[2]/div/div/div[2]/div/div')))
text = students.text
Total_numStudents = int(text)
print(Total_numStudents)
Caption_tray=WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[7]/div')))
Captions=WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/cwiz/div[1]/div/div[9]/div[3]/div[7]/div/div[2]/div/span/span')))
count = 0

staleElement = True
while staleElement :
    try :  # Exception handling (try and expect)
        Caption_tray = driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[7]/div')
        Captions = driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[7]/div/div[2]/div')
        if (Captions.is_displayed()) :
            Caption_text= Captions.text
            Caption_text = Caption_text.lower()
            print(Caption_text)
    except(StaleElementReferenceException):
        staleElement = True
    except(NoSuchElementException) :
        staleElement = True
    if count ==0 :
        words = ["Sambhrant Dora","Dora","Sambhrant","Sabhrant","20JE0846","846","0846","Attendance","attendance"]
        if any(name in Caption_text for name in words): 
            submit = driver.find_elements_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div[2]/div[2]/div/div[5]/span/button/i')
            submit.click()
            time.sleep(5)
            count+=1
