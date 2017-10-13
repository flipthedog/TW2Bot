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
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

#HomeMade Imports
import TWBuild
import TWFarm
import TWStartup
#import TWFind

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

#Waiting for page to load
def pageLoad(times):
	time.sleep(times)

########################################################################
#Main Program

# The start-up object
StartUp = TWStartup.StartUp()
StartUp.StartUpWindow()

print("Start-Up Complete!")
print("The current url:" + StartUp.getURL())

while(True):
	pageLoad(1)
	#to keep the window
#do nothing
