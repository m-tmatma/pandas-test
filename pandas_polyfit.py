#!/usr/bin/python3
'''
fit by polyfit on dataframe
'''
import time
import pandas as pd
import numpy as np

# 仮のデータフレームを作成
start_x = 10
start_y = 100
num     = 150000
df = pd.DataFrame({
    'x': np.arange(start_x, start_x+num),
    'y': np.arange(start_y, start_y+num) + np.random.randn(num)
})

# 'x'列と'y'列に対して1次の多項式フィットを行う
coeff = np.polyfit(df['x'], df['y'], 1)
vfunc = np.vectorize(lambda x: coeff[0] * x + coeff[1])

# やり方1
start = time.time()
df["fit"]  = df['x'].apply(vfunc)
diff1 = time.time() - start

# やり方2
start = time.time()
df["fit2"]  = vfunc(df['x'])
diff2 = time.time() - start

# やり方3
start = time.time()
df["fit3"]  = np.polyval(coeff, df['x'])
diff3 = time.time() - start

df["error"] = (df['fit'] - df['y']).abs()
df["rate%"] = (df['error'] / df["y"]) * 100
print(df)
print(diff1)
print(diff2)
print(diff3)

try:
    print(f"length of df: {len(df)}")
    filename_zst = "df.feather.zst"
    filename_raw = "df.feather"

    start = time.time()
    df.to_feather(filename_zst, compression='zstd')
    diff4 = time.time() - start

    start = time.time()
    df.to_feather(filename_raw)
    diff5 = time.time() - start
    print(f"length of df: {len(df)}")

    start = time.time()
    df2 = pd.read_feather(filename_zst)
    diff6 = time.time() - start
    print(df2)
    print(f"length of df2: {len(df2)}")

    start = time.time()
    df2 = pd.read_feather(filename_raw)
    diff7 = time.time() - start
    print(df2)
    print(f"length of df2: {len(df2)}")

    print(f"write  to feather zst {diff4} sec")
    print(f"write  to feather raw {diff5} sec")
    print(f"read from feather zst {diff6} sec")
    print(f"read from feather raw {diff7} sec")

except ImportError:
    print("feature is not supported.")
