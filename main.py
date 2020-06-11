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
    person.Person(p.replace(".csv", ""), p) # convert to person object.
    for p in files # targets to convert
    if os.path.isfile(os.path.join(path, p)) # if type is file
    ]

print([p.name for p in persons])