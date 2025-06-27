#This file contains lessons on how to work with numeric data

num = 3

print(num) #Prints the value of the variable
print(type(num)) #Prints the variable type

num2 = 3.14

print(type(num2)) #Prints the variable type

#Variables 

my_variable = 10
total_count = 0
user = 'Lilly'

#Invalid 
# An invalid variable name 2nd_variable = 10
# Invalid variable name = user-name = 20

#Operators on Numeric data

# Addition (+)
# Subtraction(-)
# Multiplication(*)
# Division(/)
# Modulus(%) #Is the remainder after division
# Exponent(**)

x = 10
y = 2

print(x+y)
print(x*y)
print(x-y)
print(x/y)
print(x%y) 
print(13%6)
print(x**y)

#Assignment operators

z = 10
z = z + 2 # This is the same as below
z += 2


z -= 2
print(z)

# operators with strings 

str1 = 'Hello'
str2 = 'world'

print(str1 + "" + str2) #Prints the statements without a spce inbetween
print(str1 + " " + str2) #Prints the statements with a space inbetween
print(str1 + " " + str2 + " " + str2) # Prints A string more than once 
print(str1 * 3) #Allows you to print a string multiple times depending on the amount you want

#Control Statements

num = 9

#Checking 2 conditions
if num > 0:
  print("This number is positive.")
else:
    print("This number is either zero or negative")

# Checking 3 different conditions

num1 = 0

if num1> 0:
  print("This number is positive")
elif num1 == 0:
  print("This numberis zero")
else:
  print("This number is negative ") 

# Control Statements Part2
num2 = int(input("Enter the first number:"))
num3 = int(input("Enter the second number:"))

if num2 > num3:
  print(num2, "is greater than", num3)
elif num3 > num2:
  print(num3, "is greater than", num2)
else:
  print("both numbers are equal")

#Loops - For loops

fruits = ["apples", "banana", "cherry"]

for fruit in fruits:
  print(fruit) #Prints one iteration of the list with its content 

numbers = [1, 2, 3, 5, 7]

for number in numbers:
  print(numbers) #Prints out the number of content based on the variables in the list 

  print(number)

# While loops
# Using a while loop to count from 1 to 5

count = 1

while count <= 5:
  print(count)
  count+=1 #Increments the count by one

# Loop control satements
vegtables = ["carrots", "leeks", "brocolli", "potatoes" ]

for vegtable in vegtables:
  if vegtable == "brocolli":
    break #Exits the loop if brocolli if found
  print(vegtable)

print()

for vegtable in vegtables:
  if vegtable == "brocolli":
    continue #Skips brocolli and moves to the iteration
  print(vegtable)

print()

for vegtable in vegtables:
  if vegtable == "brocolli":
    pass #Placeholder, no action is needed for brocolli
  print(vegtable)

#While Control Statements 

total = 0

while total < 5:
  print(total)
  total += 1
  if total == 3:
    break; #Exits the loop when the total is reached = 3