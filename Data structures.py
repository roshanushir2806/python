# ============================================
# Core Python - Data Structures
# My personal practice file with examples + tasks
# ============================================

# ----------------------
# 1. LIST
# ----------------------
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

fruits.append("orange")     # add
print("After append:", fruits)

fruits.remove("banana")     # remove
print("After remove:", fruits)

print("First fruit:", fruits[0])   # indexing
print("Slice:", fruits[1:3])       # slicing


# ----------------------
# 2. TUPLE
# ----------------------
colors = ("red", "green", "blue")
print("\nTuple:", colors)
print("First color:", colors[0])

# Tuple is immutable, but we can convert to list if needed
temp = list(colors)
temp.append("yellow")
colors = tuple(temp)
print("Updated tuple:", colors)


# ----------------------
# 3. SET
# ----------------------
nums = {1, 2, 2, 3, 4}
print("\nSet (no duplicates):", nums)

nums.add(5)
print("After add:", nums)

nums.remove(3)
print("After remove:", nums)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)


# ----------------------
# 4. DICTIONARY
# ----------------------
student = {"name": "Roshan", "age": 20, "lang": "Python"}
print("\nStudent:", student)

print("Name:", student["name"])

student["age"] = 21         # update
student["city"] = "Pune"    # add new
print("Updated dict:", student)

del student["lang"]         # delete
print("After delete:", student)

print("Keys:", student.keys())
print("Values:", student.values())


# ============================================
# Practice Tasks
# ============================================

# Task 1: Reverse a list
nums = [1, 2, 3, 4, 5]
print("\nOriginal list:", nums)
print("Reversed list:", nums[::-1])

# Task 2: Find max and min in a list
print("Max:", max(nums))
print("Min:", min(nums))

# Task 3: Convert list to set (remove duplicates)
dupes = [1, 2, 2, 3, 4, 4, 5]
print("Unique elements:", set(dupes))

# Task 4: Count frequency of words in a sentence
sentence = "python is fun and python is easy"
words = sentence.split()
word_count = {w: words.count(w) for w in set(words)}
print("\nWord count:", word_count)

# Task 5: Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print("Merged dict:", merged)

# Task 6: Find common elements in two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))
print("Common elements:", common)

# Task 7: Sort a dictionary by values
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print("Sorted scores:", sorted_scores)

# Task 8: Check if a key exists in dict
print("Check key 'age' in student:", "age" in student)

# Task 9: Convert tuple to list
t = (10, 20, 30)
print("Tuple:", t, "=> List:", list(t))

# Task 10: Create a set of squares from 1 to 5
squares = {x**2 for x in range(1, 6)}
print("Squares set:", squares)
