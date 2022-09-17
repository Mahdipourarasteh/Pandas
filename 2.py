import pandas as pd

data1= pd.Series([16,3,87,14,2],index=['a','b','c','d','f'])
data2= pd.Series([29,45,6,44,78],index=['a','b','c','d','f'])
#print(data1.add(data2))
#print(data1.sub(data2))
#print(data1.mul(data2))
#print(data1.div(data2).round(decimals=2))
#print(data1.pow(data2))
print(data1.pow(data2))