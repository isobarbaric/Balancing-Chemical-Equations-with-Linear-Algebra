
from parser import parser
from fraction import Fraction
from math import gcd
import numpy as np

class Reaction:

    def __init__(self, reactants, products):
        self.len = len(reactants.split('+')) + len(products.
        split('+'))
        self.reactantString = reactants 
        self.productString = products 
        self.reactants = parser(reactants)
        self.products = parser(products)
        self.possible = True
        self.grid = []
        self.answers = []
        self.build()
        if not self.possible:
            return 
        self.answers = self.extract_answers()
        
    def gaussian_elimination(self):
        row = len(self.grid)
        col = len(self.grid[0])
        for i in range(row-1):
            current = self.grid[i][i]
            for j in range(i+1, row):
                ratio = -1*self.grid[j][i]/current
                for k in range(col):
                    self.grid[j][k] += ratio*self.grid[i][k]

    def isBalanced(self):
        for i in range(len(self.grid[0])-1):
            if self.grid[len(self.grid)-1][i].evl() != 0:
                return False
        return True

    def extract_answers(self): 
        # assumption is bottom row has 2 non-zero values
        if self.isBalanced():
            rn = [1 for i in range(self.len)]
            return rn
        row = len(self.grid)
        col = len(self.grid[0])
        answers = [Fraction(1)]
        for i in range(row-1, -1, -1): 
            curr = Fraction(0)
            ptr = 0
            for j in range(col-2, i, -1):
                curr += answers[ptr]*self.grid[i][j]
                ptr += 1
            curr *= -1
            curr = curr/self.grid[i][i] 
            # overload this operator 
            answers.append(curr)
        commonDen = 1
        for i in range(len(answers)):
            commonDen = int((answers[i].den*commonDen)/gcd(commonDen, answers[i].den))
        answers = [commonDen*i for i in answers]
        return answers[::-1]

    def build(self):
        indexElements = dict()
        id = 0
        for element in self.reactants:
            if element not in indexElements.keys():
                indexElements[element] = id
                id += 1
        for element in self.products:
            if element not in indexElements.keys():
                indexElements[element] = id
                id += 1
        t = []
        for i in range(id):
            rn = []
            for j in range(self.len+1):
                rn.append(Fraction(0))
            t.append(rn)
        for key in indexElements.keys():
            for values in self.reactants[key]:
                t[indexElements[key]][values[0]-1] = Fraction(values[1])
            for values in self.products[key]:
                t[indexElements[key]][len(self.reactants[key]) + values[0]-1] = Fraction(-1*values[1])
        self.grid = np.array(t)
        for i in range(len(self.grid)):
            if self.grid[i][i].evl() == 0:
                for j in range(i+1, len(self.grid)):
                    if self.grid[j][i] != 0:
                        self.grid[[i, j]] = self.grid[[j, i]]
                        break
            if self.grid[i][i].evl() == 0:
                self.possible = False
                return 
        self.gaussian_elimination()