import calculate

length = float(input("Enter the length of the rectangle:"))
width = float(input("Enter the width of the rectangle:"))

area = calculate.area_rectangle(length, width)
perimeter = calculate.perimeter(length, width)

print("The area of the rectangle is: {area}")
print("The perimeter of the rectangle is: {perimeter}")