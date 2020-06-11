import csv


class Person:
    name = ""
    file = ""
    steps = []

    # クラスコンストラクタ　初期化
    def __init__(self, _name, _file):
        self.name = _name
        self.file = _file

    # CSVを解釈
    def interpret(self):
        csv_file = open(self.file, "r", encoding="utf_8", errors="", newline="" )
        f = csv.reader(csv_file,
         delimiter=",", 
         doublequote=True, 
         lineterminator="\r\n", 
         quotechar='"', 
         skipinitialspace=True)

        self.steps = [[step[0], step[1], step[2]] for step in f]

    # 他人と歩数を比べ、動向検知手法による類似度を計算
    def compete(self, other):
        result = 0
        for k in range(0, 10):
            result += k
        return result


    #活動量検知方法、類似度による指数算出および、非類似度の算出の値を返す
    def calculation(self, time, weigh, s1, s2):

        # シグマ計算 Σt=T,t+w (aT-bT)**2
        numerator = sum([(s1[k] - s2[k])**2 for k in range(0, time)]) # h = (time + weigh) - time
        
        # シグマ計算 Σt=T,t+w (aT**2 + bT**2)
        denominator = sum([(s1[k]**2 + s2[k]**2) for k in range(0, time)]) # h = (time + weigh) - time

        return numerator / denominator


    




#Step per a minute
# class Step:
#     day = 1
#     time = 0
#     step = 