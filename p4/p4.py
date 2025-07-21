from sklearn.metrics import confusion_matrix  # Import confusion matrix function

y_true = [0, 1, 0, 1, 0, 1]  # Actual class labels
y_pred = [0, 0, 0, 1, 0, 1]  # Predicted class labels by model

cm = confusion_matrix(y_true, y_pred)  # Create the confusion matrix

print("Confusion Matrix:")  # Print heading
print(cm)  # Show matrix (TP, FP, FN, TN)