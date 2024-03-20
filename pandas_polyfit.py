import pandas as pd
import numpy as np

# 仮のデータフレームを作成
start_x = 10
start_y = 100
num     = 150
df = pd.DataFrame({
    'x': np.arange(start_x, start_x+num),
    'y': np.arange(start_y, start_y+num) + np.random.randn(num)
})

# 'x'列と'y'列に対して1次の多項式フィットを行う
coeff = np.polyfit(df['x'], df['y'], 1)
vfunc = np.vectorize(lambda x: coeff[0] * x + coeff[1])

df["fit"]  = df['x'].apply(vfunc)
df["error"] = (df['fit'] - df['y']).abs()
df["rate%"] = (df['error'] / df["y"]) * 100
print(df)
