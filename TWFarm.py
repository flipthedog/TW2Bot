########################################################################
#Author: Floris van Rossum
#Purpose: Provide all the necessary functions for sending a specified number of
#		  troops out to farm
########################################################################
import selenium
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.alert import Alert #Not needed?
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime

import TWBuild
########################################################################
#UNITS
# 1. Spear
# 2. Swordmen
# 3. Axe
# 4. Archer
# 5. Scout
# 6. Light Cavalry
# 7. Mounted Archer
# 8. Heavy Cavalry
# 9. Ram
# 10. Catapult
# 11. Noble
# 12. Paladin
########################################################################
# The farming object holds the currently availble units
def TWFarmO(self,driver,url):
	self.driver = driver
	self.url = url
	self.units = getCurrentUnit(self.driver,self.url)
########################################################################
# This gets the number of units currently in the village
# returns the units as an array
def getCurrentUnit(driver,url):
	TWBuild.goToBuilding(driver,url,2)
	unitEl = driver.find_elements_by_class_name("units-entry-all")
	units = [0] * 12
	for x in range(0,11):
		string = unitEl[x].text
		length = len(string)
		units[x] = int(string[1:length - 1])
	TWBuild.goToBuilding(driver,url,100)
	return units
########################################################################
# Send the troops to the village, units is an array to send to a village of
# coordsX and coordsY position
def sendTroops(driver,url,units,coordsX,coordsY):
	TWBuild.goToBuilding(driver,url,2)
	unitsEnter = driver.find_elements_by_class_name("unitsInput")
	for x in range(0,11):
		unitsEnter[x].send_keys(units[x])
	coordinateEl = driver.find_element_by_xpath("//input[@placeholder = '123|456']")
	string = str(str(coordsX) + "|" + str(coordsY))
	coordinateEl.send_keys(string)
	attackButton = driver.find_element_by_id("target_attack")
	attackButton.click()
	attackButton2 = driver.find_element_by_id("troop_confirm_go")
	attackButton2.click()
	TWBuild.goToBuilding(driver,url,100)
