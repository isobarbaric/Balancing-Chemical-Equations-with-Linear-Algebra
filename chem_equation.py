
from fraction import Fraction

import math
import numpy as np
import itertools

class ChemicalEquation:

    # constructor
    def __init__(self, reactants, products):
        # self.reactants and self.products maintain a copy of the reactants and products string 
        self.reactants = reactants 
        self.products = products 

        # self.len keeps track of the total number of reactants and products
        self.len = len(self.reactants.split('+')) + len(self.products.split('+'))
        
        # these two variables maintain a dictionary containing the count of each element per reactant and product using the parser() function 
        self.parsed_reactants = self.parser(self.reactants)
        self.parsed_products = self.parser(self.products)
        
        # this boolean variable keeps track of whether an answer was found for the balancing of this equation or not
        self.possible = True
        
        # this variable maintains a grid that contains a matrix to solve for the coefficients of the balanced equation
        self.grid = []

        # in the case that this equation is balance-able, this variable keeps track of the coefficients found for each reactant and product
        self.answers = []

        # the build() function builds a matrix using the information from self.parsed_reactants and self.parsed_products
        self.build()

        # in the build() function, if the equation is not balance-able, then the self.possible boolean variable is set to false to indicate this; if it is not possible, it is misleading to generate a list of answers and hence this is skipped using 'return'
        if not self.possible:
            return 

        # if the equation is balance-able, then the coefficients are extracted using the extract_answers() method and stored in the self.answers list
        self.answers = self.extract_answers()
    
    # gaussian elimination operates on the matrix (self.grid) created by build() in order to reduce it to row-echelon form
    def gaussian_elimination(self):
        # row, col store the dimensions of the grid over which to iterate
        row = len(self.grid)
        col = len(self.grid[0])
        
        # this is the main part of the algorithm that performs the reduction procedure
        for i in range(row-1):
            current = self.grid[i][i]
            for j in range(i+1, row):
                ratio = -1*self.grid[j][i]/current
                for k in range(col):
                    self.grid[j][k] += ratio*self.grid[i][k]

    # if the last row in the matrix is entirely just composed of 0s, this means that the equation is already balanced - this function checks for this 
    def is_balanced(self):

        # if at any point in the last row, a non-zero number occurs, the function returns False based on the heuristic mentioned 
        for i in range(len(self.grid[0])-1):
            if self.grid[len(self.grid)-1][i].eval() != 0:
                return False

        # if execution of the algorithm falls through to here, this means that the entire row is just 0s
        return True

    # the extract_answers() method takes the reduced matrix and extracts the individual coefficient for each reactant or product
    def extract_answers(self): 
        # for the edge case for when the equation is already balanced, the self.is_balanced() method determines this 
        if self.is_balanced():
            # if the equation is balanced, then the equation is left unchanged and coefficients of 1 are passed to a list and returned
            rn = [1 for i in range(self.len)]
            return rn

        # row, col store the dimensions of the grid over which to iterate        
        row = len(self.grid)
        col = len(self.grid[0])

        # the answers list will store the coefficients found and will be returned and ultimately assigned to self.answers
        answers = [Fraction(1)]

        # this iterates through the reduced matrix and extracts the coefficients for each reactant as per the results of gaussian elimination
        for i in range(row-1, -1, -1): 
            curr = Fraction(0)
            ptr = 0
            for j in range(col-2, i, -1):
                curr += answers[ptr]*self.grid[i][j]
                ptr += 1
            curr /= -1*self.grid[i][i] 
            answers.append(curr)

        # to get integral coefficients, the lcm of the denominators is found and will ultimately be multipled by each currently fractional coefficient
        common_den = 1
        for i in range(len(answers)):
            common_den = int((answers[i].den*common_den)/math.gcd(common_den, answers[i].den))

        # now that the common denominator as been found, all of the elements are multiplied by this common denominator using list comprehension to obtain integral coefficients
        answers = [common_den*i for i in answers]
        
        # the coefficients generated are generated from back to front and hence they are returned in a reversed order
        return answers[::-1]

    # this function creates a matrix using information stored in the chemical equation 
    def build(self):
        # this dictionary maintains the unique ID assigned to each distinct
        index_elements = dict()
        
        # this variable keeps track of the unique ID assigned to each distinct element and will be used to numerically assign IDs
        id = 0
        
        # unique IDs are assigned to each element and these values are recorded in the indexElements dictionary
        for element in self.parsed_reactants:
            if element not in index_elements.keys():
                index_elements[element] = id
                id += 1

        # note that the same procedure as above is not performed for the products as it is known that for a valid chemical equation, the elements on either side are the same - this is not a nuclear reaction

        # t is a list that will be used to create the matrix (self.grid)   
        t = []
        for i in range(id):
            rn = []
            for j in range(self.len+1):
                # passing in values of 0 as dummy initializing values 
                rn.append(Fraction(0))
            t.append(rn)
        
        # using the information contained in the grid and putting these values into the grid at their specied location using the IDs initialized and 
        for key in index_elements.keys():
            for values in self.parsed_reactants[key]:
                t[index_elements[key]][values[0]-1] = Fraction(values[1])
            for values in self.parsed_products[key]:
                t[index_elements[key]][len(self.parsed_reactants[key]) + values[0]-1] = Fraction(-1*values[1])
        self.grid = np.array(t)
        
        # this for loop checks to see to ensure that the diagonal going from the top-left to the bottom-right does not contain any zeroes - if it does, it will attempt to swap this row with future rows
        for i in range(len(self.grid)):
            # checking to see if the diagonal contains a 0, if it is, swapping will be attempted inside the if statement
            if self.grid[i][i].eval() == 0:
                # iterating through the subsequent rows to check whether the 
                for j in range(i+1, len(self.grid)):
                    # if a value is found in a subsequent row at the same x-location, then a swap is performed and execution continues 
                    if self.grid[j][i] != 0:
                        self.grid[[i, j]] = self.grid[[j, i]]
                        break

            # if after attempts to swap, the current value in question is still on the diagonal (a swap was not possible), the chemical equation is not balance-able as the matrix cannot be solved and the self.possible boolean variable is set to False and a 'return' statement is used to prevent gaussian elimination from being performed
            if self.grid[i][i].eval() == 0:
                self.possible = False
                return 
        
        # if the grid's diagonal does not contain any 0s and the function falls through to here, then gaussian elimination is performed on the grid
        self.gaussian_elimination()

    # the parser function goes through the reactants and products and identifies the counts for each particular element
    def parser(self, one_side_chemical_equation):
        species = oneSideChemicalEquation.split('+')
        cnt_char = dict()
        iterNum = 1
        for entity in species:
            elements = []
            counts = []
            ongoing = False
            i = 0
            cnt_l = dict()
            while i < len(entity):
                if entity[i].isnumeric():
                    cnt = ''
                    end = len(entity)
                    for j in range(i, len(entity)):
                        if not entity[j].isnumeric():
                            end = j
                            break
                        cnt += str(entity[j])
                    counts.append(int(cnt))
                    i = end
                    ongoing = False
                else:
                    if ongoing:
                        if entity[i].isupper():
                            elements.append(entity[i])
                            counts.append(1)
                        else:
                            elements[-1] += entity[i]
                    else:  
                        elements.append(entity[i])
                        ongoing = True
                    i += 1
            if ongoing:
                counts.append(1) 
            for i in range(len(elements)):
                if elements[i] not in cnt_l.keys():
                    cnt_l[elements[i]] = 0
                cnt_l[elements[i]] += counts[i]
            for key in cnt_l.keys():
                if key not in cnt_char.keys():
                    cnt_char[key] = []
                cnt_char[key].append([iterNum, cnt_l[key]])
            iterNum += 1
        for key in cnt_char.keys():
            for i in range(1, len(species)+1):
                found = False
                for j in range(len(cnt_char[key])):
                    if (cnt_char[key][j][0] == i):
                        found = True
                if not found:
                    cnt_char[key].append([i, 0])
            cnt_char[key].sort()
        return cnt_char

class BalancedChemicalEquation:

    # constructor
    def __init__(self, reactants, products):
        # creating a reactants attribute to store the reactants provided
        self.reactants = reactants.replace(' ', '')

        # creating a reactants attribute to store the reactants provided
        self.products = products.replace(' ', '')
        
        # creating a list to store possible answers
        self.possible_answers = []

        # creating variables to store the coefficients associated with the balancing process
        self.answer_values = []
        self.answer_string = ""
        
        # calling the tabulate method to determine an answer to the balancing of the given chemical equation (reactants and products)
        self.tabulate()

        # if there are no solutions to the given chemical equation, then 
        if len(self.answer_values) == 0:
            return

        # calling the determine method to get the individual coefficients in the balanced chemical equation
        self.determine()

    # determining the configuration of the balanced reaction
    def tabulate(self):
        # looping through permutations of the 
        for combination in list(itertools.permutations(self.products.split('+'))):

            # converting the permutation to a string containing the reactants 
            rn = ""
            for item in combination:
                rn += item + '+'
            
            # getting rid of the final (and extraneous) plus sign
            rn = rn[:-1]
            
            # appending a Reaction object to the possible_answers attribute
            self.possible_answers.append(ChemicalEquation(self.reactants, rn))

        # looping through the possible reactions in the possible_answers attribute to see whether the 
        for potential_reaction in self.possible_answers:
            if potential_reaction.possible:
                self.answer_values = [potential_reaction.reactants, potential_reaction.products, potential_reaction.answers]
                break

    # determining the coefficients of each of the reactants and products in the balanced chemical equation
    def determine(self):
        ptr = 0
        
        # looping through the reactants and adding them to answer_string
        for species in self.answer_values[0].split('+'):
            if self.answer_values[2][ptr].eval() == 1:
                self.answer_string += species
            else:
                self.answer_string += str(self.answer_values[2][ptr]) + species
            ptr += 1
            self.answer_string += ' + '

        # removing the extraneous plus sign in the string so far
        self.answer_string = self.answer_string[:-2]
        
        # adding an arrow between the reactants and products
        self.answer_string += ' -> '

        # looping through the products and adding them to answer_string
        for species in self.answer_values[1].split('+'):
            if self.answer_values[2][ptr].eval() == 1:
                self.answer_string += species
            else:
                self.answer_string += str(self.answer_values[2][ptr]) + species
            ptr += 1
            self.answer_string += ' + '
        
        # removing the extraneous plus sign in the string at the end
        self.answer_string = self.answer_string[:-2]
    
