# Creating a shopping cart app 
# Allows the user to enter the food and the price of the food

foods = []
prices = []
total = 0

while True:
  food = input("Enter a food to buy or press q to quit: ")
  if food.lower() == 'q':
    break
  else:
    price = float(input(f"Enter the price of the {food}: R"))
    foods.append(food)
    prices.append(price)

  print("--- YOUR CART ---")

for food in foods:
  print(food, end=" ")

for price in prices:
  total += price

print()
print(f"Your total is: R{total}")