########################################################################
#Author: Floris
#Purpose: Provide all the necessary functions for sending a specified number of
#		  troops out to farm
########################################################################
import re
import time
import random

class Farm:

    def __init__(self, driver, url, build, farm_file_name, template_file_name):
        self.driver = driver
        self.url = url
        self.build = build

        self.villages = self.read_villages_file(farm_file_name)
        self.village_index = 0

        # An array of arrays of length 13
        # Stores the possible farming templates
        self.template_array = []
        self.read_templates(template_file_name)
        print(self.template_array)

    # Wait a random amount of time
    # Between 1 - 4 seconds
    def random_wait(self):
        """Wait a random amount of time between actions"""
        time.sleep((random.uniform(0, 1) * 3) + 1)

    def is_same(self, array1, array2):
        """Check if two arrays are the same"""
        for el in array1:

            for el2 in array2:

                if el is not el2:
                    return False

        return True

    def send_attack(self, troops):
        """Check for available templates, send troops to village """
        # TODO: Make this more robust
        # TODO: Minimize requests
        next_troops = self.find_usable_template(troops)
        empty_troops = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        print("selected troops: ", next_troops)

        if not self.is_same(next_troops, empty_troops):

            next_village = self.get_next_village()

            self.build.building("place")

            input_elements = self.driver.find_elements_by_class_name("unitsInput")
            village_input = self.driver.find_element_by_class_name("target-input-field")

            village_input.send_keys(str(next_village[0]) + "|" + str(next_village[1]))
            self.random_wait()

            for i in range(len(troops) - 1):
                el = input_elements[i]
                if next_troops[i] is not 0:
                    el.send_keys(next_troops[i])
                    self.random_wait()

            attack_button = self.driver.find_element_by_class_name("btn-attack")
            attack_button.click()

            self.random_wait()

            confirm_button = self.driver.find_element_by_class_name("btn-attack")
            confirm_button.click()
        else:
            print("No available troops")

    # Return the next village to farm
    def get_next_village(self):
        """Return the next villages from all possible villages"""
        return self.villages[self.village_index + 1]

    # Get the usable template
    def find_usable_template(self, current_troops):
        """Go through current troops and determine a useable template"""
        for template in self.template_array:
            print("Checking template:", template)
            j = 0

            for i in range(len(current_troops)):

                if template[i] <= current_troops[i]:
                    j = j + 1
                else:
                    continue

                if j >= 11:
                    print("Return:", template)
                    return template

        print("Return empty template")
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def read_templates(self, file_name):
        """Read the templates storage .txt file"""
        # TODO: More error handling
        if ".txt" not in file_name:
            file_name = file_name + ".txt"
        file = open(file_name, 'r')

        lines = file.readlines()

        for array in lines:

            split_array = re.split(r'[,.\s]', array)
            template = []
            #print(split_array)
            split_array = ' '.join(split_array).split()
            for troop_count in split_array:
                troops = re.sub("[^0-9]", '', troop_count)
                template.append(int(troops))

            self.template_array.append(template)

    def read_villages_file(self, file_name):
        """Read the villages storage .txt file"""
        # TODO: More error handling
        if ".txt" not in file_name:
            file_name = file_name + ".txt"
        file = open(file_name, 'r')

        lines = file.readlines()

        farm_villages = []
        for coordinate in lines:
            split_coord = re.split(r'[,.\s]', coordinate)
            coord_x = re.findall(r'[0-9]{3}', split_coord[0])
            coord_y = re.findall(r'[0-9]{3}', split_coord[1])
            farm_villages.append([int(coord_x[0]), int(coord_y[0])])

        return farm_villages