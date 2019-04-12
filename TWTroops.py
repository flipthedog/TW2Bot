########################################################################
#Author: Floris
#Purpose: Provide all the necessary functions for sending a specified number of
#		  troops out to farm
########################################################################
class Troops:

    def __init__(self, driver, url, build):
        self.driver = driver
        self.url = url
        self.build = build
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



    # Update the amount of troops currently in the village
    def update_troops(self):
        self.build.custom_building(self.url, "units")
        updated_troops = []
        updated_troops.append(int(self.driver.find_element_by_class_name("unit-item-spear").text))
        updated_troops.append(int(self.driver.find_element_by_class_name("unit-item-sword").text))
        updated_troops.append(int(self.driver.find_element_by_class_name("unit-item-axe").text))
        updated_troops.append(int(self.driver.find_element_by_class_name("unit-item-archer").text))
        updated_troops.append(int(self.driver.find_element_by_class_name("unit-item-spy").text))
        updated_troops.append(int(self.driver.find_element_by_class_name("unit-item-light").text))
        updated_troops.append(int(self.driver.find_element_by_class_name("unit-item-marcher").text))
        updated_troops.append(int(self.driver.find_element_by_class_name("unit-item-heavy").text))
        updated_troops.append(int(self.driver.find_element_by_class_name("unit-item-ram").text))
        updated_troops.append(int(self.driver.find_element_by_class_name("unit-item-catapult").text))
        updated_troops.append(int(self.driver.find_element_by_class_name("unit-item-knight").text))
        updated_troops.append(int(self.driver.find_element_by_class_name("unit-item-snob").text))
        updated_troops.append(int(self.driver.find_element_by_class_name("unit-item-militia").text))
        self.troops = updated_troops
        return self.troops
