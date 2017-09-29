########################################################################
#TWBot v3.0
#Author: Floris van Rossum
#Purpose: Bot for Tribal Wars 2

########################################################################
#IMPORT STATEMENTS

#System Imports
import sys, os
import time
import math
import pywinauto
import win32api, win32con

#Selenium Imporots
import selenium
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.alert import Alert #Not needed?


#HomeMade Imports

########################################################################
#INFO 

#Upgrade Chart:
# 0. Headquarters
# 1. Church
# 2. Rally point
# 3. statue
# 4. Timber camp
# 5. Clay camp
# 6. Iron Mine
# 7. farm
# 8. Warehouse
# 9. Hiding Place
# 10. Barracks
# 11. Stable
# 12. Workshop
# 13. Academy
# 14. Smithy
# 15. Market
# 16. Wall

########################################################################
#FUNCTIONS

#Click function clicks on screen at x,y
#Necessary in order to get past notifications

def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
#Start-Up Function
#Creates selenium driver, initializes window to village headquarters screen
def StartUp():
	driver = webdriver.Chrome()
	chrome_options = webdriver.ChromeOptions() #Not needed?

	driver.get("https://www.tribalwars.us/")
	elemUserName = driver.find_element_by_id("user")
	elemPassword = driver.find_element_by_id("password")
	elemLogIn = driver.find_element_by_class_name("btn-login")

	elemUserName.send_keys("bepthedog")
	elemPassword.send_keys("flip1997")
	elemLogIn.click()

	#Enable if chrome says "Do you want to save your password?"
	#time.sleep(1)
	#click(200,200)

	#Clicking on the correct world
	elemWorld = driver.find_element_by_class_name("world_button_active")
	elemWorld.click()
########################################################################
#Main Program
StartUp()
print("Start-Up Complete!")
while(True):
	print("hello")
	#to keep the window
#do nothing