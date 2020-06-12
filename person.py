import csv
import pprint
import store
import copy


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
    def compete(self, other):
        # print("#0 {0}, {1}".format(len(self.steps), len(other.steps)))

        m_step = self.steps.copy().tolist()
        o_step = other.steps.copy().tolist()

        p_flag = 0

        for m in range(0, len(self.steps) - 59): #0時から23時までをまとめて算出
            c_weight = 60
            s1 = m_step[m:m+60].copy().tolist()
            s2 = o_step[m:m+60].copy().tolist()


            v_active = self.calculation(weigh = c_weight, s1 = s1, s2 = s2)
            # print("{0}分目 = {1} の行動指数 {2}".format(m, m_step[0][0], v_active))

            if v_active <= 0.05:
                p_flag += 1 #ポイント追加
                
                if p_flag <= 15: #15分以上だとさらに追加
                    store.add_and_update(p1 = self, p2 = other, val = 1) #仲良しポイントを追加
            else:
                p_flag = 0 #初期化


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


    
