#!/usr/bin/python3

import pandas as pd
from styleframe import StyleFrame

x     = [1, 2, 3, 4, 5]
y     = [6, 7, 8, 9, 10]

df = pd.DataFrame( {'very very very long x' : x, 'very very very long y' : y})
print(df)

with StyleFrame.ExcelWriter("styleframe.xlsx") as writer:
    sf = StyleFrame(df)
    sf.to_excel(writer, index=False)
