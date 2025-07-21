# P4 - Confusion Matrix for Classification Evaluation

## Description
This project demonstrates the creation and interpretation of a confusion matrix using scikit-learn. A confusion matrix is a fundamental tool for evaluating the performance of classification models by showing the relationship between actual and predicted class labels.

## Algorithm

### Confusion Matrix Generation Process
1. **Data Preparation**: Define actual and predicted class labels
   - `y_true = [0, 1, 0, 1, 0, 1]` (actual labels)
   - `y_pred = [0, 0, 0, 1, 0, 1]` (predicted labels)
2. **Matrix Creation**: Use `confusion_matrix()` function from scikit-learn
3. **Analysis**: Display the resulting 2x2 matrix showing classification results

### Mathematical Background
A confusion matrix for binary classification contains four components:
- **True Positives (TP)**: Correctly predicted positive cases
- **True Negatives (TN)**: Correctly predicted negative cases
- **False Positives (FP)**: Incorrectly predicted as positive (Type I error)
- **False Negatives (FN)**: Incorrectly predicted as negative (Type II error)

### Matrix Structure
```
                Predicted
                0    1
Actual    0   [TN] [FP]
          1   [FN] [TP]
```

### Code Flow
```
1. Import confusion_matrix from sklearn.metrics
2. Define y_true (actual class labels)
3. Define y_pred (predicted class labels)
4. Create confusion matrix using confusion_matrix(y_true, y_pred)
5. Display the resulting matrix
```

## Libraries Used
- **scikit-learn**: For confusion matrix computation and metrics

## Expected Output
For the given data:
- `y_true = [0, 1, 0, 1, 0, 1]`
- `y_pred = [0, 0, 0, 1, 0, 1]`

```
Confusion Matrix:
[[3 0]
 [1 2]]
```

### Matrix Interpretation:
- **[3, 0]**: 3 True Negatives (0→0), 0 False Positives (0→1)
- **[1, 2]**: 1 False Negative (1→0), 2 True Positives (1→1)

## Performance Metrics Derivable
From the confusion matrix, we can calculate:
- **Accuracy**: (TP + TN) / (TP + TN + FP + FN) = (2 + 3) / 6 = 83.33%
- **Precision**: TP / (TP + FP) = 2 / (2 + 0) = 100%
- **Recall (Sensitivity)**: TP / (TP + FN) = 2 / (2 + 1) = 66.67%
- **Specificity**: TN / (TN + FP) = 3 / (3 + 0) = 100%

## Why Confusion Matrix?
- **Detailed Analysis**: Shows exactly where the model makes mistakes
- **Class-wise Performance**: Reveals performance for each class separately
- **Metric Foundation**: Base for calculating various performance metrics
- **Model Comparison**: Enables comparison between different models
- **Bias Detection**: Helps identify if model is biased toward certain classes

## Use Cases
- Binary classification evaluation
- Multi-class classification analysis
- Medical diagnosis accuracy assessment
- Model performance comparison
- Error pattern identification

## Files
- `p4.py`: Main Python script for confusion matrix generation
- `i4.png`: Visualization of the confusion matrix
- `README.md`: This documentation file

## How to Run
```bash
cd p4
python p4.py
```

## Learning Objectives
- Understanding confusion matrix concepts
- Evaluating classification model performance
- Interpreting True/False Positives and Negatives
- Foundation for advanced evaluation metrics
- scikit-learn metrics module usage
