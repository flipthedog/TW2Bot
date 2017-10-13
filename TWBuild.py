########################################################################
#Author: Floris van Rossum
#Purpose: Provide all the necessary functions for building buildings
########################################################################
#Import statments
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
def building(x):
    if(x == 100):
        #Main screen
        TWStartup.driver.get("https://us29.tribalwars.us/game.php?village=4444&screen=overview")
    if(x == 0):
        #Headquarters screen
        TWStartup.driver.get("https://us29.tribalwars.us/game.php?village=4444&screen=main")
    if(x == 1):
        #Church Screen
        TWStartup.driver.get("https://us29.tribalwars.us/game.php?village=4444&screen=church_f")
    if(x == 2):
        #Rallypoint screen
        TWStartup.driver.get("https://us29.tribalwars.us/game.php?village=4444&screen=main")
    if(x == 3):
        #statue Screen
        TWStartup.driver.get("https://us29.tribalwars.us/game.php?village=4444&screen=church_f")
    if(x == 4):
        #TimberCamp screen
        TWStartup.driver.get("https://us29.tribalwars.us/game.php?village=4444&screen=main")
    if(x == 5):
        #Clay camp Screen
        TWStartup.driver.get("https://us29.tribalwars.us/game.php?village=4444&screen=church_f")
    if(x == 6):
        #Iron mine screen
        TWStartup.driver.get("https://us29.tribalwars.us/game.php?village=4444&screen=main")
    if(x == 7):
        #Farm Screen
        TWStartup.driver.get("https://us29.tribalwars.us/game.php?village=4444&screen=church_f")
    if(x == 8):
        #Warehouse screen
        TWStartup.driver.get("https://us29.tribalwars.us/game.php?village=4444&screen=storage")
    if(x == 9):
        #Hiding Place Screen
        TWStartup.driver.get("https://us29.tribalwars.us/game.php?village=4444&screen=church_f")
########################################################################
