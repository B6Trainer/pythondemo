dict1 = {"us":"+1", "nl":"+31", "no":"+47"}
dict2 = dict()
dict3 = dict({"us":"+1", "nl":"+31", "no":"+47"})
dict4 = dict(us="+1", nl="+31", no="+47")
dict5 = dict(zip(["us", "nl", "no"], ["+1", "+31", "+47"]))

print("dict1 has %d items: %s" % (len(dict1), dict1))
print("dict2 has %d items: %s" % (len(dict2), dict2))
print("dict3 has %d items: %s" % (len(dict3), dict3))
print("dict4 has %d items: %s" % (len(dict4), dict4))
print("dict5 has %d items: %s" % (len(dict5), dict5))


print("Items:")
for k,v in dict1.items():
    print(k, v)
print("\nKeys:")
for k in dict1.keys():
    print(k)
print("\nValues:")
for v in dict1.values():
    print(v)

print("%s" % "us" in dict1) # True
print("%s" % "us" not in dict1) # False
dict1["uk"] = "+44"
print(dict1["uk"]) # +44
print(dict1.get("fr")) # None
print(dict1.get("fr", "xxx")) # xxx
del dict1["no"]
print(dict1.pop("uk")) # +44
print(dict1.pop("uk", "xxx")) # xxx
print(dict1.setdefault("it", "???")) # ???
dict1.update({"ca":"+1", "it":"+39"})
print(dict1) # {'ca': '+1', 'us': '+1', 'nl': '+31', 'it': '+39'}


# Create a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "Chennai"
}

print("Initial dictionary:", person)

# Add a new key-value pair
person["email"] = "alice@example.com"

# Update existing value
person["age"] = 26

# Add multiple values
person.update({
    "country": "India",
    "profession": "Engineer"
})

print("After adding elements:", person)

# Remove by key
person.pop("city")

# Remove last inserted item
person.popitem()

# Delete using del
del person["email"]

print("After removing elements:", person)

# Iterating over dictionary
print("Iterating over Dictionary:")
for key in person:
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"Key: {key}, Value: {value}")


# Quick Summary
# Dictionary stores key → value pairs
# Add/Update → dict[key] = value, update()
# Remove → pop(), popitem(), del
# Iterate → keys(), values(), items()