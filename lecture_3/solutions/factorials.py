'''
==========================================================
FACTORIAL SOLUTION
----------------------------------------------------------
Usually, factorials are denoted by a ! and it follows this
pattern:

0! = 1
1! = 1
2! = 1 * 2         = 2
3! = 1 * 2 * 3	   = 6
4! = 1 * 2 * 3 * 4 = 24
=========================================================
'''
#returns n!
def factorials(n):
	facty = 1
	for i in range(1,n+1):
		facty = facty * i
	
	return facty

			         # prints:
print(factorials(0)) # 1
print(factorials(1)) # 1
print(factorials(2)) # 2
print(factorials(3)) # 6
print(factorials(4)) # 24