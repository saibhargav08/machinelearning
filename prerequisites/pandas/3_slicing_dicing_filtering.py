import pandas as pd
import matplotlib.pyplot as plt
url = 'https://data.cityofnewyork.us/resource/fhrw-4uyv.csv'
complaints = pd.read_csv(url)
noise_complaints = complaints[complaints['complaint_type'] == "Noise - Street/Sidewalk"]#to get noise type complaints
print(noise_complaints)
print(noise_complaints[:3])
print(complaints['complaint_type'] == "Noise - Street/Sidewalk")#check every complaint type is of noise type this will return a big array of boolean values
is_noise = complaints['complaint_type'] == "Noise - Street/Sidewalk"
in_brooklyn = complaints['borough'] == "BROOKLYN"
print(complaints[is_noise & in_brooklyn])#both noise type complaint and in brooklyn with all the columns
print(complaints[is_noise & in_brooklyn][['complaint_type', 'borough', 'created_date', 'descriptor']])#select specific columns
noise_complaints = complaints[is_noise]
print(noise_complaints['borough'].value_counts())
noise_complaint_count = noise_complaints['borough'].value_counts()
complaint_counts = complaints['borough'].value_counts()
print(noise_complaint_count/complaint_counts.astype(float))#to make result not zero
plt.show()
plt.interative(True)
noise_complaint_count/complaint_counts.astype(float).plot(kind='bar')