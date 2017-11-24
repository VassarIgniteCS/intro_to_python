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
	#the first factorial (0!) is 1, so let's start there
	facty = 1
	#then we want to multiply facty * 1, 
	#then facty * 2 
	#then facty * 3
	#... 
	#then facty * n

	return facty

			         # prints:
print(factorials(0)) # 1
print(factorials(1)) # 1
print(factorials(2)) # 2
print(factorials(3)) # 6
print(factorials(4)) # 24