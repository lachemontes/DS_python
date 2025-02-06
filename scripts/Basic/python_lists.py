# Python Lists

"""
On the numbers side, there's the `float`, to represent a real number, 
and the `int`, to represent an integer. 
Next, we also have `str`, short for string, to represent text in Python, 
and `bool`, which can be either True or False.
"""

"""
Example of a Python list with different types:
"""

# Example
fam = ["Sam", 1.78, "Carl", 1.73, "Peter", 1.55, "Ana", 1.80]

# List of lists
fam2 = [
    ["Sam", 1.78],
    ["Carl", 1.73],
    ["Peter", 1.55],
    ["Ana", 1.80]
]

# Checking type
print(type(fam))

"""
Create a list for areas
"""
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)

# Creating a mixed list
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

# List of lists example
house = [
    ["hallway", hall],
    ["kitchen", kit],
    ["living room", liv],
    ["bedroom", bed],
    ["bathroom", bath]
]

# Print house
print(house)

"""
Subsetting and slicing
"""
fam2 = ["Liz", 1.73, "emma", 1.68, "mom", 1.72, "dad", 1.89]

# Access specific elements
print(fam2[3])  # emma's height
print(fam2[-1])  # dad's height

# Slicing
print(fam2[1:4])  # Slice of family heights
print(fam2[:4])   # All up to index 4

# Subsetting lists of lists
print(house[-1][1])  # Subset the float 9.50