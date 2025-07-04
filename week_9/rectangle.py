# Calculates the area and parameter of the rectangle
# Users input the length and width and get the total of the area and parameter

import math

def area_rectangle(length, width):
    return length * width

''' Function to calculate parameter'''
def parameter_rectangle(length, width):
    return 2 * (length + width)

''' Function to get a valid number greater than zero'''
def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be greater than 0. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

''' Main program '''
print("Rectangle Area and Perimeter Calculator")

length = get_valid_input("Enter the length of the rectangle: ")
width = get_valid_input("Enter the width of the rectangle: ")

area = area_rectangle(length, width)
perimeter = parameter_rectangle(length, width)

print(f"The area of the rectangle is: {area}")
print(f"The parameter of the rectangle is: {perimeter}")