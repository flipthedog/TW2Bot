########################################################################
# Author: Floris
# Purpose: Provide all the necessary functions for building buildings
########################################################################
# Import statments
import time
import random
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
        self.levels = {}
        self.cost = []
        self.points = 0
        self.population_free = 0
        self.population_total = 0
        
        self.driver = driver
        self.url = url

        # Resource storage array
        # 0 - WOOD
        # 1 - CLAY
        # 2 - IRON
        self.resources = [0, 0, 0]

    def update(self):
        """Update function of the build object"""
        self.update_buildings()
        self.update_resources()
        self.points = int(self.driver.find_element_by_id("rank_points").text)

    def update_population(self):
        """Update the object with the population currently in the village"""
        current_pop = int(self.driver.find_element_by_id("pop_current_label").text)
        max_pop = int(self.driver.find_element_by_id("pop_max_label").text)
        self.population_total = max_pop
        self.population_free = max_pop - current_pop

    def update_resources(self):
        """Update the resources currently in the village"""
        wood_element = self.driver.find_element_by_id("wood")
        stone_element = self.driver.find_element_by_id("stone")
        iron_element = self.driver.find_element_by_id("iron")
        self.resources = [int(wood_element.text), int(stone_element.text), int(iron_element.text)]
        # print(self.resources)

    def update_buildings(self):
        """Store the current building levels"""
        #TODO: Fix edge cases for unfinished, completed buildings
        self.building(0)
        levels = {}

        try:
            headquarters_element = self.driver.find_element_by_id("main_buildrow_main")
            levels["headquarters"] = (int(headquarters_element.text.split()[2]))
        except NoSuchElementException:
            pass

        try:
            barracks_element = self.driver.find_element_by_id("main_buildrow_barracks")
            levels["barracks"] = (int(barracks_element.text.split()[2]))
        except NoSuchElementException:
            pass

        try:
            stable_element = self.driver.find_element_by_id("main_buildrow_stable")
            levels["stable"] = (int(stable_element.text.split()[2]))
        except NoSuchElementException:
            pass

        try:
            garage_element = self.driver.find_element_by_id("main_buildrow_garage")
            levels["garage"] = (int(garage_element.text.split()[2]))
        except NoSuchElementException:
            pass

        try:
            smith_element = self.driver.find_element_by_id("main_buildrow_smithy")
            levels["smith"] = (int(smith_element.text.split()[2]))
        except NoSuchElementException:
            pass

        try:
            academy_element = self.driver.find_element_by_id("main_buildrow_academy")
            levels["academy"] = (int(academy_element.text.split()[2]))
        except NoSuchElementException:
            levels["academy"] = 0

        try:
            church_element = self.driver.find_element_by_id("main_buildrow_church_f")
            levels["church"] = (int(church_element.text.split()[3]))
        except NoSuchElementException:
            levels["church"] = 0

        try:
            place_element = self.driver.find_element_by_id("main_buildrow_place")
            levels["place"] = int(place_element.text.split()[3])
        except (NoSuchElementException, ValueError) as e:
            levels["place"] = 0

        try:
            statue_element = self.driver.find_element_by_id("main_buildrow_statue")
            levels["statue"] = (int(statue_element.text.split()[2]))
        except (NoSuchElementException, ValueError) as e:
            levels["statue"] = 0

        try:
            market_element = self.driver.find_element_by_id("main_buildrow_market")
            levels["market"] = (int(market_element.text.split()[2]))
        except (NoSuchElementException, ValueError) as e:
            levels["market"] = 0

        try:
            wood_element = self.driver.find_element_by_id("main_buildrow_wood")
            levels["wood"] = (int(wood_element.text.split()[3]))
        except (NoSuchElementException, ValueError) as e:
            levels["wood"] = 0

        try:
            stone_element = self.driver.find_element_by_id("main_buildrow_stone")
            levels["stone"] = (int(stone_element.text.split()[3]))
        except (NoSuchElementException, ValueError) as e:
            levels["stone"] = 0

        try:
            iron_element = self.driver.find_element_by_id("main_buildrow_iron")
            levels["iron"] = (int(iron_element.text.split()[3]))
        except (NoSuchElementException, ValueError) as e:
            levels["iron"] = 0

        try:
            farm_element = self.driver.find_element_by_id("main_buildrow_farm")
            levels["farm"] = (int(farm_element.text.split()[2]))
        except NoSuchElementException:
            levels["farm"] = 0

        try:
            storage_element = self.driver.find_element_by_id("main_buildrow_storage")
            levels["storage"] = (int(storage_element.text.split()[2]))
        except NoSuchElementException:
            levels["storage"] = 0

        try:
            hide_element = self.driver.find_element_by_id("main_buildrow_hide")
            levels["hide"] = (int(hide_element.text.split()[3]))
        except (NoSuchElementException, ValueError) as e:
            levels["hide"] = 0

        try:
            wall_element = self.driver.find_element_by_id("main_buildrow_wall")
            levels["wall"] = (int(wall_element.text.split()[2]))
        except (NoSuchElementException, ValueError) as e:
            levels["wall"] = 0

        # print("Levels: ", levels)
        self.levels = levels
        self.building(100)

    def custom_building(self, url, custom_appendix):
        """Go to a custom url of a building"""
        time.sleep(random.uniform(0, 3) + 1)

        if custom_appendix == "place&mode=units" or custom_appendix == "units":
            self.driver.get(url + "place&mode=units")

        time.sleep(random.uniform(0, 3) + 1)

    # Visit a certain building
    def building(self, x):
        """Go to a specific building, follow the commented guides for building number & names"""
        if(x == 100 or x == "overview"):
            #Main screen
           self.driver.get(self.url+"overview")
        if(x == 0 or x == "main"):
            #Headquarters screen
           self.driver.get(self.url + "main")
        if(x == 4 or x == "church_f"):
            #Church Screen
           self.driver.get(self.url + "church_f")
        if(x == 8 or x == "place"):
            #Rallypoint screen
           self.driver.get(self.url + "place")
        if(x == 9 or x == "statue"):
            #statue Screen
           self.driver.get(self.url + "statue")
        if(x == 11 or x == "wood"):
            #TimberCamp screen
           self.driver.get(self.url + "wood")
        if(x == 12 or x == "stone"):
            #Clay camp Screen
           self.driver.get(self.url + "stone")
        if(x == 13 or x == "iron"):
            #Iron mine screen
           self.driver.get(self.url + "iron")
        if(x == 14 or x == "farm"):
            #Farm Screen
           self.driver.get(self.url + "farm")
        if(x == 15 or x == "store"):
            #Warehouse screen
           self.driver.get(self.url + "store")
        if(x == 16 or x == "hide"):
            #Hiding Place Screen
            self.driver.get(self.url + "hide")
        if(x == 1 or x == "barracks"):
            # Barracks Screen
            self.driver.get(self.url + "barracks")
        if(x == 2 or x == "stable"):
            # Stable Screen
            self.driver.get(self.url + "stable")
        if (x == 3 or x == "workshop"):
            # Workshop screen
            self.driver.get(self.url + "garage")
        if (x == 6 or x == "academy"):
            # Academy Screen
            self.driver.get(self.url + "academy")
        if (x == 7 or x == "smith"):
            # Smith Screen
            self.driver.get(self.url + "smith")
        if (x == 10 or x == "market"):
            # Market Screen
            self.driver.get(self.url + "market")
        if (x == 17 or x == "wall" ):
            # Wall Screen
            self.driver.get(self.url + "wall")

        time.sleep(random.uniform(0, 3) + 1)

########################################################################
