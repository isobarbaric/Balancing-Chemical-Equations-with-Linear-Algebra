
from parser import parser
from fraction import Fraction
from math import gcd
import numpy as np
import itertools
import sys

class Answer:
    def __init__(self, reactants, products):
        self.reactants = reactants.replace(' ', '')
        self.products = products.replace(' ', '')
        self.possible_answers = []
        self.answerValues = []
        self.answerString = ""
        self.tabulate()
        if len(self.answerValues) == 0:
            return
        ptr = 0
        for species in self.reactants.split('+'):
            if self.answerValues[ptr].evl() == 1:
                self.answerString += species
            else:
                self.answerString += str(self.answerValues[ptr]) + species
            ptr += 1
            self.answerString += '+'
        self.answerString = self.answerString[:-1]
        self.answerString += ' => '
        for species in self.products.split('+'):
            if self.answerValues[ptr].evl() == 1:
                self.answerString += species
            else:
                self.answerString += str(self.answerValues[ptr]) + species
            ptr += 1
            self.answerString += '+'
        self.answerString = self.answerString[:-1]

    def tabulate(self):
        for combination in list(itertools.permutations(self.products.split('+'))):
            rn = ""
            for item in combination:
                rn += item + '+'
            rn = rn[:-1]
            self.possible_answers.append(Reaction(self.reactants, rn))
        for potential_reaction in self.possible_answers:
            if potential_reaction.possible:
                self.answerValues = potential_reaction.answers
                break

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

# a = "C5H12 + O2"
# b = "CO2 + H2O"

# rn = Answer(a, b)
# print(rn.answerString)

# setting up equations to solve 
# each element in each reactant and product
# -> reactant_1a + reactant_2b + reactant_3c + reactant_4d + .... 
#           = count of 

# here, a,b,c,d... = coefficients in front of the ath, bth, cth, dth... reactant and product (count in each reactant and product)
# dimensions of grid = 
#       height -> # of distinct elements involved in the reaction 
#       width -> # of reactants + # of products