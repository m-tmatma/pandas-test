#!/usr/bin/python3
# -*- coding: utf-8 -*-
''''
指定した値の変化点を調べるテストスクリプト
'''
import numpy as np
import pandas as pd

num   = 4
elem  = 100

state = np.random.randint(num, size=elem)
start_x = 0
start_y = 100
x     = np.arange(start_x, start_x+elem)
y     = np.arange(start_y, start_y+elem)

df = pd.DataFrame( {'x' : x, 'y' : y, 'state': state })

states = df['state']

df['change'] = states != states.shift()
dfChange = df[ df['change'] ]

df.to_csv("df.csv", index=False)
dfChange.to_csv("df_change.csv", index=False)
