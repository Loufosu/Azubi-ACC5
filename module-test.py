# import functions  # general import

# print(functions.time.gmtime())

# print(functions.read_data())

#import math

# print(float(math.pi))

# radius = 14
# area_of_circle = math.pi * (radius * radius)
# print(area_of_circle)

# import math
# from math import pi as pi_true
# pi = 23
# radius = 14
# area_of_circle = math.pi_true * (radius * radius)
# print(area_of_circle)

# var = open("file.txt", "r")

# # print(var.read())

# var2 = open("file.txt", "w")
# var2.write(var.read() + "this is what I am writing from python")

# import os
# os.mkdir("test folder")

# print(os.listdir())

# import json

# j_write = open("acc5.json", "w")
# json.dump("my name is Lawrence",j_write)
# print(json.loads(j_write))

def printCategory(age):
    if age > 18:
        print('Adult')
    elif age > 65:
        print('Senior Citizen')
    else:
        print('Child')


printCategory(80)
