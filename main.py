import pprint
import csv

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

import statistics as statics
import datetime
import math
import os

import person


# announce
start_date = datetime.datetime.today()

print("-----------------------------------------------")
print("")
print("")
print("    処理を開始します")
print("    開始時刻 {0}".format(start_date.strftime("%Y/%m/%d %H:%M:%S")))
print("")
print("")

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

#処理終了
print("-----------------------------------------------") 