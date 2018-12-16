import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
url_template = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"
url = url_template.format(month=3,year=2012)
#print(url)
weather_mar2012 = pd.read_csv(url, skiprows=15, index_col='Date/Time', parse_dates=True, encoding='latin1')
weather_report = weather_mar2012['Weather']
#print(weather_report)
is_snowing = weather_report.str.contains('Snow')
#print(is_snowing)
plt.interactive(True)
plt.show()
#is_snowing.astype(float).plot()
temp = weather_mar2012['Temp (\xc2\xb0C)'].resample('M', how=np.median)
temp.plot(kind='bar')
print(is_snowing.astype(float)[:10])
snowing_median = is_snowing.astype(float).resample('M', how=np.mean)
print(snowing_median)
snowing_median.plot(kind='bar')
temp.name = "Temperature"
snowing_median.name = "Snowiness"
stats = pd.concat([temperature, snowiness], axis=1)
stats.plot(kind='bar')
stats.plot(kind='bar', subplots=True, figsize=(15, 10))#show 2 plots one with temp and snowiness
