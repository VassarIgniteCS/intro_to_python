from random import random

def gen_field(size, percent_alive):
    field = [[]]
    for i in range(0, size):
        field.append([])
        for n in range(0, size):
            field[i].append(1 if random() < percent_alive else 0)
            
    return field

def display_field(field):
    for i in range(0, len(field) - 1):
        for n in range(0, len(field[0]) - 1):
            print("x " if field[i][n] else "o ", end="")
        print("")
        
def check_neighbors(field, i, n):
    size = len(field) - 1
    neighbors = [i, n, (i+1) % size, (n+1) % size, (i-1) % size, (n+1) % size]
    
    return sum(map(lambda x, y: field[x][y], neighbors, neighbors))

def update(field):
    temp_field = field
    for i in range(0, len(field) - 1):
        for n in range(0, len(field[0]) - 1):
            neighbors = check_neighbors(field, i, n)
            
            if neighbors < 2:
                temp_field[i][n] = 0
            elif neighbors > 3:
                temp_field[i][n] = 0
            elif neighbors == 3:
                temp_field[i][n] = 1
                
    return temp_field


field = gen_field(50, .1)

while True:
    display_field(field)
    
    input()
    update(field)
