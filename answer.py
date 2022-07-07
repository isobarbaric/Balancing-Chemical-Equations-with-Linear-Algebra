
from chem_equation import ChemicalEquation
import itertools

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
        self.answerValues = []
        self.answerString = ""
        
        # calling the tabulate method to determine an answer to the balancing of the given chemical equation (reactants and products)
        self.tabulate()

        # if there are no solutions to the given chemical equation, then 
        if len(self.answerValues) == 0:
            return

        # calling the determine method to get the individual coefficients in the balanced chemical equation
        self.determine()

    def tabulate(self):
        # looping through permutations of the products of the reaction
        for combination in list(itertools.permutations(self.products.split('+'))):

            # converting the permutation to a string containing the reactants 
            rn = ""
            for item in combination:
                rn += item + '+'
            
            # getting rid of the final (and extraneous) plus sign
            rn = rn[:-1]
            
            # appending a ChemicalEquation object to the possible_answers attribute
            self.possible_answers.append(ChemicalEquation(self.reactants, rn))

        # looping through the possible reactions in the possible_answers attribute to see whether the 
        for potential_reaction in self.possible_answers:

            if potential_reaction.possible:

                self.answerValues = [potential_reaction.reactants, potential_reaction.products, potential_reaction.answers]
                break

    def determine(self):
        print(self.answerValues)
        ptr = 0
        for species in self.answerValues[0].split('+'):
            if self.answerValues[2][ptr].eval() == 1:
                self.answerString += species
            else:
                self.answerString += str(self.answerValues[2][ptr]) + species
            ptr += 1
            self.answerString += '+'
        self.answerString = self.answerString[:-2]
        self.answerString += '='
        for species in self.answerValues[1].split('+'):
            if self.answerValues[2][ptr].eval() == 1:
                self.answerString += species
            else:
                self.answerString += str(self.answerValues[2][ptr]) + species
            ptr += 1
            self.answerString += '+'
        self.answerString = self.answerString[:-2]
