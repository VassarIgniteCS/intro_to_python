'''
==========================================================
LIST SHUFFLE
----------------------------------------------------------
Say we have two lists:
[1, 2, 3, 4, 5] and 
['a', 'b', 'c', 'd', 'e']

If we interleaved them together they would look like:
[1, 'a', 2, 'b', 3, 'c', 4, 'd', 5, 'e']

Let's write a function that takes two lists of the same
length and shuffles them together!
=========================================================
'''

#takes in two equally length list and returns both list shuffled together
def list_shuffle(list1, list2):
	shuffle = []
	#for i from 0 to length of list1 - 1
		#append to shuffle an element from list1 and an element from list2
	return shuffle

# CHALLENGE: write another function, list_shuffle2 that takes any two lists
#            of any length and shuffles them together. If one is smaller than the other,
#            just append the rest of the bigger list to the end
# Hint: If list2 is bigger than list1, you can get a list1 sized list of list2 by doing
#       list2[:len(list1)] and then you can add the rest of list2 with list2[:len(list1)]

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']
print(list_shuffle(a, b))

