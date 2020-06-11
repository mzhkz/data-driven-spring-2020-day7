import pprint
import csv

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

import statistics as statics
import math
import os

import person


# target to interpret csv
path = "./data"

# get list of files
files = os.listdir(path)


# load to targers
persons = [ 
    person.Person(p.replace(".csv", ""), path+"/"+p) # convert to person object.
    for p in files # targets to convert
    if os.path.isfile(os.path.join(path, p)) # if type is file
    ]

# print([(x.name, len(x.steps)) for x in persons])
print("")
print("")
print("{0}さん and {1}さん".format(persons[5].name, persons[6].name))

print(persons[0].compete(other = persons[1], day = 2))