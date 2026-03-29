tuple1 = tuple()
tuple2 = "Norway", # or: tuple2 = ("Norway",)
tuple3 = 3, 19, 2 # or: tuple3 = (3, 19, 2)
tuple4 = tuple()
tuple5 = tuple(tuple3)

print("tuple1 has %d items: %s" % (len(tuple1), tuple1))
print("tuple2 has %d items: %s" % (len(tuple2), tuple2))
print("tuple3 has %d items: %s" % (len(tuple3), tuple3))
print("tuple4 has %d items: %s" % (len(tuple4), tuple4))
print("tuple5 has %d items: %s" % (len(tuple5), tuple5))


# Create a tuple
numbers = (10, 20, 30, 40)
print("Initial tuple:", numbers)

# Add element by creating a new tuple
numbers = numbers + (50,)

# Add multiple elements
numbers = numbers + (60, 70)

print("After adding elements:", numbers)


# Remove elements

# Convert tuple to list
temp_list = list(numbers)
temp_list.remove(20)   # remove by value
temp_list.pop(2)       # remove by index

# Convert back to tuple
numbers = tuple(temp_list)

print("After removing elements:", numbers)

# Iterating over tuple
print("Iterating over Tuple:")

for num in numbers:
    print(num)

for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")

for index, value in enumerate(numbers):
    print(f"Index {index}, Value {value}")