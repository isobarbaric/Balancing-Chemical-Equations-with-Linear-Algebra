
from inspect import currentframe
from parser import parser
from fraction import Fraction

class Reaction:

    def __init__(self, reactants, products):
        self.reactants = parser(reactants)
        self.products = parser(products)

a = "Ca2PhO2G4K3O5+H2O"
b = "CE25PO2GhZ33O53+H23710"

# test = Reaction(a, b)

# print(test.reactants, test.products)

# for each reactant, set up an equation on a matrix

# first, let's implement Gauss, then will work in the ideas of the reactant itself

grid = [
    [-3, 2, -1, -1],
    [6, 5, 7, -7],
    [3, -4, 2, -6]
]

row = 3
col = 4

for i in range(row):
    for j in range(col):
        grid[i][j] = Fraction(grid[i][j]) 

# print(type(grid[2][2]))

def Print():
    global grid
    for row in grid:
        print(row)

def gaussian_elimination(grid):
    global row, col
    for i in range(row-1):
        current = grid[i][i]
        for j in range(i+1, row):
            ratio = -1*grid[j][i]/current
            print(ratio)
            for k in range(col):
                grid[j][k] += ratio*grid[i][k]
        
gaussian_elimination(grid)

Print()