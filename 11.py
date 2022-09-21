from email.headerregistry import Group
import pandas as pd
import numpy as np

df= pd.read_csv('file.csv')
#print(df)

mygp= df.groupby('Name')
#print(mygp.groups)

# def myfunc(self):
#     return df.loc[self].Test1 > df.loc[self].Test2

# print(df.groupby(myfunc).groups)

# print(mygp['Test3'].agg(np.mean))

# for Name, group in mygp:
#     print('Name')
#     print(group)

#print(mygp.get_group('Ali'))

df1= pd.DataFrame({'name':['ali','hamid','sadeq'],
                   'grade':[80,75,63],
                   'qualification':['high','mid','low']})

df2= pd.DataFrame({'name':['ali','hamid','sadeq'],
                   'grade':[56,82,73],
                   'qualification':['low','high','mid']})

print(pd.concat([df1,df2]))