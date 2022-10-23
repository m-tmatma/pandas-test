#!/usr/bin/python3
# -*- coding: utf-8 -*-
''''
指定した値の変化点を調べるテストスクリプト

以下のモジュールのインストールが必要
numpy
pandas
tabulate
'''
import numpy as np
import pandas as pd

num   = 4

a = np.empty(5)
a.fill(1)

b = np.empty(6)
b.fill(2)

c = np.empty(5)
c.fill(3)

state = np.concatenate([a, b, c, a, b, c])
start_x = 0
start_y = 100

elem  = state.size
x     = np.arange(start_x, start_x+elem)
y     = np.arange(start_y, start_y+elem)

df = pd.DataFrame( {'x' : x, 'y' : y, 'state': state })

states = df['state']
print("df")
print(df.to_markdown())

print("df.shift()")
print(df.shift().to_markdown())

df['change'] = states != states.shift()
print("df['change']")
print(df.to_markdown())

dfChange = df[ df['change'] ]

df.to_csv("df.csv", index=False)
dfChange.to_csv("df_change.csv", index=False)
print("dfChange")
print(dfChange.to_markdown())
