import StringFormatting

# 🔹 Sample strings
s1 = "Hello"
s2 = "World"

# 🔹 1. Using + operator
result_plus = s1 + s2
print("Using + :", result_plus)

# With space
result_plus_space = s1 + " " + s2
print("Using + with space:", result_plus_space)

# 🔹 2. Using f-strings (recommended)
result_fstring = f"{s1} {s2}"
print("Using f-string:", result_fstring)

# 🔹 3. Using join() (best for multiple strings)
words = ["Hello", "World"]
result_join = " ".join(words)
print("Using join():", result_join)

# 🔹 4. Using += operator
s = "Hello"
s += " World"
print("Using += :", s)

# 🔹 5. Multiple string concatenation
a = "Python"
b = "is"
c = "awesome"

result_multi = a + " " + b + " " + c
print("Multiple (+):", result_multi)

result_multi_join = " ".join([a, b, c])
print("Multiple (join):", result_multi_join)

# 🔹 Final note
print("\nNote: Strings are immutable, so each operation creates a new string.")