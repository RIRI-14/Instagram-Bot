# -*- coding: utf-8 -*-
"""
Created on Sat July  3 14:37:58 2021

@author: RIDDHI BARODIA
"""
#Import selenium and webdriver
from selenium import webdriver
import time

#Add the address to your own C Drive where you should paste the chromedriver from the downloads
browser = webdriver.Chrome("C:\chromedrivers\chromedriver.exe")
browser.get('https://instagram.com/')
time.sleep(4)
#Add the full xpath address to the respective icons 
Username=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")

#Add the Instagram ID you want to use in place of XXX
Username.send_keys("XXX")
time.sleep(4)

password=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
#Add the Instagram Password to your ID in place of XXX
password.send_keys("XXX")
password.submit()
time.sleep(5)

#To proceed from the pop-up related to enabling instagram notifications
Notnow=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
Notnow.click()
time.sleep(3)
Noti=browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
Noti.click()
time.sleep(7)

#Function to select the first picture/video that is shown on your feed
def firstpic():
                    
	time.sleep(5)
	pic = browser.find_element_by_class_name("fXIG0") 
	pic.click()

#Function to like the first picture/video that is shown on your feed    
def likepic(): 
	time.sleep(7) 
	like = browser.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[3]/div/article[1]/div/div[3]/div/div/section[1]/span[1]/button")
	like.click()

#Function to save the first picture/video that is shown on your feed
def savepost():
    time.sleep(7)
    save = browser.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[3]/div/article[1]/div/div[3]/div/div/section[1]/span[4]/div/div/button")
    save.click()

#Function calls
firstpic()
likepic()
savepost()
