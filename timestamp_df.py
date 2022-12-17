#!/usr/bin/python3
"""
This script demonstrates writing dataframe to excel.

Prepare
   pip install pandas openpyxl numpy

See
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.ExcelWriter.html
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.ExcelWriter.sheets.html
* https://towardsdatascience.com/how-to-auto-adjust-the-width-of-excel-columns-with-pandas-excelwriter-60cee36e175e
"""
import datetime
import pandas as pd
import numpy as np

def timedata(i):
    '''
    return test data.
    '''
    return datetime.datetime.now() + datetime.timedelta(microseconds=i*1001*1001)

df = pd.DataFrame(
    {
        'timestamp': [ timedata(i) for i in range(10)],
        'random': np.random.random(10),
    }
)
df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S.%f')

with pd.ExcelWriter('timestamp-test.xlsx') as writer:
    sheet_name='Test'
    df.to_excel(writer, sheet_name=sheet_name, index=False)

    for column in df:
        column_width = max(df[column].astype(str).map(len).max(), len(column))
        col_idx = df.columns.get_loc(column)
        writer.sheets[sheet_name].set_column(col_idx, col_idx, column_width)
