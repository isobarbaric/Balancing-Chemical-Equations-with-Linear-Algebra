
from tkinter import Tk, Label, Entry, Button, TOP
from chemEquation import BalancedChemicalEquation

class GUI:

    # constructor
    def __init__(self):
        pass

    # loading the GUI to interact with the user 
    def load(self):
        # creating a GUI object using tkinter
        root = Tk() 

        # setting a title for the window 
        root.title('Balancing Chemical Equations')

        # adding a label to the window with instructions for what to enter
        response1 = Label(root, text='Enter the reactants here (separated by plus signs, spaces between reactants are allowed)')
        response1.pack()

        # adding a text box to the window to collect user input
        inputField_reactants = Entry(root)
        inputField_reactants.pack() 

        # adding a label to the window with instructions for what to enter
        response2 = Label(root, text='Enter the products here (separated by plus signs, spaces between products are allowed)')
        response2.pack()

        # adding a text box to the window to collect user input
        inputField_products = Entry(root)
        inputField_products.pack() 

        # declared two variable to store the chemical equations entered by the user
        a = ''
        b = ''

        # a method to deal with the action when the user pushes the submit button
        def when_clicked():
            nonlocal a, b

            # storing the contents of the textboxes involved in user input
            a = inputField_reactants.get().replace(' ', '')
            b = inputField_products.get().replace(' ', '')

            # ending the current GUI before creating a new one to display the balanced chemical equation
            root.destroy()

        # adding a submit button to the window to allow the user to 'submit' their input
        submit_button = Button(root, text="Submit reactants and products", command=when_clicked)
        submit_button.pack(side = TOP)

        # running the main loop for the GUI object
        root.mainloop()
 
        # initializing a Answer object using the two strings taken as input
        current_reaction = BalancedChemicalEquation(a, b)

        # creating a GUI object using tkinter
        root = Tk()

        # setting a title for the window 
        root.title('Balancing Chemical Equations')

        # adding a label to the window with the balanced chemical equation determined
        display_balanced_eqn = Label(root, text=f"The balanced chemical equation is {current_reaction.answerString}")
        display_balanced_eqn.pack()

       # running the main loop for the GUI object
        root.mainloop()
