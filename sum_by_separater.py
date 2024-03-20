'''
セパレーターの間の合計を求める
'''
import pandas as pd
import numpy as np

# 仮のデータフレームを作成
df = pd.DataFrame([
	{	"name" : "sep",		"seq" : 1,					},
	{	"name" : "test1",	"seq" : 2,	"value" : 1,	},
	{	"name" : "test2",	"seq" : 3,	"value" : 3,	},
	{	"name" : "test3",	"seq" : 4,	"value" : 5,	},

	{	"name" : "sep",		"seq" : 5,					},
	{	"name" : "test1",	"seq" : 6,	"value" : 1,	},
	{	"name" : "test2",	"seq" : 7,	"value" : 3,	},
	{	"name" : "test3",	"seq" : 8,	"value" : 5,	},

	{	"name" : "sep",		"seq" : 9,					},
	{	"name" : "test1",	"seq" : 10,	"value" : 1,	},
	{	"name" : "test2",	"seq" : 11,	"value" : 3,	},
])

# 'name'列の値が'sep'の通算出現回数を計算
df['sep_cumulative_count'] = df[df['name'] == 'sep'].groupby('name').cumcount()

# NaNを前方の値で埋める
df['sep_cumulative_count'].fillna(method='ffill', inplace=True)
print(df)


# 'sep_cumulative_count'列の値が同じ値同士で通算和を求める
df['sum-value'] = df.groupby('sep_cumulative_count')["value"].cumsum()


# 'sep_cumulative_count'列の値の変化点を取り出す
df_border = df[ df['sep_cumulative_count'] != df['sep_cumulative_count'].shift(-1) ]

# 変化点の値のみを設定する
df['sum-value'] = df_border['sum-value']
print(df)
