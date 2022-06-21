"""
map() is a function in python that creates a new array from
calling a function for every array element. It calls a function once
for each element in an array and does not execute the functionn for
empty elements.
"""
import math

def area(x):
    return round(math.pi*(x**2), 2)

radius = [1, 2, 3]

area_list = list(map(area, radius))
print(area_list)

#prints [3.14, 12.57, 28.27]