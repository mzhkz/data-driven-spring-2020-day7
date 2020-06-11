import csv
import pprint


class Person:
    name = ""
    file = ""
    steps = [0]

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



    # 他人と歩数を比べ、動向検知手法による類似度を計算
    def compete(self, other, day):

        #1440分 = 1 DAY
        m_step = self.steps[1440*day:1440*day+1] #指定日の歩数をくり抜き
        o_step = other.steps[60*day:60*day+1] #指定日の歩数をくり抜き

        result = []

        for h in range(0, 23): #0時から23時までをまとめて算出
            v_active = self.calculation(weigh = 60, s1 = m_step[60*h:60*h+1], s2 = o_step[60*h:60*h+1])
            result.append(v_active)

        return result



    #活動量検知方法、類似度による指数算出および、非類似度の算出の値を返す
    def calculation(self, weigh, s1, s2):

        # シグマ計算 Σt=T,t+w (aT-bT)**2
        numerator = sum( [(s1[k][2] - s2[k][2])**2 for k in range(0, weigh-1)] ) # h = (time + weigh) - time
        
        # シグマ計算 Σt=T,t+w (aT**2 + bT**2)
        denominator = sum( [(s1[k][2]**2 + s2[k][2]**2) for k in range(0, weigh-1)] ) # h = (time + weigh) - time

        return numerator / denominator


    




#Step per a minute
# class Step:
#     day = 1
#     time = 0
#     step = 