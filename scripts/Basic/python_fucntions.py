# Functions
# Functions aren't entirely new for you actually: you've already used them. 
# `type`, for example, is a function that returns the type of a value. 
# A function is a piece of reusable code, aimed at solving a particular task.

# Suppose you have the list containing only the heights of your family, `fam`: 
# Say that you want to get the maximum value in this list.
# Instead of writing your own piece of Python code, you can use Python's `max` function.

# Create a list of family heights
fam = [1.73, 1.68, 1.71, 1.89]

# Print the family list
print("Family heights:", fam)

# Find the tallest member using max()
tallest = max(fam)
print("Tallest height:", tallest)

# Another built-in function is `round`, which rounds numbers to a specified precision.
# Round 1.68 to one decimal place
rounded_value = round(1.68, 1)
print("1.68 rounded to one decimal place:", rounded_value)

# Round 1.68 to the nearest integer
rounded_integer = round(1.68)
print("1.68 rounded to the nearest integer:", rounded_integer)

# Familiar Functions
# Examples of built-in functions: print(), type(), str(), int(), bool(), float()

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out the type of var1
print("Type of var1:", type(var1))

# Print out the length of var1
print("Length of var1:", len(var1))

# Convert var2 to an integer
out2 = int(var2)
print("Integer conversion of var2:", out2)

# Help!
# The `help()` function provides information about Python functions.
# Example: Get help on the `pow` function
print("\nHelp on pow function:")
help(pow)

# Multiple arguments
# Use `sorted()` with reverse argument

# Create two lists
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Merge the lists
full = first + second
print("Merged list:", full)

# Sort the merged list in descending order
full_sorted = sorted(full, reverse=True)
print("Sorted in descending order:", full_sorted)