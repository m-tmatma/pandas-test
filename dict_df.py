#!/usr/bin/python3
'''
sample code for creating a dataframe from a dictionary
'''
import pandas as pd

data = [
    {"name": "x", "value": "x"},
    {"name": "y", "value": "y"},
    {"name": "state", "value": "state"},
    {"name": "change", "value": "change"},
    {"name": "duration", "value": "duration"},
    {"test": "test3", "value": "test4"},
    {"hoge": "test3", "hoge2": "test4"},
]

df = pd.DataFrame(data)
print(df)
