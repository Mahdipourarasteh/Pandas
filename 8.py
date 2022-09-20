import pandas as pd

df= pd.read_csv('username.csv')
#   read_excel   ,  read_html
#   excellFileParse()
#   to_csv()

print(df)
#print(df.head(2))
#print(df.tail(2))
#print(df.shape)
#print(df.count())
#print(df.values)
#print(type(df.values))
#print(df.describe())
#print(df.set_index('Username'))
print(df.sort_values('First name',axis=0,inplace=False,ascending=True,na_position='last'))