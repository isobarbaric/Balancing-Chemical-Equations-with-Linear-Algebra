
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

print(type(grid[2][2]))

def Print():
    global grid
    for row in grid:
        print(row)

def gaussian_elimination():
    global row, col
    for i in range(row-1):
        current = grid[i][i]
        for j in range(i+1, row):
            ratio = -1*grid[j][i]/current
            print(ratio)
            for k in range(col):
                grid[j][k] += ratio*grid[i][k]
        Print()

gaussian_elimination()

### C++ driver code
# int row = 4;
# int col = 3;

# int grid[3][4] = {
#   {-3, 2, -1, -1},
#   {6, -6, 7, -7},
#   {3, -4, 4, -6} 
# }; // +1 for one-indexing and last row for 
#   for (int i = 0; i < row-1; i++) {
#     fraction numberCurrFront(grid[i][i]);
#     for (int newRow = i+1; newRow < row; newRow++) {
#       fraction ratio = -1*grid[newRow][i]/numberCurrFront;
#       cout << ratio << '\n';
#       for (int j = 0; j < col; j++) {
#         grid[newRow][j] += ratio*grid[i][j];
#       }
#     }
#   }
