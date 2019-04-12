########################################################################
#Author: Floris
#Purpose: Provide all the necessary functions for sending a specified number of
#		  troops out to farm
########################################################################
import re

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

    # Return the next village to farm
    def get_next_village(self):
        return self.villages[self.village_index + 1]

    # Get the useable template
    def find_useable_template(self, current_troops):

        for template in self.template_array:

            for i in len(current_troops):

                if template[i] > current_troops[i]:
                    break

            return template

        return [-1]

    def read_templates(self, file_name):
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