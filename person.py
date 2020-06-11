import csv
import pprint


class Person:
    name = ""
    file = ""
    steps = [0]
    relation = []

    # クラスコンストラクタ　初期化
    def __init__(self, _name, _file):
        self.name = _name
        self.file = _file

        self.interpret()


    # CSVを解釈
    def interpret(self):
        csv_file = open(self.file, "r", encoding="utf_8", errors="", newline="" )
        f = csv.reader(csv_file,
         delimiter=",", 
         doublequote=True, 
         lineterminator="\r\n", 
         quotechar='"', 
         skipinitialspace=True)

        self.steps = [[step[0], step[1], int(step[2])] for step in list(f)[1:]]

        if len(self.steps) < 24480:
            diff = 24480 - len(self.steps)
            self.steps[0:0] = [["未登録", "データなし", 0] for i in range(0, diff)]
            print("データの付け足しを行いました。{0} に {1}個のデータを追加 計{2}".format(self.name, diff, len(self.steps)))
        



    # 他人と歩数を比べ、動向検知手法による類似度を計算
    def compete(self, other, day):

        # print("#0 {0}, {1}".format(len(self.steps), len(other.steps)))

        #1440分 = 1 DAY
        m_step = self.steps[1440*day:1440*(day+1)] #指定日の歩数をくり抜き
        o_step = other.steps[1440*day:1440*(day+1)] #指定日の歩数をくり抜き

        # print("#12 {0}, {1}".format(len(m_step), len(o_step)))

        result = [] # 24時間分の結果を収納する

        for h in range(0, 24): #0時から23時までをまとめて算出
            c_weight = 60
            v_active = self.calculation(weigh = c_weight, s1 = m_step[c_weight*h:c_weight*(h+1)], s2 = o_step[c_weight*h:c_weight*(h+1)])
            result.append(v_active)
            # print("{0}日目 {1}時 = {2} の行動指数 {3}".format(day, h, m_step[0][0], v_active))

        return result



    #活動量検知方法、類似度による指数算出および、非類似度の算出の値を返す
    def calculation(self, weigh, s1, s2):

        # シグマ計算 Σt=T,t+w (aT-bT)**2
        numerator = sum( [(s1[k1][2] - s2[k1][2])**2 for k1 in range(0, weigh)] ) # h = (time + weigh) - time
        
        # シグマ計算 Σt=T,t+w (aT**2 + bT**2)
        denominator = sum( [(s1[k2][2]**2 + s2[k2][2]**2) for k2 in range(0, weigh)] ) # h = (time + weigh) - time

        if denominator >= 5500: #母数が5500以上
            return numerator / denominator
        else:
            return 2


    
