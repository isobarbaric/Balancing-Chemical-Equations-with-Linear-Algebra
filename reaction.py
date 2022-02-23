
from parser import parser
from fraction import Fraction
from array import *
import sys

import numpy as np

# a = np.array([[4,3, 1],[5 ,7, 0],[9, 9, 3],[8, 2, 4]]) 
# print(a)
# a[[0, 2]] = a[[2, 0]]
# print(a)


class Reaction:

    def __init__(self, reactants, products):
        self.len = len(reactants.split('+') + products.split('+'))
        self.reactants = parser(reactants)
        self.products = parser(products)

a = "Ca2PhO2G4K3O5+H2Ca5O"

b = "CE25PO2GhZ33O53Ca5+H23Pa42P34"
# bug/edge case is when a new element appears in reactants that are not the first reactant in the list
# bruh

c = "CH4+O2"

d = "CO2+H2O"
d = "H2O+CO2"
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
        rn.append(0)
    t.append(rn)

for key in indexElements.keys():
    for values in test.reactants[key]:
        t[indexElements[key]][values[0]-1] = Fraction(values[1])
    for values in test.products[key]:
        t[indexElements[key]][len(test.reactants[key]) + values[0]-1] = Fraction(-1*values[1])

grid = np.array(t)

# grid = [[0 for i in range(test.len+1)] for j in range(id)]

print(grid)

print(indexElements)

row = len(grid)
col = len(grid[0])

for i in range(len(grid)):
    if grid[i][i].evl() == 0:
        print("sadge")
        for j in range(i+1, len(grid)):
            if grid[j][i] != 0:
                print("found")
                grid[[i, j]] = grid[[j, i]]
                break
    print(grid)
    if grid[i][i].evl() == 0:
        sys.exit('Error: division by zero. The solution does not exist.')

# grid = [[0 for i in range(test.len+1)] for j in range(id)]
# +1 for the answer column, rest for the variables 

def gaussian_elimination(grid):
    global row, col
    for i in range(row-1):
        current = grid[i][i]
        for j in range(i+1, row):
            ratio = -1*grid[j][i]/current
            print(ratio)
            for k in range(col):
                grid[j][k] += ratio*grid[i][k]

def extract_answers(grid):
    answers = []
    answers.append(grid[row-1][col-1]/grid[row-1][col-2])
    for i in range(row-2, -1, -1): 
        value_rn = grid[i][col-1] 
        ptr = 0 
        for j in range(row-i-1):
            value_rn -= answers[ptr]*grid[i][col-2-j]
            ptr += 1
        answers.append(value_rn/grid[i][col-2-(row-i-1)])
    return answers[::-1]

gaussian_elimination(grid)

for line in grid:
    print(line)

answers = extract_answers(grid)
print("Answers are:", answers)

# setting up equations to solve 
# each element in each reactant and product
# -> reactant_1a + reactant_2b + reactant_3c + reactant_4d + .... 
#           = count of 

# here, a,b,c,d... = coefficients in front of the ath, bth, cth, dth... reactant (count in each reactant)
# dimensions of grid = number of unique reactants