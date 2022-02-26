
from parser import parser
from fraction import Fraction
from array import *
import sys

import numpy as np

class Reaction:

    def __init__(self, reactants, products):
        self.len = len(reactants.split('+')) + len(products.split('+'))
        self.reactants = parser(reactants)
        self.products = parser(products)
        self.reactionString = reactants + "->" + products

a = "Ca2PhO2G4K3O5+H2Ca5O"

b = "CE25PO2GhZ33O53Ca5+H23Pa42P34"
# c = "NH3+HCl"
# d = "CO2+H2O"
# d = "NH4Cl"

c = "C3H8+O2".replace(' ', '')
d = "H2O+CO2".replace(' ', '')

print(c, d)

# these two produce different results :sus:

test = Reaction(c, d)
print(test.reactants, '\n', test.products)

indexElements = dict()
id = 0
for element in test.reactants:
    if element not in indexElements.keys():
        indexElements[element] = id
        id += 1
for element in test.products:
    if element not in indexElements.keys():
        indexElements[element] = id
        id += 1

t = []

for i in range(id):
    rn = []
    for j in range(test.len+1):
        rn.append(Fraction(0))
    t.append(rn)

for key in indexElements.keys():
    for values in test.reactants[key]:
        t[indexElements[key]][values[0]-1] = Fraction(values[1])
    for values in test.products[key]:
        t[indexElements[key]][len(test.reactants[key]) + values[0]-1] = Fraction(-1*values[1])

grid = np.array(t)

print(grid)

# grid = [[0 for i in range(test.len+1)] for j in range(id)]

for i in range(len(grid)):
    if grid[i][i].evl() == 0:
        for j in range(i+1, len(grid)):
            if grid[j][i] != 0:
                grid[[i, j]] = grid[[j, i]]
                break
    if grid[i][i].evl() == 0:
        print(grid)
        sys.exit('Error: division by zero/diagonal contains zero. The solution does not exist.')

# grid = [[0 for i in range(test.len+1)] for j in range(id)]
# +1 for the answer column, rest for the variables 

row = len(grid)
col = len(grid[0])

def gaussian_elimination(grid):
    global row, col
    for i in range(row-1):
        current = grid[i][i]
        for j in range(i+1, row):
            ratio = -1*grid[j][i]/current
            for k in range(col):
                assert type(grid[j][k]) is Fraction
                grid[j][k] += ratio*grid[i][k]

# def extract_answers(grid):
#     global row, col
#     answers = [1]
#     answers.append(grid[row-1][col-1]/grid[row-1][col-2])
#     for i in range(row-2, -1, -1): 
#         value_rn = grid[i][col-1] 
#         ptr = 0 
#         for j in range(row-i-1):
#             value_rn -= answers[ptr]*grid[i][col-2-j]
#             ptr += 1
#         answers.append(value_rn/grid[i][col-2-(row-i-1)])
#     return answers[::-1]

def extract_answersRev(grid): # assumption is bottom row has 2 non-zero values
    answers = [1]
    # answers.append(-1*(grid[len(grid)-1][len(grid[0])-2]/grid[len(grid)-1][len(grid[0])-3]))
    # 
    for i in range(row-1, -1, -1): 
        curr = Fraction(0)
        ptr = 0
        for j in range(col-2, -1, -1):
            
            print(grid[i][j])
            curr += answers[ptr]*grid[i][j]
            ptr += 1
    print(answers)
    return answers[::-1]

gaussian_elimination(grid)

def isBalanced(grid):
    for i in range(len(grid[0])-1):
        if grid[len(grid)-1][i].evl() != 0:
            return False
    return True

for line in grid:
    print(line)

if isBalanced(grid):
    print(test.reactionString)
else:
    extract_answersRev(grid)

# print(isBalanced(grid))

# answers = extract_answers(grid)
# print("Answers are:", answers)

# setting up equations to solve 
# each element in each reactant and product
# -> reactant_1a + reactant_2b + reactant_3c + reactant_4d + .... 
#           = count of 

# here, a,b,c,d... = coefficients in front of the ath, bth, cth, dth... reactant and product (count in each reactant and product)
# dimensions of grid = 
#       height -> # of distinct elements involved in the reaction 
#       width -> # of reactants + # of products