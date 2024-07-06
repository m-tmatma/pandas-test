#!/usr/bin/python3
'''
sin
'''
import numpy as np
import pandas as pd

# サンプル数と範囲を設定
num_samples = 100
x = np.linspace(0, 2 * np.pi, num_samples)

# sin波を計算
y = np.sin(x)

# DataFrameを作成
df = pd.DataFrame({'X': x, 'Y': y})

# DataFrameを表示
print(df)
