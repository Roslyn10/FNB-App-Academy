# Functions

# Creating a simple function
def greet(name):
  print(f"Hello, {name}")

greet("Alice")

def add(a, b):
  return a + b

result = add(6, 8)
print(result)



def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n -1)

total = factorial(8)
print(total)