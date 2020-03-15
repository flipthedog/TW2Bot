########################################################################
# TWBot v3.0
# Author: Floris
# Purpose: Bot for Tribal Wars
########################################################################
# IMPORT STATEMENTS

# System Imports
import time
import random
from selenium.common.exceptions import NoSuchElementException

# HomeMade Imports
import TWBuild
import TWFarm
import TWStartup
import TWTroops

########################################################################
# INSTRUCTIONS

# How templates work:
# 1. Create a template text file (e.g. templates.txt)
# 2. Populate template text file with troops, as shown in attached example template file
# 3. Separate with comma's, spaces or both
# 4. Change the variable "template_name" below, to be equal to the name of your template .txt file

# How farm villages work:
# 1. Create a .txt file for farm villages
# 2. Populate the text file with villages, as shown in attached example
# 3. Separate values with comma's
# 4. Change the variable farm_villages_name to your farm villages filename

########################################################################
# INFO

# Move Chart:
# 100. Overview
# 0. Headquarters
# 1. Barracks
# 2. Stable
# 3. Workshop
# 4. Church
# 5. Watchtower
# 6. Academy
# 7. Smithy
# 8. Rally Point
# 9. Statue
# 10. Market
# 11. Timber Camp
# 12. Clay pit
# 13. Iron mine
# 14. Farm
# 15. Warehouse
# 16. Hiding Place
# 17. Wall

########################################################################
# FUNCTIONS

# Waiting for page to load
def pageLoad(times):
    """Wait for page load"""
    time.sleep(random.uniform(0, times) + 1)

########################################################################
# USER DEFINED VARIABLES
template_name = "templates2"
farm_villages_name = "farm_villages2"

########################################################################
# BOT OBJECT

class TWBot:

    def __init__(self):
        self.startup = TWStartup.StartUp()
        self.driver = self.startup.driver
        self.url = self.startup.get_url()
        self.build = TWBuild.Build(self.driver, self.url)
        self.troops = TWTroops.Troops(self.driver, self.url, self.build)
        self.farm = TWFarm.Farm(self.driver, self.url, self.build, farm_villages_name, template_name)

    def update(self):
        """Update function of the bot"""
        if not self.bot_check():
            self.build.update()
            #self.troops.update_troops()
            #self.farm.send_attack(self.troops.troops)
        else:
            return False

    def bot_check(self):
        """Check if the bot captcha code is on the screen"""
        # TODO: More better bot check
        try:
            bot_el = self.driver.find_element_by_class_name("recaptcha-anchor-label")
            if bot_el.text == "I'm not a robot":
                return True
            else:
                return False
        except NoSuchElementException:
            print("No bot-check found")
            return False

########################################################################
# EXECUTION

# Initialize the bot object
Bot = TWBot()
print("Start-Up Complete!")
print("The current url:" + str(Bot.url))

# TODO: Create better loop conditions & states
#checker = True
# while (1):
#     # Check if bot state is triggered
#
#     Bot.update()
#     pageLoad(5)