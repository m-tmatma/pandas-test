#!/usr/bin/python3

import pandas as pd

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

