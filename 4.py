import pandas as pd

# mylist= ['tp','pandas','ttl']
# df= pd. DataFrame(mylist, index=['first','second','third'],columns=['text'])
# print(df)

data= {'name':['Ali','Reza','Hosein'],'age':[25,36,18],'city':['Tehran','Isfahan','Shiraz'],'email':['test1','test2','test3']}
df= pd.DataFrame(data, index=['person1','person2','person3'])
#print(df[['name','city']])
#print(df)
#print(df.loc['person2'])
#print(df.loc[['person2']])
#print(df.iloc[[1]])
#print(df.loc[['person2','person3']])
#print(df.loc['person1':'person2'])
#print(df.iloc[0:2])
#print(df.iloc[0:2,1:2])
print(df.loc['person1':'person2','age':'email'])