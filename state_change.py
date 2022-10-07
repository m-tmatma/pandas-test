#!/usr/bin/python3
# -*- coding: utf-8 -*-
''''
指定した値の変化点を調べるテストスクリプト
'''
import numpy as np
import pandas as pd

num   = 4

state = np.random.randint(num, size=100)
x     = np.arange(100)
y     = np.arange(100,200)

df = pd.DataFrame( {'x' : x, 'y' : y, 'state': state })

states = df['state']

df['change'] = states != states.shift()
dfChange = df[ df['change'] ]

df.to_csv("df.csv", index=False)
dfChange.to_csv("df_change.csv", index=False)
