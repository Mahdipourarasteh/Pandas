#preprocessing

import pandas as pd

df1= pd.DataFrame({'name':['ali','hamid','sadeq','hamed'],
                   'grade':[80,75,63,45],
                   'qualification':['high','mid','low','low']})

df2= pd.DataFrame({'name':['ali','hamid','sadeq','hamed'],
                   'grade':[56,82,73,89],
                   'qualification':['low','high','mid','low']})

df3= pd.DataFrame({'name':['ali','hamid','sadeq'],
                   'grade':[49,72,84],
                   'qualification':['test1','test2','test3']})

#print(pd.merge(df1,df2,on='name'))

# df1.set_index('name',inplace=True)
# df3.set_index('name',inplace=True)
# myjoin= df1.join(df3, lsuffix='_left')
# print(myjoin)

#merged= pd.merge(df1,df2, on='name',how='left')
#merged= pd.merge(df1,df2, on='name',how='inner')
merged= pd.merge(df1,df2, on='name',how='outer')
merged.set_index('name',inplace=True)
print(merged)