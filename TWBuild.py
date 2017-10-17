########################################################################
#Author: Floris van Rossum
#Purpose: Provide all the necessary functions for building buildings
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
# TWBuild object
# Will always know what to build next if it needs to
# implement some kind of priority algorithm
class TWBuildO:
	def updateResources(self,driver, url):
		resources = [0] * 3
		resources = updateCurrentResources(driver,url)
		self.wood = resources[0]
		self.clay = resources[1]
		self.iron = resources[2]

	def BuildNext():
		if (not(CheckFarm(self.driver,self.url))):
			print("Not enough farm space, so upgrade the farm")
			startBuild(self.driver,self.url,7)
		elif (not(CheckWarehouse(self.driver,self.driver))):
			print("Not enough warehouse space, upgrade the warehouse")
			startBuild(self.driver,self.url,8)
		else:
			building = TWChoice.nextBuild(self.driver,self.url)
			if (CanBuild(self.driver,self.url, building)):
				startBuild(self.driver, self.url, building)
			else: print("there are not enough resources to build the building")
			# this will determine if it can build the next build project

	def __init__(self, driver, url):
		self.url = url
		self.driver = driver
		self.updateResources(self.driver,self.url)
		# self.TWChoice = TWChoice(driver,url)
		# the next build project

########################################################################
# For going into a certain building
def goToBuilding(driver,url,building):
	if(building == 100):
		#Main screen
		driver.get(url + "overview")
	if(building == 0):
	    #Headquarters screen
		driver.get(url + "main")
	if(building == 1):
	    #Church Screen
		driver.get(url + "church_f")
	if(building == 2):
	    #Rallypoint screen
		driver.get(url + "place")
	if(building == 3):
	    #statue Screen
		driver.get(url + "statue")
	if(building == 4):
	    #TimberCamp screen
		driver.get(url + "wood")
	if(building == 5):
	    #Clay camp Screen
		driver.get(url + "stone")
	if(building == 6):
		#Iron mine screen
		driver.get(url + "iron")
	if(building == 7):
	    #Farm Screen
		driver.get(url + "farm")
	if(building == 8):
	    #Warehouse screen
		driver.get(url + "storage")
	if(building == 9):
	    #Hiding Place Screen
		driver.get(url + "hide")
########################################################################

def startBuild(driver, url, building):
	if(building == 0):
		#Upgrade HQ
		print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " : Building Headquarters")
		buildBuiding(driver, url, "'main'",building)
	if(building == 1):
		#Upgrade church
		print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " : Building church")
		buildBuiding(driver, url, "'church_f'",building)
	if(building == 2):
		#Upgrade rally point
		print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " : Building rallypoint")
		buildBuiding(driver, url, "'place'",building)
	if(building == 3):
		#Upgrade the statue
		print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " : Building statue")
		buildBuiding(driver, url, "'statue'",building)
	if(building == 4):
		#Upgrade the Timber camp
		print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " : Building woodcamp")
		buildBuiding(driver, url, "'wood'",building)
	if(building == 5):
		#Upgrade the clay camp
		print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " : Building claycamp")
		buildBuiding(driver, url, "'stone'",building)
	if(building == 6):
		#Upgrade the iron camp
		print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " : Building ironcamp")
		buildBuiding(driver, url, "'iron'",building)
	if(building == 7):
		#Upgrade the farm
		print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " : Building farm")
		buildBuiding(driver, url, "'farm'",building)
	if(building == 8):
		#Upgrade the warehouse
		print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " : Building warehouse")
		buildBuiding(driver, url, "'storage'",building)
	if(building == 9):
		#Upgrade the hideout
		print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " : Building hideout")
		buildBuiding(driver, url, "'hide'",building)
	### add the rest later #######

def buildBuiding(driver, url, buildName, build):
	goToBuilding(driver, url, 0)
	string = "//a[@data-building = " + buildName + "]"
	buildElt = driver.find_elements_by_xpath(string)
	time.sleep(2)
	buildElt[1].click()
	time.sleep(2)
	goToBuilding(driver, url, 100)


########################################################################
# Figure out if the build queue is empty
def QueueEmpty(driver,url):
	try:
		goToBuilding(driver, url, 0) # go to the headquarters
		queueElt = driver.find_elements_by_xpath("//a[@class = 'btn btn-cancel']")
	except NoSuchElementException:
		print("Exception called")
		return True
		pass
	goToBuilding(driver,url,100)
	return 0>=len(queueElt)

########################################################################
# Check if there are enough resources to build a building
def CanBuild(driver, url, building):
	resources = updateCurrentResources(driver,url)
	goToBuilding(driver,url,0) # go to the headquarters
	time.sleep(1)
	if (building == 0):
		# Check headquarters upgrade cost
		reqResources = [0] * 3
		reqResources = getBuildingResources(driver,url,"main_buildrow_main")
		for x in range(0,3):
			if(reqResources[x] > resources[x]):
				return False
		return True
	if (building == 1):
		# Check Church Upgrade cost
		reqResources = [0] * 3
		reqResources = getBuildingResources(driver,url,"main_buildrow_main")
		for x in range(0,3):
			if(reqResources[x] > resources[x]):
				return False
		return True
	if (building == 2):
		# Check Rally Point upgrade cost
		reqResources = [0] * 3
		reqResources = getBuildingResources(driver,url,"main_buildrow_place")
		for x in range(0,3):
			if(reqResources[x] > resources[x]):
				return False
		return True
	if (building == 3):
		# Check Statue upgrade cost
		reqResources = [0] * 3
		reqResources = getBuildingResources(driver,url,"main_buildrow_statue")
		for x in range(0,3):
			if(reqResources[x] > resources[x]):
				return False
		return True
	if (building == 4):
		# Check Timber camp upgrade cost
		reqResources = [0] * 3
		reqResources = getBuildingResources(driver,url,"main_buildrow_wood")
		for x in range(0,3):
			if(reqResources[x] > resources[x]):
				return False
		return True
	if (building == 5):
		# Check clay camp upgrade cost
		reqResources = [0] * 3
		reqResources = getBuildingResources(driver,url,"main_buildrow_stone")
		for x in range(0,3):
			if(reqResources[x] > resources[x]):
				return False
		return True
	if (building == 6):
		# Check iron camp upgrade cost
		reqResources = [0] * 3
		reqResources = getBuildingResources(driver,url,"main_buildrow_iron")
		for x in range(0,3):
			if(reqResources[x] > resources[x]):
				return False
		return True
	if (building == 7):
		# Check Farm upgade cost
		reqResources = [0] * 3
		reqResources = getBuildingResources(driver,url,"main_buildrow_farm")
		for x in range(0,3):
			if(reqResources[x] > resources[x]):
				return False
		return True
	if (building == 8):
		# Check warehouse upgrade cost
		reqResources = [0] * 3
		reqResources = getBuildingResources(driver,url,"main_buildrow_storage")
		for x in range(0,3):
			if(reqResources[x] > resources[x]):
				return False
		return True
	if (building == 9):
		# Check hiding place upgrade cost
		reqResources = [0] * 3
		reqResources = getBuildingResources(driver,url,"main_buildrow_hide")
		for x in range(0,3):
			if(reqResources[x] > resources[x]):
				return False
		return True
	if (building == 10):
		# Check barracks upgrade cost
		reqResources = [0] * 3
		reqResources = getBuildingResources(driver,url,"main_buildrow_barracks")
		for x in range(0,3):
			if(reqResources[x] > resources[x]):
				return False
		return True
	if (building == 11):
		# Check stable upgrade cost
		reqResources = [0] * 3
		reqResources = getBuildingResources(driver,url,"main_buildrow_main")
		for x in range(0,3):
			if(reqResources[x] > resources[x]):
				return False
		return True
	if (building == 12):
		# Check workshop upgrade cost
		reqResources = [0] * 3
		reqResources = getBuildingResources(driver,url,"main_buildrow_main")
		for x in range(0,3):
			if(reqResources[x] > resources[x]):
				return False
		return True
	if (building == 13):
		# Check Academy upgrade cost
		reqResources = [0] * 3
		reqResources = getBuildingResources(driver,url,"main_buildrow_main")
		for x in range(0,3):
			if(reqResources[x] > resources[x]):
				return False
		return True
	if (building == 14):
		# Check smithy upgrade cost
		reqResources = [0] * 3
		reqResources = getBuildingResources(driver,url,"main_buildrow_main")
		for x in range(0,3):
			if(reqResources[x] > resources[x]):
				return False
		return True
	if (building == 15):
		# Check market upgrade cost
		reqResources = [0] * 3
		reqResources = getBuildingResources(driver,url,"main_buildrow_market")
		for x in range(0,3):
			if(reqResources[x] > resources[x]):
				return False
		return True
	if (building == 16):
		# Check wall upgrade cost
		reqResources = [0] * 3
		reqResources = getBuildingResources(driver,url,"main_buildrow_wall")
		for x in range(0,3):
			if(reqResources[x] > resources[x]):
				return False
		return True

	goToBuilding(driver,url,100) # Return to the main overview screen

# Helper method for the method above
# Gets the resources of a building upgrade
def getBuildingResources(driver, url, buildingstr):
	elemRow = driver.find_element_by_id(buildingstr)
	reqResources = [0] * 3
	reqResources[0] = int(elemRow.find_element_by_class_name("cost_wood").text)
	reqResources[1] = int(elemRow.find_element_by_class_name("cost_stone").text)
	reqResources[2] = int(elemRow.find_element_by_class_name("cost_iron").text)
	return(reqResources) # Return an array of the resources required for the building
########################################################################
# Check if there is enough farm space, true = enough space, false = not enough
def CheckFarm(driver, url):
	goToBuilding(driver,url,100) # ensure we are in overview
	maxPop = int(driver.find_element_by_id("pop_max_label").text)
	print("This is the maxpop:" + str(maxPop))
	usedPop = int(driver.find_element_by_id("pop_current_label").text)
	print("This is the usedPop: " + str(usedPop))
	percent = float((usedPop / maxPop))
	return percent < 0.9

########################################################################
# Return the current resources available
def updateCurrentResources(driver,url):
	rescArray = [0] * 3
	goToBuilding(driver,url,100)
	woodEl = int(driver.find_element_by_id("wood").text)
	clayEl = int(driver.find_element_by_id("stone").text)
	ironEl = int(driver.find_element_by_id("iron").text)
	rescArray[0] = woodEl
	rescArray[1] = clayEl
	rescArray[2] = ironEl
	return rescArray

########################################################################
# Return a building level of a specific building
def BuildingLevel(driver,url, building):
	goToBuilding(driver,url,0) # Go to the headquarters
	levelElt = driver.find_elements_by_xpath("//span[@style='font-size: 0.9em']")
	if(building == 0):
	    return re.findall('\d+', levelElt[0].text)
	if(building== 1):
	    return re.findall('\d+', levelElt[1].text)
	if(building== 2):
	    return re.findall('\d+', levelElt[2].text)
	if(building== 3):
	    return re.findall('\d+', levelElt[3].text)
	if(building== 4):
	    return re.findall('\d+', levelElt[4].text)
	if(building == 5):
	    return re.findall('\d+', levelElt[5].text)
	if(building == 6):
	    return re.findall('\d+', levelElt[6].text)
	if(building == 7):
	    return re.findall('\d+', levelElt[7].text)
	if(building == 8):
	    return re.findall('\d+', levelElt[8].text)
	if(building == 9):
	    return re.findall('\d+', levelElt[9].text)
	if(building == 10):
	    return re.findall('\d+', levelElt[10].text)
	if(building == 11):
	    return re.findall('\d+', levelElt[11].text)
	if(building == 12):
	    return re.findall('\d+', levelElt[12].text)
	if(building == 13):
	    return re.findall('\d+', levelElt[13].text)
	if(building == 14):
	    return re.findall('\d+', levelElt[14].text)
	if(building == 15):
	    return re.findall('\d+', levelElt[15].text)
	if(building == 16):
	    return re.findall('\d+', levelElt[16].text)
	goToBuilding(driver, url, 100)

########################################################################
# Return if there is enough space in the warehouse
# True = Enough space
# False = not enough space
def CheckWarehouse(driver,url):
	warehouseElem = driver.find_element_by_id("storage").text
	print(warehouseElem)
	resources = updateCurrentResources(driver, url)
	print(resources)
	for x in range(0,3):
		calcVal = float(int(resources[x])/int(warehouseElem))
		print(str(calcVal))
		if((calcVal) > 0.7):
			return False
	return True
