#!/usr/bin/python3
#
#
#	Prepare
#		pip install pandas openpyxl
#
import pandas as pd
import datetime

df = pd.DataFrame(
	{
		'timestamp': [ datetime.datetime.now() + datetime.timedelta(microseconds=i*1001*1001) for i in range(10)]
	}
)
df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S.%f')

with pd.ExcelWriter('timestamp-test.xlsx') as writer:
	df.to_excel(writer, sheet_name='Test')
