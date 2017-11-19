#====================================#
#  Extract even numbers from a list  #
#------------------------------------#
#  Given a list of integers, make a  #
#  list that contains only the even  #
#  integers of that list.            #
#====================================#

#     .------------------.
#    | Some initial notes |
# .--'--------------------'------------------------------------.
# | -> This is by no means the only way to extract even        |
# |    elements from a list.                                   |
# |                                                            |
# | -> If you think of a different way, try it out! Ask for    |
# |    help if you need!                                       |
# '------------------------------------------------------------'


#     .--------.
#    | Step One |
# .--'----------'-----------------------------------------------.
# | First, we need a list that we can use to test our function. |
# | You don't need to change anything for this step!            |
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

# We need this variable to hold the number of elements in example_list. That way, we can
# know when to stop looping through it and won't accidentally check for more numbers than the list has.
list_length = <PLACEHOLDER>

# We need this variable to track the index of the current element we're looking at. The value we assign
# it now represents the index of the first element in example_list. What is the index of the first element in any list?
curr_elt = <PLACEHOLDER>


#     .----------.
#    | Step Three |
# .--'------------'-----------------------------------------------.
# | Let's define a function to check whether a number is even.    |
# | We want it to return True if it's even and False if it's odd. |
# '---------------------------------------------------------------'

# A common way to check whether a number is even is to check the remainder of the number in question divided by 2.
# The % operator is called modulus, and it returns just the remainder of some division.
# 
# For example: (10 % 3) evaluates to 1 because 10 divided by 3 is 3 with a remainder of 1
# 
# What remainder when dividing val by 2 would indicate that val is even?

# Replace each <PLACEHOLDER> to complete the function!
def is_even(val):
	if val % 2 == <PLACEHOLDER>:
		<PLACEHOLDER>
	else:
		<PLACEHOLDER>

# Extra bit: Can you think of way to write this function without an if-else statement?


#     .---------.
#    | Step Four |
# .--'-----------'--------------------------------------.
# | Time to make the mechanism of our program!          |
# '-----------------------------------------------------'

#     .---------------> First, we're going to use a while loop to allow us to check each element of the list.
#   .'
# .'              .---> Before executing the body, we always check that this expression evaluates to True. If it doesn't, we stop looping
# |              |      and start executing the code immediately after the while loop (marked by the change in indentation).
# |    .---------'--------.
# |   /                    \
while curr_elt < list_length:
	# Here, let's assign curr_val the value of the current element in example_list that we're looking at.
	# Remember, we previously made curr_elt for this exact purpose! How do we access the curr_elt^th (imagine the superscript :s) element in example_list?
	curr_val = <PLACEHOLDER>

    # We use an if statement to allow us to do different things depending on whether curr_val is even.
    # We want our expression to test whether curr_val is even. I think it might be time to use that function from before!
	if <PLACEHOLDER>:
		# Once we're in the body of the if, we know that curr_val is even, so in here we want to add curr_val to
		# the list we made that will contain only even numbers. There might be a useful built-in function we can use here.
		<PLACEHOLDER>

    # Now, we're getting to the end of the while body, so we want to make sure that the next time we execute it, we are looking
    # at this /next/ element, rather than the current one. We can do that by incrementing curr_elt because curr_elt determines what value we
    # put into curr_val.
	curr_elt = <PLACEHOLDER>

# We've made it passed the while loop! Now we're just printing both lists to see
# whether even_list contains exactly the even elements of example_list. Nothing to do here!
print(example_list)
print(even_list)