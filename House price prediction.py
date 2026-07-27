import numpy as np
import matplotlib.pyplot as plt
X=np.array([500,750,1000,1250,1500,1750,2000,2250,2500,2750,3000])
Y=np.array([100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600])
mean_x=np.mean(X)
mean_y=np.mean(Y)
num =np.sum((X-mean_x)*(Y-mean_y))
den=np.sum(np.square(X-mean_x))
slope=num/den
intercept=mean_y-(slope*mean_x)
print(f"Slope(m):{slope:.2f}")
print(f"Intercept (b): {intercept:.2f}")
print(f"Equation: price={slope:.2f} * size +{intercept:.2f}")
y_pred=slope*X+intercept
try:
  size_input=float(input("Enter the house size in square feet: "))
  pred_price=slope*size_input + intercept
  print(f"Predicted house price: ${pred_price:.2f}")
except ValueError:
  print("Invalid input. Please enter a valid number.")
plt.scatter(X,Y,c="r",label="Training Data")
plt.plot(X,y_pred,"b",label="Regression Line")
plt.xlabel("House Size (spft)")
plt.ylabel("House Price in rupees")
plt.title("House Price Prediction")
plt.legend()
plt.grid(True)
plt.show()
