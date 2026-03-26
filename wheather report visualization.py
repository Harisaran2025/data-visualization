import matplotlib.pyplot as plt
n = int(input("Enter number of days: "))
days = []
temps = []
for i in range(n):
    day = input(f"Enter day {i+1} (e.g., Mon, Tue): ")
    temp = float(input(f"Enter temperature for {day}: "))
    days.append(day)
    temps.append(temp)
max_temp = max(temps)
min_temp = min(temps)

max_day = days[temps.index(max_temp)]
min_day = days[temps.index(min_temp)]

plt.figure(figsize=(10,6))
plt.plot(days, temps, marker='o', linestyle='-', label="Temperature")
plt.scatter(max_day, max_temp, color='red', s=120, label=f"Hottest ({max_temp}°C)")
plt.scatter(min_day, min_temp, color='blue', s=120, label=f"Coldest ({min_temp}°C)")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Weather Data Visualization")
plt.grid(True)
plt.legend()
plt.show()
