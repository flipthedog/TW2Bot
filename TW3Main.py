########################################################################
# TWBot v3.0
# Author: Floris
# Purpose: Bot for Tribal Wars

########################################################################
# IMPORT STATEMENTS

# System Imports
import time, random

# HomeMade Imports
import TWBuild
import TWFarm
import TWStartup
import TWTroops

########################################################################
# INFO

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
    time.sleep(random.uniform(0, times) + 1)

########################################################################
#Main Program
# The start-up object
# Constructor starts up the program
#StartUp = TWStartup.StartUp()


class TWBot:

    def __init__(self):
        self.startup = TWStartup.StartUp()
        self.driver = self.startup.driver
        self.url = self.startup.get_url()
        self.build = TWBuild.Build(self.driver, self.url)
        self.troops = TWTroops.Troops(self.driver, self.url, self.build)
        self.farm = TWFarm.Farm(self.driver, self.url, self.build, "farm_villages2", "templates2")

    def update(self):
        #self.build.update()
        self.troops.update_troops()
        self.farm.send_attack(self.troops.troops)


# Initialize the bot object
Bot = TWBot()
print("Start-Up Complete!")
print("The current url:" + str(Bot.url))

while (1):
    Bot.update()
    pageLoad(5)
