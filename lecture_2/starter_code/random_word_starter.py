# we want to use the randint function from random

from random import randint

# we need somewhere to get our letters to generate a random word!
alphabet = "abcdefghijklmnopqrstuvwxyz"

# we can pass in an alphabet, which is list a string of 
# characters to choose from, so we can customize the list if we want later
def rand_word(alphabet):
    # the length of our word will be a random number, generated with randint()
    length = ???
    
    # we wanna start with an empty word we can add to in a loop
    word = ""

    for i in range(0, length):
        # we need a random number that is no longer than alphabet
        n = randint(0, ???)
        # we take the nth element of alphabet and add it on to word
        word = ???
        
    return word
