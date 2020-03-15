########################################################################
#Author: Floris
#Purpose: Setup the bot, setup selenium
########################################################################
#System Imports
import time, re

#Selenium Imports
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

# XML imports
import xml.etree.ElementTree as ET

class StartUp:
    def __init__(self):
        self.url = "" # URL of the home village
        self.domain_url = "" # URL to get world, unit and building data
        self.domain = "" # String containing the domain of the active world
        self.world_number = 0 # Integer representing the active world number

        # Start-up the bot
        self.driver = self.StartUpWindow()

        # Get the world information
        self.world_info = self.generate_world_info()

    # Start-Up Function
    # Creates selenium driver, initializes window to village headquarters screen
    def StartUpWindow(self):
        """Start up the bot, selenium"""
        # TODO: More error handling for login
        driver = webdriver.Chrome(executable_path=r"C:\Users\Jan\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")

        chrome_options = webdriver.ChromeOptions() #Not needed?

        #self.domain = input("Enter server domain (.net, .ge, .ch, etc.): ")
        #driver.get("https://www.tribalwars" + self.domain + "/")

        driver.get("https://www.tribalwars.us/")

        elemUserName = driver.find_element_by_id("user")
        elemPassword = driver.find_element_by_id("password")
        elemLogIn = driver.find_element_by_class_name("btn-login")

        username = input("Username: ")
        password = input("Password: ")
        print("You entered username: ", username, " password: ", password)

        elemUserName.send_keys(username)
        elemPassword.send_keys(password)
        elemLogIn.click()

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
        print("Original url: ", tempURL)

        # Retrieve the current domain and world number
        substr = tempURL[8:].split('.')
        match = re.match(r"([a-z]+)([0-9]+)", substr[0], re.I)
        if match:
            items = match.groups()

        self.world_number = int(items[1])
        self.domain = items[0]

        print("World number: ", self.world_number)
        print("Domain:", self.domain)

        self.domain_url = tempURL.split("game.php")[0]

        self.url = tempURL.split("screen=")[0] + "screen="

        # https://us30.tribalwars.us/game.php?village=8191&screen=overview
        # https://en107.tribalwars.net/game.php?village=12186&screen=overview
        # https://us30.tribalwars.us/game.php?village=8191&screen=main


        return driver

    # Return the home function of the village
    def get_url(self):
        """Return the url of the home village"""
        print(self.url)
        return str(self.url)

    def generate_world_info(self):
        """
        Create a .txt file containing the relevant world information
        If no existing file is present, overwrite existing information
        :return: None, generates a .txt file
        """

        world_config_url = '/interface.php?func=get_config'
        self.driver.get(self.domain_url + world_config_url)
        source = self.driver.page_source
        text_file = open("worldinfo.xml", "w")
        n = text_file.write(source)
        text_file.close()

        new_source = source.split("</style>")[0]
        new_source = new_source.split("</win>")[0]
        print(new_source)
        root = ET.fromstring(new_source)


        info = {}

        for child in root.iter():
            tagname = child.tag
            info[tagname] = child.text
            if tagname is "wind":
                continue
            print(child.tag, child.attrib, child.text)

        #print(source)



    def generate_building_info(self):
        """
        Create a .txt file containing the relevant information for building
        If no existing file is present, overwrite existing information
        :return: None, generates a .txt file
        """
        building_info_url = '/interface.php?func=get_building_info'

    def generate_unit_info(self):
        """
        Create a .txt file containing the relevant unit informatio
        :return:
        """
        unit_info_url = '/interface.php?func = get_unit_info'

#Waiting for page to load
def pageLoad(times):
    """Wait for the page to load"""
    time.sleep(times)
