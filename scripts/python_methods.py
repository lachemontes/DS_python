# Methods

# You already know about functions such as max, to get the maximum of a list,
# len, to get the length of a list or a string, and so on.
# But what about other basic things, such getting the index of a specific 
# element in the list, or reversing a list? 

# Example list
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.72, "dad", 1.89]
print(fam)

# Using the index() method to get the index of "mom"
print(fam.index("mom"))

# Using count() method to count occurrences of 1.73
print(fam.count(1.73))

# Experimenting with string methods
sister = "liz"

# Capitalize the first letter
print(sister.capitalize())

# Find the index of the character 'z'
print(sister.index("z"))

# Replace 'z' with 'sa'
print(sister.replace("z", "sa"))

# Strings come with a bunch of methods, such as .upper() and .count()
place = "poolhouse"

# Convert the string to uppercase
place_up = place.upper()

# Print original and modified strings
print(place)
print(place_up)

# Count occurrences of 'o' in the string
print(place.count("o"))

# List Methods

# Lists also come with useful methods such as .index() and .count()
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Get the index of the element 20.0
print(areas.index(20.0))

# Count how many times 9.50 appears in the list
print(areas.count(9.50))

# List Methods (2)

# Most list methods will change the list they're called on.
# Examples: .append(), .remove(), and .reverse()
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage sizes
areas.append(24.5)
areas.append(15.45)

# Print the list after appending
print(areas)

# Reverse the order of the elements
areas.reverse()

# Print the reversed list
print(areas)