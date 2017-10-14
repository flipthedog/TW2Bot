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
	def __init__(self,url):
		self.nextBuildProject #Put some function here later that determines
		self.url
		# the next build project

	def BuildNext():
		hello
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

def startBuild(driver, building ):
    if(building == 0):
        #Upgrade HQ
        goToBuilding(driver,0)
        buildElt = driver.find_elements_by_xpath("//a[@data-building = 'main']")
        time.sleep(2)
        buildElt[1].click()
        time.sleep(2)
        goToBuilding(driver, 100)
    if(building == 1):
        #Upgrade church
        goToBuilding(driver, 0)
        #insert buildlink here for church later
        driver.find_element_by_id("")
        goToBuilding(driver, 100)
    if(building == 2):
        #Upgrade rally point
        goToBuilding(driver, 0)
        #insert buildlink here for rally point if needed
        driver.find_element_by_id("")
        goToBuilding(driver, 100)
    if(building == 3):
        #Upgrade the statue
        goToBuilding(driver, 0)
        buildElt = driver.find_elements_by_xpath("//a[@data-building = 'statue']")
        time.sleep(2)
        buildElt[1].click()
        time.sleep(2)
        goToBuilding(driver, 100)
    if(building == 4):
        #Upgrade the Timber camp
        goToBuilding(driver, 0)
        buildElt = driver.find_elements_by_xpath("//a[@data-building = 'wood']")
        time.sleep(2)
        buildElt[1].click()
        time.sleep(2)
        goToBuilding(driver, 100)
    if(building == 5):
        #Upgrade the clay camp
        goToBuilding(driver, 0)
        buildElt = driver.find_elements_by_xpath("//a[@data-building = 'stone']")
        time.sleep(2)
        buildElt[1].click()
        time.sleep(2)
        goToBuilding(driver, 100)
    if(building == 6):
        #Upgrade the iron camp
        goToBuilding(driver, 0)
        buildElt = driver.find_elements_by_xpath("//a[@data-building = 'iron']")
        time.sleep(2)
        buildElt[1].click()
        time.sleep(2)
        goToBuilding(driver, 100)
    if(building == 7):
        #Upgrade the farm
        goToBuilding(driver, 0)
        buildElt = driver.find_elements_by_xpath("//a[@data-building = 'farm']")
        time.sleep(2)
        buildElt[1].click()
        time.sleep(2)
        goToBuilding(driver, 100)
    if(building == 8):
        #Upgrade the warehouse
        goToBuilding(driver, 0)
        buildElt = driver.find_elements_by_xpath("//a[@data-building = 'storage']")
        time.sleep(2)
        buildElt[1].click()
        time.sleep(2)
        goToBuilding(driver, 100)
    if(building == 9):
        #Upgrade the hideout
        goToBuilding(0)
        buildElt = driver.find_elements_by_xpath("//a[@data-building = 'hide']")
        time.sleep(2)
        buildElt[1].click()
        time.sleep(2)
        goToBuilding(100)
	###########UPDATELATER#######
    if(building == 10):
        #Upgrade the farm
        goToBuilding(0)
        buildElt = driver.find_elements_by_xpath("//a[@data-building = 'hide']")
        time.sleep(2)
        buildElt[1].click()
        time.sleep(2)
        goToBuilding(100)
    if(building == 11):
        #Upgrade the farm
        goToBuilding(0)
        buildElt = driver.find_elements_by_xpath("//a[@data-building = 'hide']")
        time.sleep(2)
        buildElt[1].click()
        time.sleep(2)
        goToBuilding(100)
    if(building == 12):
        #Upgrade the farm
        goToBuilding(0)
        buildElt = driver.find_elements_by_xpath("//a[@data-building = 'hide']")
        time.sleep(2)
        buildElt[1].click()
        time.sleep(2)
        goToBuilding(100)
    if(building == 13):
        #Upgrade the farm
        goToBuilding(0)
        buildElt = driver.find_elements_by_xpath("//a[@data-building = 'hide']")
        time.sleep(2)
        buildElt[1].click()
        time.sleep(2)
        goToBuilding(100)
    if(building == 14):
        #Upgrade the farm
        goToBuilding(0)
        buildElt = driver.find_elements_by_xpath("//a[@data-building = 'hide']")
        time.sleep(2)
        buildElt[1].click()
        time.sleep(2)
        goToBuilding(100)
    if(building == 15):
        #Upgrade the farm
        goToBuilding(0)
        buildElt = driver.find_elements_by_xpath("//a[@data-building = 'hide']")
        time.sleep(2)
        buildElt[1].click()
        time.sleep(2)
        goToBuilding(100)
    if(building == 16):
        #Upgrade the farm
        goToBuilding(0)
        buildElt = driver.find_elements_by_xpath("//a[@data-building = 'hide']")
        time.sleep(2)
        buildElt[1].click()
        time.sleep(2)
        goToBuilding(100)

########################################################################
# Figure out if the build queue is empty
def QueueEmpty(driver):
    try:
        goToBuilding(0) # go to the headquarters
        queueElt = driver.find_elements_by_class_name("order_feature btn btn-btr btn-instant")
    except NoSuchElementException:
        goToBuilding(100) # Return to the home screen
        return True
        pass
    return 1>=len(queueElt)

########################################################################
# Figure out if requirements to build a building are met
def CanBuild(driver, building):
	rescources

########################################################################
# Check if there is enough farm space
def CheckFarm(driver):
	goToBuilding(0) # ensure we are in overview
	maxPop = int(driver.find_element_by_id("pop_max_label").text)
	usedPop = int(driver.find_element_by_id("pop_current_label").text)
	percent = float((usedPop / maxPop))
	return percent < 0.9

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
