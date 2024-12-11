# 2D Numpy Arrays

# Import the NumPy library
import numpy as np

# 1D NumPy arrays
np_height = np.array([1.75, 1.45, 1.90, 1.67, 1.68])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

# Check the type of the arrays
print("Type of np_height:", type(np_height))
print("Type of np_weight:", type(np_weight))

# Creating a 2D NumPy array
np_2d = np.array([
    [1.75, 1.45, 1.90, 1.67, 1.68],
    [65.4, 59.2, 63.6, 88.4, 68.7]
])
print("2D Array:\n", np_2d)

# Shape of the 2D array
print("Shape of np_2d:", np_2d.shape)

# Subsetting 2D arrays
# Accessing a specific element
print("Element at row 0, column 2:", np_2d[0, 2])

# Slicing: Second and third columns
print("Second and third columns:\n", np_2d[:, 1:3])

# Accessing the second row
print("Second row:", np_2d[1, :])

# Example with baseball data
baseball = [
    [180, 78.4],
    [215, 102.7],
    [210, 98.5],
    [188, 75.2]
]

# Create a 2D NumPy array from baseball
np_baseball = np.array(baseball)
print("Baseball 2D Array:\n", np_baseball)

# Type and shape of np_baseball
print("Type of np_baseball:", type(np_baseball))
print("Shape of np_baseball:", np_baseball.shape)

# Subsetting and slicing np_baseball
# Select the entire second column
np_weight_lb = np_baseball[:, 1]
print("Weights (lbs):", np_weight_lb)

# Access height of a specific player (error example for out-of-bounds index)
try:
    print("Height of 124th player:", np_baseball[123, 0])
except IndexError:
    print("Error: np_baseball does not have 124 rows.")

# Accessing the first column (heights)
print("Heights (first column):", np_baseball[:, 0])

# Attempting to access the 50th row (error example for out-of-bounds index)
try:
    print("50th row of np_baseball:", np_baseball[49, :])
except IndexError:
    print("Error: np_baseball does not have 50 rows.")