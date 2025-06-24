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