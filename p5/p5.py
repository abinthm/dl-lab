from sklearn.metrics import accuracy_score  # Import accuracy function

y_true = [1, 0, 1, 1, 0, 1]  # Actual class values
y_pred = [1, 0, 0, 1, 0, 1]  # Predicted class values

accuracy = accuracy_score(y_true, y_pred)  # Calculate ratio of correct predictions

print("Accuracy:", accuracy)  # Output accuracy value
