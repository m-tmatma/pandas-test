import numpy as np
import pandas as pd

state = np.random.randint(3, size=100)
x     = np.arange(100)
y     = np.arange(100,200)

df = pd.DataFrame( {'x' : x, 'y' : y, 'state': state })

states = df['state']

df['change'] = states != states.shift(-1)
dfChange = df[ df['change'] ]
dfdiff_dfChange = dfChange.diff(-1)

df['duration'] = dfdiff_dfChange['x'].abs()
#dfChange['duration'] = dfdiff_dfChange['x'].abs()

df.to_csv("df.csv")
#dfChange.to_csv("dfChange.csv")
