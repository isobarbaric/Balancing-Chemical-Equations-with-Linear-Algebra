
from tkinter import *
from answer import Answer

root = Tk() 
root.title('Balancing Chemical Equations')

response1 = Label(root, text='Enter the reactants here (separated by plus signs, spaces between reactants are allowed)')
response1.pack()

input_field_reactants = Entry(root)
input_field_reactants.pack() 

response2 = Label(root, text='Enter the products here (separated by plus signs, spaces between products are allowed)')
response2.pack()

input_field_products = Entry(root)
input_field_products.pack() 

a = ''
b = ''

def when_clicked():
    global a, b
    a = input_field_reactants.get().replace(' ', '')
    b = input_field_products.get().replace(' ', '')
    root.destroy()

submit_button = Button(root, text="Submit reactants and products", command=when_clicked)
submit_button.pack(side = TOP)

root.mainloop()

current_reaction = Answer(a, b)

root = Tk()
root.title('Balancing Chemical Equations')

display_balanced_eqn = Label(root, text=f"The balanced chemical equation is {current_reaction.answerString}")
display_balanced_eqn.pack()

root.mainloop()