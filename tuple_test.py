#!/usr/bin/python3
'''
tuple column name test and styleframe
'''
# gh-20: tuple_test.py

import pandas as pd
from styleframe import StyleFrame

df = pd.DataFrame([
    {
        ("data", "name"): "a",
        "value": 1,
    },
    {
        ("data", "name"): "b",
        "value": 2,
    },
    {
        ("data", "name"): "c",
        "value": 3,
    },
    {
        ("data", "name"): "d",
        "value": 4,
    },
    {
        ("data", "name"): "e",
        "value": 5,
    },
])
print(df)

with StyleFrame.ExcelWriter("tuple_test.xlsx") as writer:
    sf = StyleFrame(df)
    sf.to_excel(writer, index=False)
