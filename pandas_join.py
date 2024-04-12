import pandas as pd

df1 = pd.read_csv('data1.csv').set_index(['major_id', 'minor_id'])
df2 = pd.read_csv('data2.csv').set_index(['major_id', 'minor_id'])

df = pd.concat([df1, df2], axis=1).reset_index()
print(df)

df = pd.merge(df1, df2)
print(df)
