# ==============================
# FILTER EXAMPLES - SINGLE FILE
# ==============================

# 🔹 Example 1: Using normal function
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

result1 = filter(is_even, numbers)
print("Even numbers (function):", list(result1))


# 🔹 Example 2: Using lambda
result2 = filter(lambda x: x % 2 == 0, numbers)
print("Even numbers (lambda):", list(result2))


# 🔹 Example 3: Filter numbers greater than 3
result3 = filter(lambda x: x > 3, numbers)
print("Numbers > 3:", list(result3))


# 🔹 Example 4: Filtering strings
names = ["Alice", "Bob", "Anna", "Charlie"]

result4 = filter(lambda name: name.startswith("A"), names)
print("Names starting with A:", list(result4))


# 🔹 Example 5: Using None (remove falsy values)
data = [0, 1, "", "Hello", None, True, False, "World"]

result5 = filter(None, data)
print("Truthy values:", list(result5))


# 🔹 Example 6: Equivalent using list comprehension
result6 = [x for x in numbers if x % 2 == 0]
print("Even numbers (list comprehension):", result6)


# 🔹 Example 7: Showing iterator behavior
result7 = filter(lambda x: x > 2, numbers)

print("Filter object:", result7)       # iterator
print("Converted to list:", list(result7))  # actual values


# ==============================
# END
# ==============================