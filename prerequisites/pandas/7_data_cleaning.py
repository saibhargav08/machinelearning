import pandas as pd
import matplotlib.pyplot as plt
na_values = ['NO CLUE', 'N/A', '0']
url = 'https://data.cityofnewyork.us/resource/fhrw-4uyv.csv'
requests = pd.read_csv(url, na_values=na_values, dtype={'incident_zip':str})
#print(requests.columns)
print(requests['incident_zip'].unique())
rows_with_dashes = requests['incident_zip'].str.contains('-').fillna(False)
print(len(rows_with_dashes))
#basically we use unique to get the all the values in the column if it is a numeric column generally use a histogram