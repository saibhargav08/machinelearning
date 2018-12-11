import pandas as pd
import matplotlib.pyplot as plt

# Make the graphs a bit prettier, and bigger
 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)

plt.rcParams['figure.figsize'] = (15, 5)
url = 'https://data.cityofnewyork.us/resource/fhrw-4uyv.csv'
complaints = pd.read_csv(url)
print(complaints)
print(complaints['complaint_type'])#selecting a column
print(complaints[:5])#first 5 rows
print(complaints[:5]['complaint_type'])#five rows of a column (complaints['complaint_type'][:5] gives same value
print(complaints[['complaint_type','borough']])#If we want to select multiple columns
print(complaints[['complaint_type','borough']][:10])#multiple columns of first 10 rows
complaint_counts = complaints['complaint_type'].value_counts()# to get the most commonly values of a column
print(complaint_counts[:10])#top 10 values
plt.interactive(True)
plt.show()
print(complaint_counts[:10].plot(kind='bar'))#plot with bar chart