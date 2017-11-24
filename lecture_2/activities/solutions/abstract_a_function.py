
# we start by defining a function called "rev"
#   (reverse is already the name of a function, so we can't use that!)

# this is the exact code from the first challenge in the last lecture!
# instead of using input() to get the variables, we input them to the function as parameters
def rev(string):
    # set our index variable for use in the while loop
    index = 0

    # set an empty string to collect our reversed string as we go through the loop
    reversed_string = ""

    # while loop
    while index < len(string):
        reversed_string = string[index] + reversed_string
        index = index + 1

    # instead of printing the result to the console with print(), we return the string
    # so that we can use it in the code we are calling the function from
    return reversed_string

# now we can use this function to implement the second challenge from last lecture, checking
# if a word is a palindrome

def is_palindrome(string):

    reversed_string = rev(string)

    # now we have a string and the reverse of that string (stored in reversed_string)
    # if these two strings are the same, than the input string is a palindrome!
    return string == reversed_string
