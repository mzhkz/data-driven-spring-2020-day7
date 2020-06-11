import pprint
import csv

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from itertools import combinations

import statistics as statics
import copy
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


# イテレータからコンビネーションを計算
c_pair = combinations(persons, 2)
c_pair_list = list(c_pair)
print("組合せの数：{}".format(len(c_pair_list)))


total_result = []

for p in c_pair_list:
    r_com = p[0].compete(other = p[1], day = 0)
    total_result.append(r_com)


#処理終了
print("-----------------------------------------------") 