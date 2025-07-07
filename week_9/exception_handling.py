# Basics of exceptions

try:
  print(x)
# except NameError:
#  print("Variable x is not defined")
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# using the else block

try:
  print(x)
except NameError:
  print("Variable x is not defined")
else:
  print("Everything went wrong")


# raising exceptions
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")