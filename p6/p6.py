import numpy as np                          # Import numpy for numerical operations
import matplotlib.pyplot as plt             # Import matplotlib for plotting
from sklearn.linear_model import LinearRegression  # Import linear regression model

# Generate synthetic input data (features)
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)  # Reshape required for sklearn
y = np.array([2, 4, 5, 4, 5, 6])                # Target/output values

model = LinearRegression()              # Create a LinearRegression model
model.fit(X, y)                         # Train the model using the synthetic data

y_pred = model.predict(X)              # Predict output for input X using the trained model

# Print model parameters
print("Slope (m):", model.coef_[0])     # Coefficient of the line (slope)
print("Intercept (c):", model.intercept_)  # Intercept of the line

# Visualization
plt.scatter(X, y, color='blue', label="Actual Data")  # Scatter plot of original data
plt.plot(X, y_pred, color='red', label="Fitted Line") # Plot the regression line
plt.xlabel('X')                          # Label x-axis
plt.ylabel('y')                          # Label y-axis
plt.title('Simple Linear Regression')    # Title of the plot
plt.legend()                             # Show legend
plt.grid(True)                           # Add grid to plot
plt.savefig('linear_regression_output.png', dpi=300, bbox_inches='tight')  # Save the plot
plt.show()                               # Display the plot