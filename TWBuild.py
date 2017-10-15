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
class TWBuild:
	def __init__(self, driver, url):
		self.nextBuildProject #Put some function here later that determines
		self.url = url
		self.driver = driver
		# the next build project

	def BuildNext(building):
		if (canBuild(self.driver, self.url, building)):
			startBuild(self.driver, self.url, building)
		# this will determine if it can build the next build project

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
		goToBuilding(driver, url, 100) # Return to the home screen
		return True
		pass
	print("No exception")
	return 0>=len(queueElt)

########################################################################
# Figure out if requirements to build a building are met, return true
def CanBuild(driver, url, building):
	# check resources, state of the build queue
	return CheckFarm(driver,url) and QueueEmpty(driver, url)
########################################################################
# Check if there is enough farm space
def CheckFarm(driver, url):
	goToBuilding(0) # ensure we are in overview
	maxPop = int(driver.find_element_by_id("pop_max_label").text)
	usedPop = int(driver.find_element_by_id("pop_current_label").text)
	percent = float((usedPop / maxPop))
	return percent < 0.9

def updateCurrentResources(driver,url):
	goToBuilding(driver,url,100)
	woodEl = driver.find_element_by_id("wood")
	clayEl = driver.find_element_by_id("stone")
	ironEl = driver.find_element_by_id("iron")
	rescArray[0] = re.findall('\d+', woodEl)
	rescArray[1] = re.findall('\d+', clayEl)
	rescArray[3] = re.findall('\d+', ironEl)
	return rescArray

########################################################################
# Return a building level of a specific building
def BuildingLevel(driver, building):
	goToBuilding(0)
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
	goToBuilding(100)
