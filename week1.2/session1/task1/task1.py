# Week 1.2, Session 1: Task 1

# Create a shopping list

shopping = ["eggs", "milk", "flour", "carrots"]
print(shopping)

# We forgot something, so add it to list

shopping.append("bananas")
print(shopping)

# We bought something, so remove it from list

shopping.remove("eggs")
print(shopping)

# Replace bananas with grapes
shopping = ["grapes" if item == "bananas" else item for item in shopping]
print(shopping)

# Add yoghurt, just after milk
for item in range(len(shopping)):
    if shopping[item]=="milk":
        shopping.insert(item+1,"yoghurt")
        break
print(shopping)
