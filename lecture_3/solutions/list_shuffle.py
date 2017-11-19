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
	for i in range(len(list1)):
		#append an element from list1 and an element from list2
		shuffle.append(list1[i])
		shuffle.append(list2[i])
	return shuffle

def list_shuffle2(list1, list2):
	if len(list1) < len(list2):
		#if the length of the first list is less than the second
		#shuffle up to list1 then append the rest of list2
		shuffle = list_shuffle(list1, list2[:len(list1)]) + list2[len(list1):]
	elif len(list2) < len(list1):
		#if the length of the first list is less than the second
		#shuffle up to list2 then append the rest list1
		shuffle = list_shuffle(list1[:len(list2)], list2) + list1[len(list2):]
	else:
		#else, just do the regular list_shuffle
		shuffle = list_shuffle(list1, list2)
	return shuffle

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']
print(list_shuffle(a, b))

a = [1, 2, 3, 4, 5, 6]
b = ['a', 'b', 'c']
print(list_shuffle2(a, b))

a = [1, 2, 3]
b = ['a', 'b', 'c', 'd', 'e']
print(list_shuffle2(a, b))