import pandas as pd
import numpy as np

data= {'name':['ali','hamid',np.nan,'reza'],
       'age':[18,40,23,25],
       'city':['tehran','shiraz','tehran',np.nan],
       'teaching':['pandas','numpy','scipy','matplotlib']}
#df= pd.DataFrame(data)
#print(df)
#df= pd.DataFrame(data,index=[True,False,True,False])
#print(df.loc[True])
#print(df['age']==40)
#print(df['city']=='tehran')
#print(df[df['age']>=25])