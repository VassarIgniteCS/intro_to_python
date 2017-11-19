'''
==========================================================
QUADRATIC FORMULA
----------------------------------------------------------
Do you remember the quadratic formula? It's use to find
where a quadratic function crosses the x axis, like this:
 .    |    .
  .   |   .
____._|_._____
      .  

Quadratic equation have the form:
y = ax^2 + bx + c, where a, b, c are constants

We can solve for this equation using the quadratic formula:
           _________
x = -b +- √b^2 - 4ac
    -----------------
           2a

The b^2 - 4ac part is called the determinant and cannot be negative
The +- means there are two solutions, one plus and one minus
So let's make a quadratic equation solver!
=========================================================
'''
import math

#returns the roots of the quadratic equation
def quadratic(a,b,c):
	determinant = b**2 - 4*a*c
	if determinant >= 0:
		#determinant is positive
		x_plus  = (-b + math.sqrt(determinant))/(2*a)
		x_minus = (-b - math.sqrt(determinant))/(2*a)
	else:
		#determinant is negative, can't take the square root of that!
		x_plus  = "ERROR"
		x_minus = "ERROR"

	#return both solutions
	return [x_plus, x_minus]

print(quadratic(1,0,-1)) #prints [1.0, -1.0]
print(quadratic(1,-2,0)) #prints [2.0, 0.0]
print(quadratic(1,2,5))  #prints ["ERROR", "ERROR"]
