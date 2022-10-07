#!/usr/bin/python3
# -*- coding: utf-8 -*-
''''
unix epoch time を DataFrame (UTC, JST) に変換する。

以下のモジュールのインストールが必要
pandas
'''
import time
import pandas as pd

nowt  = int(time.time())
df = pd.DataFrame( {'time' : [nowt] })

df['utc']   = pd.to_datetime(df["time"], unit='s', utc=True)
df['local'] = df['utc'].dt.tz_convert('Asia/Tokyo')
print(df)
