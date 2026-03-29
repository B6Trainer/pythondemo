set1 = {"dog", "ant", "bat", "cat", "dog"}
set2 = set()
set3 = set(("dog", "ant", "bat", "cat", "dog"))
set4 = set("abracadabra")
set5 = {c.upper() for c in "abracadabra"}

print("set1 has %d items: %s" % (len(set1), set1))
print("set2 has %d items: %s" % (len(set2), set2))
print("set3 has %d items: %s" % (len(set3), set3))
print("set4 has %d items: %s" % (len(set4), set4))
print("set5 has %d items: %s" % (len(set5), set5))



# Create a set (duplicates are automatically removed)
numbers = {10, 20, 30, 40, 40}
print("Initial set:", numbers)  # {10, 20, 30, 40}

# Add a single element
numbers.add(50)
# Add multiple elements
numbers.update([60, 70, 80])
print("After adding elements:", numbers)

# Remove element (error if not found)
numbers.remove(20)
# Remove element safely (no error if not found)
numbers.discard(100)
# Remove a random element
removed_value = numbers.pop()
# Clear all elements
# numbers.clear()

print("After removing elements:", numbers)
print("Removed value:", removed_value)


# Iterating over set
print("Iterating over Set:")
for num in numbers:
    print(num)


# Bonus: Set Operations

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union (all elements)
print(a | b)  # {1,2,3,4,5,6}

# Intersection (common elements)
print(a & b)  # {3,4}

# Difference
print(a - b)  # {1,2}

# Symmetric Difference
print(a ^ b)  # {1,2,5,6}


# Quick Summary
# No duplicates allowed
# Unordered collection
# Add → add(), update()
# Remove → remove(), discard(), pop()
# Powerful for mathematical operations