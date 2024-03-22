#!/usr/bin/python3
# gh-20: tuple_test.py

import pandas as pd
import openpyxl

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

df.to_excel("tuple_test.xlsx", index=False)
