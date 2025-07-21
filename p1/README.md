# P1 - Statistical Analysis with NumPy and SciPy

## Description
This project demonstrates basic statistical calculations using Python's NumPy and SciPy libraries.

## Algorithm

### Statistical Measures Calculation
1. **Input Data**: Define a sample dataset `[10, 20, 20, 40, 30, 20, 50]`
2. **Mean Calculation**: Use `np.mean()` to calculate the arithmetic average
3. **Median Calculation**: Use `np.median()` to find the middle value
4. **Mode Calculation**: Use `stats.mode()` with `keepdims=True` to find the most frequent value
5. **Standard Deviation**: Use `np.std()` to measure data spread

### Code Flow
```
1. Import required libraries (numpy, scipy.stats)
2. Define sample data array
3. Calculate statistical measures:
   - Mean: Sum of all values / Number of values
   - Median: Middle value when data is sorted
   - Mode: Most frequently occurring value
   - Standard Deviation: Measure of data dispersion
4. Display results
```

## Libraries Used
- **NumPy**: For numerical operations and statistical calculations
- **SciPy**: For advanced statistical functions (mode calculation)

## Expected Output
```
Mean: 27.14
Median: 20.0
Mode: 20
Standard Deviation: 13.80
```

### Output Screenshot
![Statistical Analysis Results](i1.png)

## Files
- `p1.py`: Main Python script with statistical calculations
- `README.md`: This documentation file

## How to Run
```bash
python p1.py
```

## Learning Objectives
- Understanding basic statistical measures
- Working with NumPy arrays
- Using SciPy for statistical analysis
- Data analysis fundamentals
