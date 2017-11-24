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
#returns n number of fibonacci numbers
def fib(n):
	if n == 1:
		#if n is 1, just return [0]
		return [0]
	elif n == 2:
		#if n is 2, just return [0]
		return [0,1]
	else:
		#else, we're going to start with the first two
		#      fibonacci numbers and iterate to n
		fibby = [0,1]
		for i in range(1, n+1):
			#append to fibby the addition of the two previous numbers
			current  = fibby[i]
			previous = fibby[i-1]
			fibby.append(current + previous)

	return fibby

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))