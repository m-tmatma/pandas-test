import pandas as pd

df1 = pd.read_csv('data1.csv').set_index(['major_id', 'minor_id'])
df2 = pd.read_csv('data2.csv').set_index(['major_id', 'minor_id'])
df3 = pd.read_csv('data3.csv').set_index(['major_id', 'minor_id'])
df4 = pd.read_csv('data4.csv').set_index(['major_id', 'minor_id'])

print("concat[df1, df2]")
df = pd.concat([df1, df2], axis=1).reset_index()
print(df)

print("merge(df1, df2)")
df = pd.merge(df1, df2)
print(df)

print("merge(df3, df4)")
df = pd.concat([df3, df4], axis=1).reset_index()
print(df)
df_nan = df[df.isnull().any(axis=1)]
print("df_nan")
print(df_nan)

print("merge(df3, df4)")
df = pd.merge(df3, df4)
print(df)

print("merge(df4, df3)")
df = pd.merge(df4, df3)
print(df)
