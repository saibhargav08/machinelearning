import pandas as pd
import matplotlib.pyplot as plt
url_template = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"
url = url_template.format(month=3, year=2012)
print(url)
weather_mar2012 = pd.read_csv(url, skiprows=15, index_col='Date/Time', parse_dates=True, encoding='latin1')
print(weather_mar2012)
plt.interactive(True)
plt.show()
#print(weather_mar2012[u"Temp (\xc2\xb0C)"].plot(figsize=(15, 5)))
print(weather_mar2012.columns)
weather_data.columns = [col.replace('\xb0', '') for col in weather_data.columns]

#axis can be "columns", if axis not specified it will drop rows with atleast one element missing
# only how='all' drop rows where all the elements are missing
#thresh= integer meaning atleast integer non-NA values
#subset=[listof columns] look where missing values
#inplace keep dataframe with valid entries in the same values
weather_mar2012_d = weather_mar2012.dropna(axis=1, how='any')#The argument axis=1 to dropna means "drop columns", not rows", and how='any' means "drop the column if any value is null".
print(weather_mar2012_d)
weather_mar2012_dd = weather_mar2012_d.drop(['Year', 'Month', 'Day', 'Time'], axis=1)
print(weather_mar2012_dd)
temperatures = weather_mar2012[[u'Temp (C)']].copy()
print(temperatures.head)
temperatures.loc[:,'Hour'] = weather_mar2012.index.hour
temperatures.groupby('Hour').aggregate(np.median).plot()
data_by_month = [download_weather_month(2012, i) for i in range(1, 13)]
weather_2012 = pd.concat(data_by_month)
weather_2012.to_csv('../data/weather_2012.csv')

