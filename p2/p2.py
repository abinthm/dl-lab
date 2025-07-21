from sklearn.preprocessing import MinMaxScaler  # Import MinMaxScaler for normalization

# Define sample data as a list of lists (2D array)
data = [[20], [40], [60], [80], [100]]

scaler = MinMaxScaler()           # Create a MinMaxScaler object
scaled_data = scaler.fit_transform(data)  # Normalize data to range [0,1]

print("Normalized Data:\n", scaled_data)  # Print the normalized data