import numpy as np

# 1D Arrays Example
np_height = np.array([1.75, 1.45, 1.90, 1.67, 1.68])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
print("Type of np_height:", type(np_height))
print("Type of np_weight:", type(np_weight))

# 2D Array Example
np_2d = np.array([[1.75, 1.45, 1.90, 1.67, 1.68], [65.4, 59.2, 63.6, 88.4, 68.7]])
print("2D Array:\n", np_2d)
print("Shape of np_2d:", np_2d.shape)
print("Subsetting: np_2d[0][2] =", np_2d[0][2])
print("Subsetting: np_2d[:, 1:3] =\n", np_2d[:, 1:3])
print("Second row:", np_2d[1, :])

# Baseball Data
baseball = [[180, 78.4], [215, 102.7], [210, 98.5], [188, 75.2]]
np_baseball = np.array(baseball)
print("Type of np_baseball:", type(np_baseball))
print("Shape of np_baseball:", np_baseball.shape)

# Subsetting np_baseball
print("First column of np_baseball:", np_baseball[:, 0])
try:
    print("50th row of np_baseball:", np_baseball[49, :])
except IndexError:
    print("IndexError: np_baseball does not have a 50th row.")
try:
    print("Height of 124th player:", np_baseball[123, 0])
except IndexError:
    print("IndexError: np_baseball does not have a 124th row.")

# Arithmetic with np_baseball
updated = np.array([[1, 2], [2, 1], [3, 2], [4, 3]])
print("Addition of np_baseball and updated:\n", np_baseball + updated)
conversion = np.array([0.0254, 0.453592])
print("Converted np_baseball to metric:\n", np_baseball * conversion)