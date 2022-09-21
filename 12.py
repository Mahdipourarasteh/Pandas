import pandas as pd

#print(pd.to_datetime('2019-05-15 3:45pm'))
#print(type(pd.to_datetime('2019-05-15 3:45pm')))

# print(pd.to_datetime(['2019-05-15', '7/8/2010', 'oct 10, 1999']))
# print(pd.to_datetime('2/25/10', format= '%m/%d/%y'))

#################################################################################
opsd_daily= pd.read_csv('opsd germany daily.csv')
#print(opsd_daily.shape)
#print(opsd_daily.head())

#print(opsd_daily.dtypes)

# opsd_daily= opsd_daily.set_index('Date')
opsd_daily= opsd_daily.set_index(pd.DatetimeIndex(opsd_daily['Date']))
#print(opsd_daily.tail())
#print(opsd_daily.index)
#print(opsd_daily.loc['2017-08-10'])
#print(opsd_daily.loc['2017-08-10' : '2017-08-20'])
print(opsd_daily.loc['2017-08'])