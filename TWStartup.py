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
from selenium.webdriver.common.action_chains import ActionChains

class StartUp:
	villageURL = "Empty"
	def __init__(self):
		self.driver = self.StartUpWindow()

	#Start-Up Function
	#Creates selenium driver, initializes window to village headquarters screen
	def StartUpWindow(self):
		driver = webdriver.Chrome(executable_path=r"C:\Users\Jan\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")
		chrome_options = webdriver.ChromeOptions() #Not needed?

		driver.get("https://www.tribalwars.us/")
		elemUserName = driver.find_element_by_id("user")
		elemPassword = driver.find_element_by_id("password")
		elemLogIn = driver.find_element_by_class_name("btn-login")

		username = input("Username: ")
		password = input("Password: ")

		elemUserName.send_keys(username)
		elemPassword.send_keys(password)
		elemLogIn.click()

		#Enable if chrome says "Do you want to save your password?"
		pageLoad(1) #wait for page to load

		#Clicking on the correct world
		try:
			elemWorld = driver.find_element_by_class_name("world_button_active")
			elemWorld.click()
		except NoSuchElementException:
			print("Error: No active worlds, start a world")
			exit()

		pageLoad(1) #wait for page to load

		#Trying to find popup box if it opens up
		#i.e. daily rewards
		try:
			elemPopBox = driver.find_element_by_id("popup_box_daily_bonus")
			elemOpenHourly = driver.find_element_by_link_text("Open")
			elemOpenHourly.click()
		except NoSuchElementException:
			pass #No daily reward, don't do anything

		#Now the program is in the main screen:
		# reload the village overview to get the href link
		actions = ActionChains(driver)
		actions.send_keys('v')
		actions.perform()

		# wait for the page to load, update link
		pageLoad(1)
		tempURL = str(driver.current_url)
		self.villageURL = tempURL[0:56]
		# https://us30.tribalwars.us/game.php?village=8191&screen=overview
		# https://us30.tribalwars.us/game.php?village=8191&screen=main
		return driver

	# Return the home function of the village
	def getURL(self):
		return str(self.villageURL)

	def getDriver(self):
		return self.driver

#Waiting for page to load
def pageLoad(times):
	time.sleep(times)

#Click function clicks on screen at x,y
#Necessary in order to get past notifications
def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
