########################################################################
#Author: Floris
#Purpose: Setup the bot, setup selenium
########################################################################
#System Imports
import time

#Selenium Imports
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class StartUp:
    def __init__(self):
        self.url = ""
        self.driver = self.StartUpWindow()

    # Start-Up Function
    # Creates selenium driver, initializes window to village headquarters screen
    def StartUpWindow(self):
        """Start up the bot, selenium"""
        # TODO: More error handling for login
        driver = webdriver.Chrome(executable_path=r"C:\Users\Jan\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")
        chrome_options = webdriver.ChromeOptions() #Not needed?

        driver.get("https://www.tribalwars.us/")
        #driver.get("https://www.tribalwars.net/")


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
            print("Error: No active worlds, start a world, or wrong username/password")
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

        self.url = tempURL[0:56]
        #self.villageURL = tempURL[0:59]

        # https://us30.tribalwars.us/game.php?village=8191&screen=overview
        # https://en107.tribalwars.net/game.php?village=12186&screen=overview
        # https://us30.tribalwars.us/game.php?village=8191&screen=main
        return driver

    # Return the home function of the village
    def get_url(self):
        return str(self.url)


#Waiting for page to load
def pageLoad(times):
    """Wait for the page to load"""
    time.sleep(times)
