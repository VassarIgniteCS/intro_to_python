
names = []
numbers = []

# here we have a list of the two lists, which we can use to represent a phonebook
phonebook = [names, numbers]

# we want this function to take in our phonebook, a name to add, and the phone number of that name
def add_entry(phonebook, name_to_add, number_to_add):
    # first, we want to get the names and numbers lists from inside the phonebook
    names =  ??
    numbers =  
    
    # use the list.append(item) function to add the parameters to the lists 
    names.append(???)
    numbers.append(???)
    
    # now we want to reconstruct the phonebook with our updates lists
    phonebook = [names, numbers]
    
    return phonebook

# we want this function to take in the phonebook and a name to lookup
def get_number(phonebook, name):
    # we need to retrieve the two lists from inside of phonebook
    names = ??
    numbers = ??
    
    # we want to go through the names list until we 
    # find the name we're looking for. 
    # we know that the number we're looking for has the same index
    # as the name, so we can just return the number at that index
    # this return ends the loop, even if we haven't gotten through it!
    for i in range(0, ???):
        if ??? == name:
            return ???
        

def display_phonebook(phonebook):
    # we need to retrieve the two lists from inside of phonebook
    names =  ??
    numbers = ??
    
    # we want to go through the entire list.
    # we could use len(names) or len(numbers), they're always gonna be the same!
    for i in range(0, len(names)):
        # we just print both the name and the number on the same line
        print(??, ??)
