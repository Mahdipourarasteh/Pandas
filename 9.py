import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv')
df.dropna(axis=0)
print(df)
print(df.describe())

df['Value'].plot(title='title',xlabel='Index', ylabel='Value')
plt.show()