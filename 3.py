import numpy as np
import pandas as pd

data= np.array(['t','o','p','l','e','a','r','n'])
myseries= pd.Series(data,index=[5,10,15,20,25,30,35,40])

#print(myseries)
#print(myseries.iloc[3:6])
print(myseries.loc[20:35])  ##with index 35