#!/usr/bin/python
''''
指定した値の継続時間(duration)を計算するテストスクリプト
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

nrows = 2
ncols = 2
num   = nrows * ncols

cm = plt.cm.get_cmap('tab20')

fig = plt.figure()
for i in range(num):
    ax = fig.add_subplot(nrows, ncols, i+1)

    state = np.random.randint(3+i, size=100)
    x     = np.arange(100)
    y     = np.arange(100,200)

    df = pd.DataFrame( {'x' : x, 'y' : y, 'state': state })

    states = df['state']

    df['change'] = states != states.shift(-1)
    dfChange = df[ df['change'] ]

    # ダミー要素に与える x 値を計算する
    diffX = df.diff(-1)["x"][0]

    # 先頭にダミーの要素を追加して、最初の項目の差分を計算できるようにする
    dfTemp = pd.DataFrame( {'x' : [diffX], 'state': False }, index=[-1])
    dfChange = dfTemp.append(dfChange)

    dfdiff_dfChange = dfChange.diff()

    df['duration'] = dfdiff_dfChange['x']
    #dfChange['duration'] = dfdiff_dfChange['x'].abs()

    df.to_csv("df_" + str(i) + ".csv")

    ax.hist(df['duration'].values, bins=range(6), label=str(i), color=cm.colors[i])
    ax.legend()

fig.savefig("img.png")
