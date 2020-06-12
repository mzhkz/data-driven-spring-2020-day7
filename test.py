
a = [10, 15, 0, 20, 30]
b = [10, 20, 15, 15, 20]


for i in range(0, len(a)-2):
    # シグマ計算 Σt=T,t+w (aT-bT)**2
    numerator = sum( [(a[k1] - b[k1])**2 for k1 in range(i, i+3)] ) # h = (time + weigh) - time
    # シグマ計算 Σt=T,t+w (aT**2 + bT**2)
    denominator = sum( [(a[k2]**2 + b[k2]**2) for k2 in range(i, i+3)] ) # h = (time + weigh) - time
    print(numerator / denominator)