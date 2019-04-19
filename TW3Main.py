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

# TODO: Fix this list to be consistent
# Upgrade Chart:
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
            pass

    def bot_check(self):
        """Check if the bot captcha code is on the screen"""
        # TODO: More better bot check
        try:
            print("Bot check found")
            self.driver.find_element_by_id("recaptcha-anchor-label")
            return True
        except NoSuchElementException:
            #print("No bot-check found")
            return False

########################################################################
# EXECUTION

# Initialize the bot object
Bot = TWBot()
print("Start-Up Complete!")
print("The current url:" + str(Bot.url))

# TODO: Create better loop conditions & states
while (1):
    Bot.update()
    pageLoad(5)
