# Week 1.2, Session 1: Task 3

fruit = ("apple", "banana", "cherry")
print(fruit)

# Find and display position of "banana"
banana_index=fruit.index("banana")
print(f"the positition of banana is {banana_index}")

# Display how many times "cherry" occurs
cherry_count=fruit.count("cherry")
print(f"there are {cherry_count} cherries")

# Display how many times "strawberry" occurs
strawb_count=fruit.count("strawberry")
print(f"there are {strawb_count} strawberries")

# Unpack tuple into variables
a,b,c = fruit
print(a)
print(b)
print(c)