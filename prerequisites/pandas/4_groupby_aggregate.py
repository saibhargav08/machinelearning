import pandas as pd
import matplotlib.pyplot as plt
url = 'http://donnees.ville.montreal.qc.ca/dataset/f170fecc-18db-44bc-b4fe-5b0b6d2c7297/resource/d54cec49-349e-47af-b152-7740056d7311/download/comptagevelo2012.csv'
bikes = pd.read_csv(url, sep=',', parse_dates={'datetime':[0, 1]}, index_col='datetime')
berri_bikes = bikes[['Berri1']].copy()#this makes a copy of the pandas dataframe which is similar to deepcopy
print(berri_bikes)
#print(berri_bikes.index)#returns datetime as the default indexing is datetime
#print(berri_bikes.index.day)
#print(berri_bikes.index.weekday)
berri_bikes.loc[:,'weekday'] = berri_bikes.index.weekday#adding a new column to the dataframe with its value
#print(berri_bikes)
x =berri_bikes.groupby('weekday')
#print(x.groups)# to get group by data
weekday_counts = x.aggregate(sum)#Group the rows by weekday and then add up all the values with the same weekday
print(weekday_counts)
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']#to make the represenation of 0-6 
plt.interactive(True)
plt.show()
weekday_counts.plot(kind='bar')
print (weekday_counts)