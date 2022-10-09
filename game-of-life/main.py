import copy
import os
import time

class Universe:
    def __init__(self, gens, cols, rows, field):
        self.gens = gens
        self.cols = cols
        self.rows = rows
        self.field = field

def create_universe(data):
    data = data.split('\n')
    field = []
    for i in range(len(data) - 2):
        field.append(list(data[i+2]))
    return Universe(int(data[0]), len(field[0]), len(field), field)

def neighbours(universe, x, y):
    count = 0
    for i in (-1, 0, 1):
        cordX = x + i if x + i < universe.cols else 0
        for t in (-1, 0, 1):
            cordY = y + t if y + t < universe.rows else 0
            if i == 0 and t == 0:
                continue
            if universe.field[cordY][cordX] == 'x':
                count += 1
    return count

def cell_change(cell, neighs):
    if cell == '.':
        return 'x' if neighs == 3 else '.'
    else:
        return '.' if neighs < 2 or neighs > 3 else 'x'

def next_gen(universe):
    nextgen = copy.deepcopy(universe.field)
    for i in range(universe.cols):
        for t in range(universe.rows):
            neighs = neighbours(universe, i, t)
            nextgen[t][i] = cell_change(universe.field[t][i], neighs)
    return nextgen

def evolution(universe, anim=False):
    for i in range(universe.gens):
        universe.field = next_gen(universe)
        if anim:
            os.system('clear')
            print('gen {}'.format(i+1))
            for i in range(universe.rows):
                print(''.join(universe.field[i]))
            time.sleep(0.5)


if __name__ == "__main__":
    f = open('input.txt', 'r')
    data = f.read()
    f.close()

    uni = create_universe(data)
    evolution(uni, anim=True)

    f = open('output.txt', 'w')
    for row in uni.field:
        for col in row:
            f.write(col)
        f.write('\n')
    f.close()
