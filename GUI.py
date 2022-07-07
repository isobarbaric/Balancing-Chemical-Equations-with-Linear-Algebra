
from tkinter import Tk, Label, Entry, Button, TOP
from chem_equation import BalancedChemicalEquation

class GUI:

    # constructor
    def __init__(self):
        pass

    # a public method through a call of whom the functionality of the GUI will work 
    def load(self):
        self.__loadInputMenu()

    # loading the GUI to interact with the user 
    def __loadInputMenu(self):
        # creating a GUI object using tkinter
        root = Tk() 

        # setting a title for the window 
        root.title('Balancing Chemical Equations')

        # prevent resizing in any dimensions, x or y
        root.resizable(False, False)  
        
        # determining the center of the screen to set the position for the GUI
        w_height, w_width = 150, 600
        s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
        x_coordinate = int((s_width/2) - (w_width/2))
        y_coordinate = int((s_height/2) - (w_height/2))

        # setting the location for the GUI object
        root.geometry("{}x{}+{}+{}".format(w_width, w_height, x_coordinate, y_coordinate))

        # adding a label to the window with instructions for what to enter
        reactant_prompt = Label(root, text='Enter the reactants here:')
        reactant_prompt.pack()

        # adding a text box to the window to collect user input
        inputField_reactants = Entry(root)
        inputField_reactants.pack() 

        # adding a label to the window with instructions for what to enter
        product_prompt = Label(root, text='Enter the products here:')
        product_prompt.pack()

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

            # initializing a Answer object using the two strings taken as input
            self.current_reaction = BalancedChemicalEquation(a, b)

            # ending the current GUI before creating a new one to display the balanced chemical equation
            root.destroy()

            self.__loadResultsMenu()

        # adding a submit button to the window to allow the user to 'submit' their input
        submit_button = Button(root, text="Submit reactants and products", command=when_clicked)
        submit_button.pack(side = TOP)

        # adding a label to the window with instructions for what to enter
        spec_label = Label(root, text='* all input should be separated by plus signs, spaces between are allowed')
        spec_label.pack()

        # running the main loop for the GUI object
        root.mainloop()


    def __loadResultsMenu(self):
        # creating a GUI object using tkinter
        root = Tk()

        # setting a title for the window 
        root.title('Balancing Chemical Equations')

        # prevent resizing in any dimensions, x or y
        root.resizable(False, False)  

        # determining the center of the screen to set the position for the GUI
        w_height, w_width = 100, 600
        s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
        x_coordinate = int((s_width/2) - (w_width/2))
        y_coordinate = int((s_height/2) - (w_height/2))

        # setting the location for the GUI object
        root.geometry("{}x{}+{}+{}".format(w_width, w_height, x_coordinate, y_coordinate))

        # adding a label to the window with the balanced chemical equation determined
        display_balanced_eqn = Label(root, text=f"\nThe balanced chemical equation is:\n\n{self.current_reaction.answerString}")
        display_balanced_eqn.pack()

        # running the main loop for the GUI object
        root.mainloop()
