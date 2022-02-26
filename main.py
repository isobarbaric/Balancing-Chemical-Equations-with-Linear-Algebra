
from tkinter import *
from answer import Answer

root = Tk() 
root.title('Balancing Chemical Equations')

input_field_reactants = Entry(root)
input_field_reactants.pack() 

input_field_products = Entry(root)
input_field_products.pack() 

response = Label(root, text='Waiting for input...press submit once ready')
response.pack()

a = ''
b = ''

def when_clicked():
    global a, b
    try:
        a = input_field_reactants.get().replace(' ', '')
        b = input_field_products.get().replace(' ', '')
        response.config(text = "Input processed successfully...please standby")
        root.destroy()
    except ValueError:
        num_attempts += 1
        response.config(text = f"Invalid input, please correct input format and press submit again. Number of invalid attempts: {num_attempts}")  

submit_button = Button(root, text="Submit coefficients", command=when_clicked)
submit_button.pack()

root.mainloop()

current_reaction = Answer(a, b)

root = Tk()
root.title('Balancing Chemical Equations')

display_balanced_eqn = Label(root, text=f"The balanced chemical equation is {current_reaction.answerString}")
display_balanced_eqn.pack()

root.mainloop()