from http import server
import numpy as np
import pandas as pd

data= np.array(['t','o','p','l','e','a','r','n'])
myseries= pd.Series(data, index=[10,20,30,40,50,60,70,80])
# print(myseries)
#print(myseries.values)
#print(myseries.index)
print(myseries[3:6])

# data= {'first':'ali', 'second':'majid', 'third':'hosein'}
# #ser= pd.Series(data)
# ser= pd.Series(data,index=['second','first','fifth','third'])
# print(ser)