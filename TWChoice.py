########################################################################
#Author: Floris van Rossum
#Purpose: Provide the next building to build
########################################################################
#Import statments
import selenium
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.alert import Alert #Not needed?
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime

import time
import re

import TWBuild
########################################################################
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

class TWChoiceO:
	def __init__(self,driver,url):
		self.driver = driver
		self.url = url
		self.level = getAllLevels(driver,url)
	def nextBuild():
		self.nexti = nextBuilding(self.driver,self.url)
		return nexti

def nextBuilding(driver,url):
	print("this is the level of the woodcutting camp: " + BuildingLevel(driver,url,4))

def getAllLevels(driver,url):
	TWBuild.goToBuilding(driver, url, 0) # return to the overview screen
	levels = [0] * 16
	for x in range(0,15):
		levels[x] = BuildingLevel(driver,url,x)
	TWBuild.goToBuilding(driver, url, 100) # return to the overview screen
	print(levels)
	return levels
########################################################################
# Return a building level of a specific building
def BuildingLevel(driver,url, building):
	if(building == 0):
		elemRow = driver.find_element_by_id("main_buildrow_main")
		levelElt = elemRow.find_element_by_xpath("//span[@style='font-size: 0.9em']")
		return int(levelElt.text[6])
	if(building == 1):
		elemRow = driver.find_element_by_id("main_buildrow_main")
		levelElt = elemRow.find_element_by_xpath("//span[@style='font-size: 0.9em']")
		return int(levelElt.text[6])
	if(building == 2):
		elemRow = driver.find_element_by_id("main_buildrow_place")
		levelElt = elemRow.find_element_by_xpath("//span[@style='font-size: 0.9em']")
		return int(levelElt.text[6])
	if(building == 3):
		elemRow = driver.find_element_by_id("main_buildrow_statue")
		levelElt = elemRow.find_element_by_xpath("//span[@style='font-size: 0.9em']")
		return int(levelElt.text[6])
	if(building== 4):
		elemRow = driver.find_element_by_id("main_buildrow_wood")
		levelElt = elemRow.find_element_by_xpath("//span[@style='font-size: 0.9em']")
		return int(levelElt.text[6])
	if(building == 5):
		elemRow = driver.find_element_by_id("main_buildrow_stone")
		levelElt = elemRow.find_element_by_xpath("//span[@style='font-size: 0.9em']")
		return int(levelElt.text[6])
	if(building == 6):
		elemRow = driver.find_element_by_id("main_buildrow_iron")
		levelElt = elemRow.find_element_by_xpath("//span[@style='font-size: 0.9em']")
		return int(levelElt.text[6])
	if(building == 7):
		elemRow = driver.find_element_by_id("main_buildrow_farm")
		levelElt = elemRow.find_element_by_xpath("//span[@style='font-size: 0.9em']")
		return int(levelElt.text[6])
	if(building == 8):
		elemRow = driver.find_element_by_id("main_buildrow_storage")
		levelElt = elemRow.find_element_by_xpath("//span[@style='font-size: 0.9em']")
		return int(levelElt.text[6])
	if(building == 9):
		elemRow = driver.find_element_by_id("main_buildrow_hide")
		levelElt = elemRow.find_element_by_xpath("//span[@style='font-size: 0.9em']")
		return int(levelElt.text[6])
	if(building == 10):
		elemRow = driver.find_element_by_id("main_buildrow_barracks")
		levelElt = elemRow.find_element_by_xpath("//span[@style='font-size: 0.9em']")
		return int(levelElt.text[6])
	if(building == 11):
		elemRow = driver.find_element_by_id("main_buildrow_main")
		levelElt = elemRow.find_element_by_xpath("//span[@style='font-size: 0.9em']")
		return int(levelElt.text[6])
	if(building == 12):
		elemRow = driver.find_element_by_id("main_buildrow_main")
		levelElt = elemRow.find_element_by_xpath("//span[@style='font-size: 0.9em']")
		return int(levelElt.text[6])
	if(building == 13):
		elemRow = driver.find_element_by_id("main_buildrow_main")
		levelElt = elemRow.find_element_by_xpath("//span[@style='font-size: 0.9em']")
		return int(levelElt.text[6])
	if(building == 14):
		elemRow = driver.find_element_by_id("main_buildrow_main")
		levelElt = elemRow.find_element_by_xpath("//span[@style='font-size: 0.9em']")
		return int(levelElt.text[6])
	if(building == 15):
		elemRow = driver.find_element_by_id("main_buildrow_market")
		levelElt = elemRow.find_element_by_xpath("//span[@style='font-size: 0.9em']")
		return int(levelElt.text[6])
	if(building == 16):
		elemRow = driver.find_element_by_id("main_buildrow_wall")
		levelElt = elemRow.find_element_by_xpath("//span[@style='font-size: 0.9em']")
		return int(levelElt.text[6])
