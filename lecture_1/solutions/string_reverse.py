# input a string to reverse
to_reverse = input("enter a string: ")

# set our index variable for use in the while loop
index = 0

# set an empty string to collect our reversed string as we go through the loop
reversed_string = ""

# while loop
while index < len(to_reverse):
    reversed_string = to_reverse[index] + reversed_string
    index = index + 1
    
# print out the reversed string
print(reversed_string)
    
