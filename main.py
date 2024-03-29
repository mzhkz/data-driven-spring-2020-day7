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
import save
import analyze
import compete
import table


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
files.remove(".DS_Store")

# load to targers
persons = [ 
    person.Person(p.replace(".csv", ""), path+"/"+p) # convert to person object.
    for p in files # targets to convert
    if os.path.isfile(os.path.join(path, p)) # if type is file
]



# イテレータからコンビネーションを計算 
store.i_states(person = persons)
store.combinate()

proc_count = 0
#各ペアの行動類似度を計算し、指定された条件とともにポイントを追加
for p in store.t_pairs:
    proc_count +=1
    print("  {0}ペア目を処理開始..".format(proc_count))
    p[0].compete(other = p[1])


# #保存
save.save_data(store.t_pairs)

# analyze.describe(persons[0], day = 7)
# compete.describe(p1 = persons[0], p2 = persons[1], day = 8)
table.describe(pairs=store.t_pairs)

#処理終了
finished_date = datetime.datetime.today()
exec_time = finished_date.timestamp() * 1000 - start_date.timestamp() * 1000
print("")
print("")
print("    処理時間 {} ms".format(round(exec_time)))
print("")
print("-----------------------------------------------") 
