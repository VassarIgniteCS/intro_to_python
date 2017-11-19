'''
==========================================================
FIBONACCI NUMBERS
----------------------------------------------------------
The Fibonacci numbers is a famous sequence that looks like this:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

Notice the pattern? You start with 0 and 1 and the next
number is the previous two numbers added together, so
0
1
1 = 0 + 1
2 = 1 + 1
3 = 1 + 2
5 = 2 + 3
8 = 3 + 5
and so on. Let's generate them!
=========================================================
'''
# returns n number of fibonacci numbers
def fib(n):
	if n == 1:
		# if n is 1, just return [0]
		return [0]
	elif n == 2:
		# if n is 2, just return [0]
		return [0,1]
	else:
		# else, we're going to start with the first two
		#       fibonacci numbers and iterate to n
		fibby = [0,1]
		# Now we want to append the next number on to the list
		# which is calculated from the previous two numbers on the list.
		# Hint: start counting i from 1 up to n+1 and use fibby[i] and fibby[i-1]
		#       to get the current and previous fibonacci number

	return fibby

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))