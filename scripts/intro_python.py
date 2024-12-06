# Interactive Python Script

# Welcome message
print("# Hello Python!")
print("\n## Python as a calculator")
print("Python is perfectly suited to do basic calculations. It can do addition, subtraction, multiplication, and division.")

# Basic calculations
print("\nHit run code to see the output!")
print("5 / 8 =", 5 / 8)

# User exercises for basic operations
print("\nPrint the sum of 4 + 5:", 4 + 5)
print("Print the result of subtracting 5 from 5:", 5 - 5)
print("Print the result of multiplying 3 by 5:", 3 * 5)
print("Print the result of dividing 10 by 2:", 10 / 2)

# Variables and Types
print("\n## Variables and Types")
print("Assigning values to variables and calculating BMI:")

# User-provided input for BMI calculation
height = float(input("Enter your height in meters (e.g., 1.79): "))
weight = float(input("Enter your weight in kilograms (e.g., 68.7): "))

# BMI calculation
bmi = weight / height ** 2
print("Your BMI is:", bmi)

# Variable types
print("\n## Python Types")
print("BMI is of type:", type(bmi))

# Examples of different types
day_of_week = 5
print("An integer type:", type(day_of_week))

x = "body mass index"
print("A string type:", type(x))

z = True
print("A boolean type:", type(z))

# Operations with different types
intro = "Hello! How are you?"
doubleintro = intro + intro
print("\nString concatenation example:")
print(doubleintro)

# Working with lists
print("\n## Lists and slicing")
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Slicing lists interactively
print("\nOriginal list of areas:", areas)
downstairs = areas[:6]
upstairs = areas[6:]
print("Downstairs:", downstairs)
print("Upstairs:", upstairs)