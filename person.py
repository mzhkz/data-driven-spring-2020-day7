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




#Step per a minute
# class Step:
#     day = 1
#     time = 0
#     step = 