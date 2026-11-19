# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}
print(rivers)

# Add two new entries to the rivers database
rivers["Chelmsford"]="Chelmer"
rivers["Maldon"]="Blackwater"
print(rivers)
print("\n")

# Display all the keys
rivers_keys=rivers.keys()
print(rivers_keys)
print("\n")

# Display all the values
rivers_values=rivers.values()
print(rivers_values)
print("\n")

# Display all the key:value pairs, as tuples
rivers_items=rivers.items()
print(rivers_items)
print("\n")

# Delete an entry from the rivers database
rivers.pop("Leeds")
print(rivers)