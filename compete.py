import matplotlib.pyplot as plt
import numpy as np


def describe(p1, p2, day):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    p1_step_d = p1.steps[1440*day:1440*(day+1)]
    p2_step_d = p2.steps[1440*day:1440*(day+1)]

    p1_step_d_1 = [sum( map(lambda x: x[2], p1_step_d[60*pi:60*(1+pi)] )) for pi in range(0, 24)]
    p2_step_d_1 = [sum( map(lambda x: x[2], p2_step_d[60*pi:60*(1+pi)] )) for pi in range(0, 24)]


    p1_left = np.array([p1_i * 9 for p1_i in range(0, len(p1_step_d_1))])
    p1_height = np.array([p1_s for p1_s in p1_step_d_1])
    ax1.plot(p1_left, p1_height, color="royalblue")

    p2_left = np.array([p2_i * 9 for p2_i in range(0, len(p2_step_d_1))])
    p2_height = np.array([p2_s for p2_s in p2_step_d_1])
    ax2.plot(p2_left, p2_height, color="crimson")


    # グラフデザイン
    plt.grid(False) #グリッドを表示
    plt.title('{0} ~ {1}'.format(p1_step_d[0], p2_step_d[len(p2_step_d)-1])) # グラフのタイトル

    # ラベルを打つ
    label = ["{}:00".format(x) for x in range(0, 25)] # X軸のラベル
    ax1.set_xticks([x * (0.15 * 60) for x in range(0, 25)]) #ラベルを表示するX軸座標を指定
    ax1.set_xticklabels(label, rotation = 0, fontsize=5) #表示するラベル

    print("{0} {1}".format(p1.name, p2.name))

    # 描画
    plt.show()