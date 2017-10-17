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

class TWChoice:
	def __init__(self,driver,url):
		self.driver = driver
		self.url = url

	def nextBuild():
		self.nexti = nextBuilding(self.driver,self.url)
		return nexti

def nextBuilding(driver,url):
	print("this is the level of the woodcutting camp: " + BuildingLevel(driver,url,4))
