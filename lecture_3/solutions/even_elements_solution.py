#     .--------.
#    | Step One |
# .--'----------'-----------------------------------------------.
# | First, we need a list that we can use to test our function. |
# '-------------------------------------------------------------'


#       .---------------> Define a variable called example_list, and assign it the value of the proceeding expression.
#       |
#       |           .---> This expression is just a list of integers, so there's nothing to evaluate.
#       |           |
# .-----'---.   .---'----------------.
#/           \ /                      \
example_list = [7, 4, 8, 3, 9, 2, 6, 5]


#     .--------.
#    | Step Two |
# .--'----------'----------------------------------------------------------------.
# | We need some variables to help guide our loop through the list:              |
# |                                                                              |
# | CURR_ELT, to track the current element we're looking at in the list          |
# | LIST_LENGTH, to know when we're at the end of the list and can stop our loop |
# '------------------------------------------------------------------------------'


#      .---------------> Define a variable called list_length, and assign it the value of the proceeding expression.
#      |
#      |           .---> As part of evaluating expressions, Python will call functions and replace them with the value they return.
#      |           |
# .----'---.   .---'---------.
#/          \ /               \
list_length = len(example_list)


#    .---------> Define a variable called curr_elt, and assign it the value of the proceeding expression.
#    |
#    |     .---> Lists are 0-indexed, meaning that elements are indexed starting at 0.
#    |     |     We want the element we're looking at when we start to be the first in the list, so we use 0.
# .--'--.  |
#/       \ |
curr_elt = 0


#     .----------.
#    | Step Three |
# .--'------------'-------------------------------------------.
# | Let's define a function to make our code a little neater. |
# '-----------------------------------------------------------'


#      .---------> This is the name of the function.
#      |
#      |     .---> This tells the function to expect a parameter when it is called.
#    .-'-.   |     When created our function, we use "val" to describe what we want to do to some input 
#   /     \  |       that we don't know the value of yet. This allows our code to be more dynamic!
def is_even(val):
	if val % 2 == 0:   # <-- The % is the modulus operator. It calculates the remainder when dividing its operands. So, (val % 2) simulates (val / 2), and 
		return True    #     rather than returning the result, it returns the remainder. It is very common to check if a number (val, in this case) is even
	else:              #     by checking whether the remainder when dividing by 2 is 0. We can use an if-else statement to return True or False depending on
		return False   #     the value of the expression (val % 2 == 0).


# We can simplify is_even(), but it isn't as clear as the way we had it written before.
# 
#     val % 2 == 0  |  return
#     ------------------------
#             True  |  True
#            False  |  False
#                   |
#                   
# The boolean that we get when we evaluate the expression (val % 2 == 0) is already what we want to return.
# So rather than return True or False explicitly, we can skip the entire if-else statement and just return
# the value that the expression evaluates to in the first place. How convenient!
def is_even_opt(val):
	return val % 2 == 0   


#     .---------.
#    | Step Four |
# .--'-----------'-------------------------------------------.
# | Time to make the mechanism part of our program!          |
# '----------------------------------------------------------'


#     .---------------> First, we're going to use a while loop to allow us to check each element of the list.
#   .'
# .'              .---> Before executing the body, we always check that this expression evaluates to True. If it doesn't, we stop looping
# |              |      and start executing the code immediately after the while loop (marked by the change in indentation).
# |    .---------'--------.
# |   /                    \
while curr_elt < list_length:
	# We access an element of the list using the index variable we created, curr_elt.
	# Then, we store that integer in a variable called curr_val.
	curr_val = example_list[curr_elt]

    # We use an if statement to allow us to do different things depending on whether curr_val is even.
    # We don't have an "else" case because we want to do nothing if curr_val is odd.
	if is_even(curr_val):
		# We are not inside the "if body". We know that if we get to this point, it must be the case that
		# curr_val holds an even number. We're going to add that to our list of even numbers... because it's even!
		even_list.append(curr_val)

    # Here, we increase curr_elt by 1 so that we can look at the next element of the list
    # once we loop back up to check the while conditional and potentially execute the loop code again.
    # Because we increased curr_elt by 1, curr_val will be assigned the next element in the list, and
    # the loop will do the same to it as it did to the previous element.
	curr_elt = curr_elt + 1

# We've made it passed the while loop! Now we're just printing both lists to see
# whether even_list contains exactly the even elements of example_list.
print(example_list)
print(even_list)



#     .----------------.
#    | Some final notes |
# .--'------------------'--------------------------------------.
# | -> This is by no means the only way to extract even        |
# |    elements from a list.                                   |
# |                                                            |
# | -> Your solution could look completely different but still |
# |    be correct -- maybe even better!                        |
# |                                                            |
# | -> Example: use a for loop instead of a while loop         |
# |                                                            |
# |    for curr_val in example_list:                           |
# |        if is_even(curr_val):                               |
# |            even_list.append(curr_val)                      |
# |                                                            |
# |    You don't even need curr_elt or list_length!            |
# '------------------------------------------------------------'


# There are a LOT of comments in the code above, so here's just the code.

# example_list = [7, 4, 8, 3, 9, 2, 6, 5]
# list_length = len(example_list)
# curr_elt = 0
# 
# def is_even(val):
# 	if val % 2 == 0:
# 		return True
# 	else:
# 		return False
# 		
# while curr_elt < list_length:
# 	curr_val = example_list[curr_elt]
#
# 	if is_even(curr_val):
# 		even_list.append(curr_val)
#
# 	curr_elt = curr_elt + 1
# 	
# print(example_list)
# print(even_list)