#!/usr/bin/python3
'''
Test for adding a new DataFrame to an existing DataFrame
'''
import pandas as pd

df = pd.DataFrame(
    {
        'Date': pd.date_range('2020-01-01', periods=10, freq='D'),
    }
)
df['Date'] = pd.to_datetime(df['Date'])

df2 = pd.DataFrame(
    {
        'Date': pd.date_range(df['Date'].max()+pd.offsets.Day(1), periods=10, freq='D'),
    }
)
print(df)
print(df2)
df3 = pd.concat([df, df2], ignore_index=True)
print(df3)
