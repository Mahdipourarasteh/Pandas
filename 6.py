import pandas as pd
import numpy as np

data= {'name':['ali','hamid',np.nan,'reza'],
       'age':[18,40,23,25],
       'city':['tehran','shiraz','tehran',np.nan],
       'teaching':['pandas','numpy',np.nan,'matplotlib']}
df= pd.DataFrame(data)
print(df)
#print(df.isnull())
#print(df[df.notnull()])
#print(df.fillna('-'))
#print(df.dropna())
print(df.dropna(axis=1))   #axis=1 vertical /  axis=0  Horizantal