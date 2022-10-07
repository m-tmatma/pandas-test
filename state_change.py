#!/usr/bin/python3
# -*- coding: utf-8 -*-
''''
指定した値の変化点を調べるテストスクリプト
'''
import numpy as np
import pandas as pd

num   = 4
elem  = 10

state = np.random.randint(num, size=elem)
start_x = 0
start_y = 100
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
print(df['change'].to_markdown())

dfChange = df[ df['change'] ]

df.to_csv("df.csv", index=False)
dfChange.to_csv("df_change.csv", index=False)
print("dfChange")
print(dfChange.to_markdown())
