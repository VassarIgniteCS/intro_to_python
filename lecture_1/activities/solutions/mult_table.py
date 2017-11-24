dim = 10

# since we are making a multiplication table, which is two dimensional, we need
# two loops, and two index variables

i = 0
while i < dim:
    
    n = 0
    while n < dim:
        # print has an input called end which gets set to "\n" by default,
        # but we can tell it to be an empty string instead, so that print()
        # doesn't create a new line!
        print(i*n, end='')
        # '\t' represents a tab, just like how '\n' represents a new line
        # this is to make the table look nice, you can delete the line and it will still work!
        print('\t', end='')
        n += 1
    # now we have printed out one line of the table, so we want a new line
    print()
    i += 1
