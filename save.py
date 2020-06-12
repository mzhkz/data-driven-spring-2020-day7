import pathlib
import os

def save_data(pair):
    save1 = pathlib.Path("./output/save1.txt")
    save2 = pathlib.Path("./output/save2.txt")
    
    with save1.open(mode='w') as f:
        for p in pair:
            if p[2] > 0:
                f.write("{0} {1}\n".format(p[0].name, p[1].name))
        f.close()

    with save2.open(mode='w') as f:
        for p in pair:
            if p[2] > 0:
                f.write("{0},{1},{2}\n".format(p[0].name, p[1].name, p[2]))
        f.close()