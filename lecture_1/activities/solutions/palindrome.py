# input a string to check
string = input("enter a string: ")

# this is the exact same code we wrote in the previous activity to reverse a string!
index = 0
reversed_string = ""

while index < len(string):
    reversed_string = string[index] + reversed_string
    index = index + 1

# now we have a string and the reverse of that string (stored in reversed_string)
# if these two strings are the same, than the input string is a palindrome!
if string == reversed_string:
    print(string + " is a palindrome!")
else:
    print(string + " is not a palindrome!")
