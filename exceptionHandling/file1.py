# to calculate area and perimeter of a circle the radius input take by user

def caculateArea(radius):
    ans = 3.14*radius*radius
    return ans

def calculatePerimeter(radius):
    ans = 2*3.14*radius
    return ans

radius = float(input("enter the number"))
result = caculateArea(radius)
result2 = calculatePerimeter(radius)
print(result)
print(result2)

import math

# take input from user
radius = float(input("Enter the radius of the circle: "))

# calculate area and perimeter
area = math.pi * radius * radius
perimeter = 2 * math.pi * radius

# display results
print("Area of circle:", area)
print("Perimeter (Circumference) of circle:", perimeter)

# exception should be handle not remove 