import sqlite3

years = []
co2 = []
temp = []

connection = sqlite3.connect(r"climate.db")
cursor = connection.cursor()
sql_cmd = """
SELECT * FROM ClimateData;
"""
cursor.execute(sql_cmd)

result = cursor.fetchall() # Return all (remaining) rows of a query result as a list.
for r in result:
    years.append(r[0])
    co2.append(r[1])
    temp.append(r[2])

print(f"years: {years}")
print(f"co2: {co2}")
print(f"temp: {temp}")


import matplotlib.pyplot as plt
        

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
plt.savefig("co2_temp_1.png") 
