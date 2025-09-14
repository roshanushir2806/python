# Core Python - Conditional Statements
# My notes + examples + practice tasks 

# 1. Simple if
print("=== Simple if ===")
x = 10
if x > 5:
    print("x is greater than 5")  # condition true


# 2. if-else
print("\n=== if-else ===")
num = 7
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 3. if-elif-else ladder
print("\n=== if-elif-else ladder ===")
marks = 82
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")


# 4. Nested if
print("\n=== Nested if ===")
age = 20
if age > 18:
    if age < 60:
        print("You are an adult")
    else:
        print("You are a senior citizen")
else:
    print("You are a minor")


# 5. Shorthand if
print("\n=== Shorthand if ===")
y = 12
if y > 10: print("y is greater than 10")  # one-liner


# 6. Shorthand if-else (ternary operator style)
print("\n=== Shorthand if-else ===")
a = -5
result = "Positive" if a > 0 else "Non-positive"
print(result)


# 7. Multiple conditions using logical operators
print("\n=== Multiple conditions with and/or ===")
temperature = 28
rain = False

if temperature > 25 and not rain:
    print("It's hot and dry outside.")
elif temperature > 25 and rain:
    print("It's hot but raining.")
else:
    print("Weather is normal.")


# 8. Checking membership
print("\n=== Membership in if ===")
fruits = ["apple", "banana", "mango"]
if "apple" in fruits:
    print("Apple is available!")
else:
    print("No apple found.")


# 9. Real life login example
print("\n=== Real life example ===")
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful ✅")
else:
    print("Login failed ❌")


# ---------------------------------------------------
# 📝 PRACTICE TASKS 
# ---------------------------------------------------

print("\n=== Practice Task 1 ===")
# Task: Check if a number is positive, negative, or zero
n = -3
if n > 0:
    print(f"{n} is Positive")
elif n < 0:
    print(f"{n} is Negative")
else:
    print("The number is Zero")


print("\n=== Practice Task 2 ===")
# Task: Find the largest of three numbers
a, b, c = 12, 45, 23
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print(f"Largest number is {largest}")


print("\n=== Practice Task 3 ===")
# Task: Check if a year is a leap year
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT a Leap Year")


print("\n=== Practice Task 4 ===")
# Task: Simple calculator using if-elif
x, y = 15, 3
operator = "/"

if operator == "+":
    print(f"Sum = {x + y}")
elif operator == "-":
    print(f"Difference = {x - y}")
elif operator == "*":
    print(f"Product = {x * y}")
elif operator == "/":
    print(f"Quotient = {x / y}")
else:
    print("Invalid Operator")


print("\n=== Practice Task 5 ===")
# Task: Voting eligibility check
age = 17
citizen = True
if age >= 18 and citizen:
    print("You are eligible to vote ✅")
else:
    print("You are NOT eligible to vote ❌")
