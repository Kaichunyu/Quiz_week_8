import matplotlib.pyplot as plt
import pandas as pd

years = []
co2 = []
temp = []

df = pd.read_csv(r"climate.csv")

year_data = df['Year']
co2_data = df['CO2']
temp_data = df['Temperature']

for i in year_data:
    years.append(i)
print(years)

for i in co2_data:
    co2.append(i)
print(co2)

for i in temp_data:
    temp.append(i)
print(temp)


plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

