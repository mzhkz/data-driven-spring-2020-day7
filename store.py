from itertools import combinations
import hashlib
import datetime

t_persons = [] #ユーザー
t_pairs = [] #ペア一覧


def i_states(person):
    global t_persons
    t_persons = person

    print("    {}人のデータを読み込みました".format(len(t_persons)))


#2組ずつにペア訳を行う
def combinate():
    global t_persons
    global t_pairs

    # イテレータからコンビネーションを計算
    combinated = list(combinations(t_persons, 2))
    for pair in combinated:
        t_pairs.append([pair[0], pair[1], 0])
    print("組合せの数：{}".format(len(t_pairs)))



#なかよし度を追加する
def add_and_update(p1, p2, val):
    global t_pairs

    sort_p2 = [p1.name, p2.name] #並び替える。コンビネーションなのでペアは一つだけ
    sort_p2.sort()
    for pair in t_pairs:
        sort_p1 = [pair[0].name, pair[1].name] 
        sort_p1.sort()

        if sort_p1[0] == sort_p2[0] and sort_p1[1] == sort_p2[1]:
            pair[2] += val #変数を置き換え
            print(".." + 
                datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S") 
                + "  {0} 仲良し度が追加された 合計{1}".format("{0} and {1}".format(p1.name, p2.name) ,pair[2]))

    
