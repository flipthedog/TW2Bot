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
import re
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
import TWChoice
from TWBuild import TWBuildO
from TWBuild import CheckWarehouse
from TWChoice import TWChoiceO
from TWFarm import TWFarmO
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
# Constructor starts up the program
#StartUp = TWStartup.StartUp()


class TWBot:
	def __init__(self):
		self.StartUp = TWStartup.StartUp()
		#self.Build = TWBuild.TWBuild()
		self.driver = self.StartUp.getDriver()
		self.URL = self.StartUp.getURL()

# Initialize the bot object
Bot = TWBot()
Build = TWBuildO(Bot.driver,Bot.URL)
Choice = TWChoiceO(Bot.driver,Bot.URL)
Farm = TWFarmO(Bot.driver,Bot.URL)
print("Start-Up Complete!")
print("The current url:" + str(Bot.URL))

#print(TWBuild.QueueEmpty(Bot.driver,Bot.URL))
#TWBuild.startBuild(Bot.driver,Bot.URL, 4)
#print(TWBuild.CheckFarm(Bot.driver,Bot.URL))
#print(TWBuild.CheckWarehouse(Bot.driver,Bot.URL))
print("The current level of the HQ: " + str(TWChoice.BuildingLevel(Bot.driver,Bot.URL,0)))
print("The current level of the timbercamp: " + str(TWChoice.BuildingLevel(Bot.driver,Bot.URL,4)))
#units = TWFarm.getCurrentUnit(Bot.driver,Bot.URL)
#TWFarm.sendTroops(Bot.driver,Bot.URL,units,416,492)

#Farm.addVillage(416,492)
#village = [0] * 2
#village = Farm.getVillage(0)
#TWFarm.sendTroops(Bot.driver,Bot.URL,units,village[0],village[1])

while(True):
	pageLoad(1)
	#to keep the window
#do nothing
