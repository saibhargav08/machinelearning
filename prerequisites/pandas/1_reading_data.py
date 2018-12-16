#read_csv other options sep, encoding,dayfirst(DD/MM) format, parse_dates, index_col
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
url = 'http://donnees.ville.montreal.qc.ca/dataset/f170fecc-18db-44bc-b4fe-5b0b6d2c7297/resource/d54cec49-349e-47af-b152-7740056d7311/download/comptagevelo2012.csv'
broken_df = pd.read_csv(url)#'http://donnees.ville.montreal.qc.ca/dataset/f170fecc-18db-44bc-b4fe-5b0b6d2c7297/resource/d54cec49-349e-47af-b152-7740056d7311/download/comptagevelo2012.csv')
print(broken_df[:3])# first 3 rows
#fixed_df = pd.read_csv(url, sep=';', encoding='latin1', parse_dates=["Date"], dayfirst=True, index_col=['Date'])
#this did not work as the file is a comma separator and the encoding is utf-8 default and there is a unnamed column for time so parsing date fails
fixed_df = pd.read_csv(url, sep=',', parse_dates={'datetime':[0, 1]}, index_col='datetime')
print(fixed_df)
print(fixed_df['Berri1'])#for selecting a column
#the below 2 lines are for wingware to show the plot
plt.interactive(True)
plt.show()
print (fixed_df['Berri1'].plot())#plot a column
print(fixed_df.plot(figsize=(15, 10)))#plot the entire data