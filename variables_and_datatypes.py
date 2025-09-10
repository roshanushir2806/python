# ============================
# Variables and Data Types in Python
# ============================

# Variable assignment
x = 10
print("x:", x)

# Changing variable type
x = "Hello Python"
print("x changed to:", x)

# Basic data types
num = 42               # int
pi = 3.14              # float
name = "Roshan"        # str
is_learning = True     # bool

print(num, pi, name, is_learning)

# List
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)

# Tuple
colors = ("red", "green", "blue")
print("Tuple:", colors)

# Set
unique_numbers = {1, 2, 2, 3, 4}
print("Set (no duplicates):", unique_numbers)

# Dictionary
student = {"name": "Roshan", "age": 20, "lang": "Python"}
print("Dictionary:", student)

# Type conversion
a = "100"
print("int(a):", int(a))
print("float(a):", float(a))
print("str(10):", str(10))

# Checking types
print(type(num))
print(type(name))
print(type(fruits))

# Multiple assignment
x, y, z = 5, 10, 15
print("x:", x, "y:", y, "z:", z)


# ============================
# Practice Tasks + Solutions
# ============================

# Task 1: Swap two numbers
a = 5
b = 10
print("\nBefore Swap -> a:", a, "b:", b)
a, b = b, a
print("After Swap -> a:", a, "b:", b)

# Task 2: Find the average of three numbers
n1, n2, n3 = 12, 15, 18
avg = (n1 + n2 + n3) / 3
print("\nAverage of", n1, n2, n3, "is:", avg)

# Task 3: Count total characters in a string
my_str = "Python is fun"
char_count = len(my_str)
print("\nTotal characters in string:", char_count)

# Task 4: Get first and last element of a list
nums = [10, 20, 30, 40, 50]
print("\nFirst element:", nums[0])
print("Last element:", nums[-1])

# Task 5: Create a dictionary of squares from 1 to 5
squares = {i: i**2 for i in range(1, 6)}
print("\nDictionary of squares:", squares)

# Task 6: Check if a number is even or odd
number = 17
if number % 2 == 0:
    print("\n", number, "is Even")
else:
    print("\n", number, "is Odd")

# Task 7: Convert Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print("\n", celsius, "Celsius = ", fahrenheit, "Fahrenheit")

# Task 8: Find unique elements from a list
nums_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums_with_duplicates))
print("\nUnique numbers:", unique_nums)

# Task 9: Concatenate two strings
s1 = "Python"
s2 = "Rocks"
result = s1 + " " + s2
print("\nConcatenated string:", result)

# Task 10: Reverse a string
text = "Hello"
reversed_text = text[::-1]
print("\nReversed string:", reversed_text)

