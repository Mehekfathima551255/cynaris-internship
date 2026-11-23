
import numpy as np
import pandas as pd

# 1. Create 1D, 2D and 3D arrays
arr_1d = np.array([10, 20, 30, 40])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("1D Shape:", arr_1d.shape)
print("2D Shape:", arr_2d.shape)
print("3D Shape:", arr_3d.shape)

# 2. Broadcasting
numbers = np.array([10, 20, 30])
print("Broadcasting:", numbers + 5)

# 3. Vectorised operations
print("Multiplication:", numbers * 2)

# 4. Matrix multiplication
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

print("Matrix Multiplication:")
print(np.matmul(matrix_a, matrix_b))


# 5. Load real CSV dataset using Pandas
df = pd.read_csv("student_scores.csv")

# Convert columns into NumPy arrays
math_scores = df["Math_Score"].to_numpy()
science_scores = df["Science_Score"].to_numpy()

# 6. Calculate statistics
print("\n--- Statistical Analysis ---")

print("Mean:", np.mean(math_scores))
print("Standard Deviation:", np.std(math_scores))

# 7. Calculate correlation
correlation = np.corrcoef(math_scores, science_scores)

print("Correlation:")
print(correlation)
