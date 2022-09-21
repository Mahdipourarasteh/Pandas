import pandas as pd

df= pd.read_csv('opsd germany daily.csv')
#print(df)
#print(df.info())
#print(df.head())
#print(df.describe())
# print("Average Consumption: ", df['Consumption'].mean())
# print("Standard Deviation in Consumption: ", df['Consumption'].std())
# print("Correlation between Solar and Wind: ", df['Solar'].corr(df['Wind']))
print("Minimum Power Quantity: ", df['Wind+Solar'].min())
print("Maximum Power Quantity: ", df['Wind+Solar'].max())
 
# mode()   var()    cov()   median()   ...