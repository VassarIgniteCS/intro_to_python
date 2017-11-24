
# we want to import the sqrt() function from the math package

from math import sqrt
# we can also write "import math"
# and then call "math.sqrt()" instead

def pythag(a, b):
    # pythagoras tells us that, for a right triangle, a^2 + b^2 = c^2, where
    # c is the hypotenuse (the side opposite the right angle), and a and b
    # are the legs (the other two sides)
    # x**y = "x to the power of y"
    c_squared = a**2 + b**2
    
    # we want to return the square root of c_squared
    return sqrt(c_squared)
