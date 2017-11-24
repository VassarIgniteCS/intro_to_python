# write a function that takes in a triangle's base and height
# and then returns the area of that triangle

# triangle_area
# given a triangle's base and height, will return the area of said triangle
def triangle_area(b, h) :
    return (b * h) / 2

print(triangle_area(0, 0)) # prints 0.0
print(triangle_area(1, 1)) # prints 0.5
print(triangle_area(2, 3)) # prints 3.0
print(triangle_area(3, 2)) # prints 3.0
print(triangle_area(24, 42)) # prints 504.0
