
from reaction import Reaction
import itertools

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
        print(self.answerValues)
        ptr = 0
        for species in self.answerValues[0].split('+'):
            if self.answerValues[2][ptr].evl() == 1:
                self.answerString += species
            else:
                self.answerString += str(self.answerValues[2][ptr]) + species
            ptr += 1
            self.answerString += '+'
        self.answerString = self.answerString[:-1]
        self.answerString += ' => '
        for species in self.answerValues[1].split('+'):
            if self.answerValues[2][ptr].evl() == 1:
                self.answerString += species
            else:
                self.answerString += str(self.answerValues[2][ptr]) + species
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
                self.answerValues = [potential_reaction.reactantString, potential_reaction.productString, potential_reaction.answers]
                break