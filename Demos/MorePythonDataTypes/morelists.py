list1 = []
list2 = ["Italy", "France", "Spain"]
list3 = [3, 12, 19, 1, 2, 7]
list4 = list()
list5 = list(list3)
list6 = list("Hello")


print("list1 has %d items: %s" % (len(list1), list1))
print("list2 has %d items: %s" % (len(list2), list2))
print("list3 has %d items: %s" % (len(list3), list3))
print("list4 has %d items: %s" % (len(list4), list4))
print("list5 has %d items: %s" % (len(list5), list5))
print("list6 has %d items: %s" % (len(list6), list6))


# Create a list
numbers = [10, 20, 30, 40]
print("Initial list:", numbers)

# Add a single element at the end
numbers.append(50)

# Add multiple elements
numbers.extend([60, 70])

# Insert at a specific position (index 2)
numbers.insert(2, 25)

print("After adding elements:", numbers)

# Remove by value (removes first occurrence)
numbers.remove(25)

# Remove by index
removed_value = numbers.pop(3)  # removes element at index 3

# Remove last element
numbers.pop()

# Delete using del
del numbers[0]

print("After removing elements:", numbers)
print("Removed value:", removed_value)

for num in numbers:
    print(num)

for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")

for index, value in enumerate(numbers):
    print(f"Index {index}, Value {value}")

# Quick Summary
# append() → add one item
# extend() → add multiple items
# insert() → add at position
# remove() → remove by value
# pop() → remove by index / last
# del → delete using index
# for loop → iterate