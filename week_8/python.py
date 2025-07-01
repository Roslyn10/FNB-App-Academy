# Basics on Lists 

fruits = ["apple", "banana", "cherry"]
print(fruits[2])

fruits[1] = "blueberry"
print(fruits[1])
print(fruits)

# adding items to a list 

vegetables = ["carrot", "potatoes", "lettuce"]
vegetables.append("leeks")
print(vegetables)

vegetables.insert(1, "kale")

print(vegetables)

# Removing items from the list
vegetables.remove("kale")
print(vegetables)

#Sorting the list in alphabetical order
vegetables.sort()
print(vegetables)

#Sorting the list in reverse alphabetical order
vegetables.sort(reverse=True)
print(vegetables)