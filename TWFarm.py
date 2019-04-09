########################################################################
#Author: Floris van Rossum
#Purpose: Provide all the necessary functions for sending a specified number of
#		  troops out to farm
########################################################################
import re

class Farm:

    def __init__(self, file_name):
        villages = self.read_villages_file(file_name)
        print(villages)

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