# Manipulating lists with Python

# Changing list elements
# Example: Updating a height value in a list
fam = ["Liz", 1.73, "Emma", 1.68, "mom", 1.71, "dad", 1.89]
print(fam)

# Update dad's height
fam[7] = 1.86
print(fam)

# Change the first two elements
fam[0:2] = ["lisa", 1.74]
print(fam)

# Adding elements to the list
fam_ext = fam + ["me", 1.79]
print(fam_ext)

# Removing elements
del fam[2]
print(fam)

# Working with references
x = ["a", "b", "c"]
y = x
y[1] = "z"
print(y)
print(x)

# To store in a new list (avoiding references)
x = ["a", "b", "c"]
y = list(x)  # or y = x[:]
y[1] = "z"
print(y)
print(x)

# Replace list elements
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"

print(areas)

# Extend a list
areas_1 = areas + ["poolhouse", 24.5]
areas_2 = areas_1 + ["garage", 15.45]
print(areas_2)

# Delete list elements
del areas_2[10:12]
print(areas_2)

# Inner workings of lists
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = list(areas)  # Explicit copy
areas_copy[0] = 5.0
print(areas)

# Quiz: List slicing
p = ["a", "r", "y", "v", "k", "s"]
del p[1:3]
print(p)

foo = [0.2, 1.7, "A", "Wed", "1.5"]
foo[0:2] = [2.75, -1.5]
print(foo)

x = [2, 1, -4, 3, -1, 5]
print(x[-1])

# Concatenating lists
x = ["Winter", "Spring"]
y = ["Summer", "Fall"]
print(x + y)