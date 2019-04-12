########################################################################
#TWBot v3.0
#Author: Floris
#Purpose: Bot for Tribal Wars

########################################################################
#IMPORT STATEMENTS

#System Imports
import sys, os
import time

#HomeMade Imports
import TWBuild
import TWFarm
import TWStartup
import TWTroops
#import TWFind

########################################################################
#INFO

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
#FUNCTIONS

#Waiting for page to load
def pageLoad(times):
    time.sleep(times)

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
        self.farm = TWFarm.Farm(self.driver, self.url, self.build, "farm_villages", "templates")

    def update(self):
        self.troops.update_troops()

    def farm(self):
        next_village = self.farm.get_next_village()
        next_attack = self.farm.find_useable_template(self.troops.troops)


# Initialize the bot object
Bot = TWBot()
print("Start-Up Complete!")
print("The current url:" + str(Bot.url))

while (1):
    pageLoad(1)
    Bot.update()
