'''
==========================================================
STAR TRIANGLE SOLUTION
----------------------------------------------------------
Takes in a number n prints triangle that looks like this:
*
**
***
****
*****
... and so on, where the last row has n number of stars

=========================================================
'''
#prints n number of rows of stars
def star_triangle(n):
	#start i at 1, then 2, 3....n 
	#n+1 since the range function stops one before 
	for i in range(1,n+1):
		print('*'*i)

star_triangle(3)
star_triangle(5)
