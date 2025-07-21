import numpy as np                      # For numerical operations
from scipy import stats                 # For statistical calculations

data = [10, 20, 20, 40, 30, 20, 50]     # Sample data list

mean = np.mean(data)                   # Calculate the mean
median = np.median(data)               # Calculate the median
mode = stats.mode(data, keepdims=True) # Compute mode (keepdims=True prevents scalar issue)
std_dev = np.std(data)                 # Compute standard deviation

print("Mean:", mean)                   # Print mean value
print("Median:", median)               # Print median value
print("Mode:", mode.mode[0])           # Print the mode correctly (now it's an array)
print("Standard Deviation:", std_dev)  # Print standard deviation