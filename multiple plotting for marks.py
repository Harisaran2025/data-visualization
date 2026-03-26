import matplotlib.pyplot as plt
x = input("Enter subjects separated by comma:  ").split(",")
y = list(map(int, input("Enter marks separated by comma:").split(",")))
plt.figure(figsize=(10,8))

plt.subplot(3,2,1)
plt.plot(x,y)
plt.title("Line Plot")

plt.subplot(3,2,2)
plt.bar(x,y)
plt.title("Bar Chart")

plt.subplot(3,2,3)
plt.scatter(x,y)
plt.title("Scatter Plot")

plt.subplot(3,2,4)
plt.hist(y)
plt.title("Histogram")

plt.subplot(3,2,5)
plt.pie(y,labels=x,autopct='%1.1f%%')
plt.title("Pie Chart")

plt.tight_layout()
plt.show()
