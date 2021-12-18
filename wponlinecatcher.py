from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
import winsound

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
input("Read the qr then open the chat you want to track and press enter")

onlineStatus = 1
currentTimeAsSeconds = 0
hasLoggedIn = False
beepOnce = True
while True:
    try:
        
        #if online
        onlineStatus = driver.find_element(By.XPATH,"//*[@id='main']/header/div[2]/div[2]/span")
        if onlineStatus.get_attribute('innerHTML') == "online" :
            hasLoggedIn = True
            currentTimeAsSeconds+=2
            if beepOnce:
                frequency = 2500  # Set Frequency To 2500 Hertz
                duration = 1000  # Set Duration To 1000 ms == 1 second
                winsound.Beep(frequency, duration)
                beepOnce = False
        else:
            raise ValueError("")
    except Exception as e:
        if hasLoggedIn:
            print(str(datetime.datetime.now())+" "+str(currentTimeAsSeconds)+" saniye kadar kaldı")
            
            hasLoggedIn = False
        currentTimeAsSeconds=0
        beepOnce = True
        #if not online
        
    time.sleep(2)
