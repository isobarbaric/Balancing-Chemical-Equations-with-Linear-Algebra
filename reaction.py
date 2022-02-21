
from parser import parser
from fraction import Fraction

class Reaction:

    def __init__(self, reactants, products):
        self.reactants = parser(reactants)
        self.products = parser(products)

a = "Ca2PhO2G4K3O5+H2Ca5O"

b = "CE25PO2GhZ33O53Ca5+H23710Pa"
# bug/edge case is when a new element appears in reactants that are not the first reactant in the list
# bruh

test = Reaction(a, b)
print(test.reactants, '\n', test.products)

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

def gaussian_elimination(grid):
    global row, col
    for i in range(row-1):
        current = grid[i][i]
        for j in range(i+1, row):
            ratio = -1*grid[j][i]/current
            for k in range(col):
                grid[j][k] += ratio*grid[i][k]
        
gaussian_elimination(grid)

for row in grid:
    print(row)

# answers = []
# for i in range():
    
# reverse(answers)
# print(answers)

# setting up equations to solve 
# each element in each reactant and product
# -> reactant_1a + reactant_2b + reactant_3c + reactant_4d + .... 
#           = count of 

# here, a,b,c,d... = coefficients in front of the ath, bth, cth, dth... reactant (count in each reactant)
# dimensions of grid = number of unique reactants

