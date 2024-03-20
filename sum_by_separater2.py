'''
セパレーターの間の合計を求める
'''
import pandas as pd

# 仮のデータフレームを作成
df = pd.DataFrame([
    {   "type" : "sep",                         "seq" :  1,                 },
    {   "type" : "data",    "name" : "test1",   "seq" :  2, "value" : 1,    },
    {   "type" : "data",    "name" : "test2",   "seq" :  3, "value" : 3,    },
    {   "type" : "data",    "name" : "test3",   "seq" :  4, "value" : 5,    },
    {   "type" : "other",   "name" : "test3",   "seq" :  5, "value" : 5,    },

    {   "type" : "sep",                         "seq" :  6,                 },
    {   "type" : "data",    "name" : "test1",   "seq" :  7, "value" : 1,    },
    {   "type" : "data",    "name" : "test2",   "seq" :  8, "value" : 3,    },
    {   "type" : "data",    "name" : "test3",   "seq" :  9, "value" : 5,    },
    {   "type" : "other",   "name" : "test3",   "seq" : 10, "value" : 5,    },

    {   "type" : "sep",                         "seq" : 11,                 },
    {   "type" : "data",    "name" : "test1",   "seq" : 12, "value" : 1,    },
    {   "type" : "data",    "name" : "test2",   "seq" : 13, "value" : 3,    },
    {   "type" : "other",   "name" : "test3",   "seq" : 14, "value" : 5,    },
])

unique_values = df['name'].unique()
for value in unique_values:
    df.loc[df['name'] == value, f'seq-{value}'] = df['value']

for value in unique_values:
    df[f'seq-{value}'].fillna(method='ffill', inplace=True)

print(df)

df['sum-value'] = df.filter(like='seq-').sum(axis=1)
df2 = df[ df['type'].isin(['sep', 'data']) ]
df2 = df2[ df2.shift(-1)['type'] == 'sep' ]
print(df2)
