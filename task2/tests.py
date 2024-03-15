from area import *
import math


r = 5
a = 3
b = 4
c = 5
p = (a + b + c) / 2
circle = Circle(r)
triangle = Triangle(a, b, c)

assert circle.get_area() == math.pi * r ** 2
assert triangle.get_area() == (p * (p-a) * (p-b) * (p-c)) ** 0.5
assert triangle.is_right() is True
