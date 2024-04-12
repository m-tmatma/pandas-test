import pandas as pd

df1 = pd.read_csv('data1.csv').set_index(['major_id', 'minor_id'])
df2 = pd.read_csv('data2.csv').set_index(['major_id', 'minor_id'])
df3 = pd.read_csv('data3.csv').set_index(['major_id', 'minor_id'])
df4 = pd.read_csv('data4.csv').set_index(['major_id', 'minor_id'])

df = pd.concat([df1, df2], axis=1).reset_index()
print(df)

df = pd.merge(df1, df2)
print(df)

df = pd.concat([df3, df4], axis=1).reset_index()
print(df)

df = pd.merge(df3, df4)
print(df)

df = pd.merge(df4, df3)
print(df)
