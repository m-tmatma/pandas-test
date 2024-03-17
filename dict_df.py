#!/usr/bin/python3
import pandas as pd

data = [
    {"name": "x", "value": "x"},
    {"name": "y", "value": "y"},
    {"name": "state", "value": "state"},
    {"name": "change", "value": "change"},
    {"name": "duration", "value": "duration"}
]

df = pd.DataFrame(data)
print(df)


