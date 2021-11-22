import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

state = np.random.randint(3, size=100)
x     = np.arange(100)
y     = np.arange(100,200)

df = pd.DataFrame( {'x' : x, 'y' : y, 'state': state })

states = df['state']

df['change'] = states != states.shift(-1)
dfChange = df[ df['change'] ]

# 先頭にダミーの要素を追加して、最初の項目の差分を計算できるようにする
dfTemp = pd.DataFrame( {'x' : [-1], 'state': False }, index=[-1])
dfChange = dfTemp.append(dfChange)

dfdiff_dfChange = dfChange.diff()

df['duration'] = dfdiff_dfChange['x']
#dfChange['duration'] = dfdiff_dfChange['x'].abs()

df.to_csv("df.csv")

fig, ax = plt.subplots()

df['duration'].hist(ax=ax, bins=range(6))
fig.savefig("img.png")
