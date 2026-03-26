import matplotlib.pyplot as plt
print("Choose Visualization Type:")
print("1. Line Chart")
print("2. Bar Chart")
print("3. Pie Chart")

choice = int(input("Enter your choice (1/2/3): "))

n = int(input("Enter number of data points: "))
labels = []
values = []

for i in range(n):
    label = input(f"Enter label {i+1}: ")
    value = float(input(f"Enter value for {label}: "))
    
    labels.append(label)
    values.append(value)

# LINE CHART
if choice == 1:
    plt.plot(labels, values, marker='o')
    plt.title("Line Chart")
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.grid(True)
    plt.show()

# BAR CHART
elif choice == 2:
    plt.bar(labels, values)
    plt.title("Bar Chart")
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.show()

# PIE CHART
elif choice == 3:
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Pie Chart")
    plt.axis('equal')
    plt.show()

else:
    print("Invalid choice!")
