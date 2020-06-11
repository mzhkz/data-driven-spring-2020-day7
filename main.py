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
import store


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
store = store.Store(persons)
store.combinate()


#各ペアの行動類似度を計算し、指定された条件とともにポイントを追加
for p in store.t_pairs:

    for d in range(0, 17):
         results = p[0].compete(other = p[1], day = d)

         for r in results:
             if (r <= 0.05):
                 store.add_and_update(p1 = p[0], p2 = p[1], val = 1) #仲良しポイントを追加
    


#処理終了
finished_date = datetime.datetime.today()
exec_time = finished_date.timestamp() * 1000 - start_date.timestamp() * 1000
print("")
print("")
print("    処理時間 {} ms".format(round(exec_time)))
print("")
print("-----------------------------------------------") 