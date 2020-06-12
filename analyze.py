import matplotlib.pyplot as plt


def describe(anyone, day):
    fig, ax = plt.subplots()

    step_d = anyone.steps[1440*day:1440*(day+1)]
    count_x = 0.0

    for step in step_d:
        plt.bar(count_x, # バーの左端と重なるx座標
            step[2], # バーの高さ
            0.3, # バーの幅
            0, # バーが始まる高さ
            color="red", # 色
        )
        count_x += 0.15

    # グラフデザイン
    plt.grid(False) #グリッドを表示
    plt.title('{0} ~ {1}'.format(step_d[0], step_d[len(step_d)-1])) # グラフのタイトル

    # ラベルを打つ
    label = ["{}:00".format(x) for x in range(0, 25)] # X軸のラベル
    ax.set_xticks([x * (0.15 * 60) for x in range(0, 25)]) #ラベルを表示するX軸座標を指定
    ax.set_xticklabels(label, rotation = 0, fontsize=5) #表示するラベル

    print(anyone.name)

    # 描画
    plt.show()