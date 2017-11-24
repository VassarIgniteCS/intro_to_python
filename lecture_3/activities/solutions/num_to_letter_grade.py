# write a function that takes in a numeric grade
# and then returns its corresponding letter grade

# assume that all numeric grades are between [0, 100]
# and that letter grades are the traditional A, B, C, D, and F
def num_to_letter_grade(num_grade):
    if num_grade >= 90:
        return "A"
    elif num_grade >= 80:
        return "B"
    elif num_grade >= 70:
        return "C"
    elif num_grade >= 60:
        return "D"
    else:
        return "F"
# HINT: use control flow statements as discussed in lecture 1
