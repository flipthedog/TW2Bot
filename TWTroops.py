########################################################################
#Author: Floris van Rossum
#Purpose: Provide all the necessary functions for sending a specified number of
#		  troops out to farm
########################################################################
class Troops:

    def __init__(self):
        # Troop storage array
        # 0 - SPEAR
        # 1 - SWORD
        # 2 - AXE
        # 3 - ARCHER
        # 4 - SCOUT
        # 5 - LC (Light Cavalry)
        # 6 - MA (Mounted Archer)
        # 7 - HC (Heavy Cavalry)
        # 8 - RAM
        # 9 - CATAPULT
        # 10 - PALADIN
        # 11 - NOBLEMAN
        # 12 - MILITIA
        self.troops = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Resource storage array
        # 0 - WOOD
        # 1 - CLAY
        # 2 - IRON
        self.resources = [0, 0, 0]
