
# we can make our own "repl" function (replace is already used!) with
# the same code we used for the last challenge of the first lecture

def repl(string, old, new):
    i = 0

    while i < len(string):
        
        # if the string the length of the string we are replacing that starts
        # at our current index is equal to the string we are replacing, execute the next line!
        if string[i : i + len(old)] == old:
            # here, we are taking everything that comes before the appearance of old in string,
            # adding new to that, and finally adding whatever follows this appearance of old in string
            string = string[:i] + new + string[i + len(old):]
                
        i += 1

    return string
