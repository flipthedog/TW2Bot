########################################################################
#Author: Floris
#Purpose: Provide all the necessary functions for building buildings
########################################################################
#Import statments
import time, random
import selenium
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.alert import Alert #Not needed?
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import TWStartup
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
#going into a certain building

class Build:

    def __init__(self, driver, url):
        self.levels = []
        self.cost = []
        self.population_free = 0
        self.population_total = 0
        
        self.driver = driver
        self.url = url

        # Resource storage array
        # 0 - WOOD
        # 1 - CLAY
        # 2 - IRON
        self.resources = [0, 0, 0]

    # TODO: Write update function to determine building level, cost, population
    def update(self):
        self.building(0)

        elements = self.driver.find_elements_by_id("main_buildrow_main")

        for el in elements:
            print(el, el.text)
    
    def custom_building(self, url, custom_appendix):
        time.sleep(random.uniform(0, 3) + 1)

        if custom_appendix == "place&mode=units" or custom_appendix == "units":
            self.driver.get(url + "place&mode=units")

        time.sleep(random.uniform(0, 3) + 1)

    # Visit a certain building
    def building(self, x):
        if(x == 100 or x == "overview"):
            #Main screen
           self.driver.get(self.url+"overview")
        if(x == 0 or x == "main"):
            #Headquarters screen
           self.driver.get(self.url + "main")
        if(x == 1 or x == "church_f"):
            #Church Screen
           self.driver.get(self.url + "church_f")
        if(x == 2 or x == "place"):
            #Rallypoint screen
           self.driver.get(self.url + "place")
        if(x == 3 or x == "statue"):
            #statue Screen
           self.driver.get(self.url + "statue")
        if(x == 4 or x == "wood"):
            #TimberCamp screen
           self.driver.get(self.url + "wood")
        if(x == 5 or x == "stone"):
            #Clay camp Screen
           self.driver.get(self.url + "stone")
        if(x == 6 or x == "iron"):
            #Iron mine screen
           self.driver.get(self.url + "iron")
        if(x == 7 or x == "farm"):
            #Farm Screen
           self.driver.get(self.url + "farm")
        if(x == 8 or x == "store"):
            #Warehouse screen
           self.driver.get(self.url + "store")
        if(x == 9):
            #Hiding Place Screen
            TWStartup.driver.get("https://us29.tribalwars.us/game.php?village=4444&screen=church_f")

        time.sleep(random.uniform(0, 3) + 1)

########################################################################
