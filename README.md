# Balancing-Chemical-Equations-with-Linear-Algebra

### Table of Contents
1. [Description](#motivation-and-description-for-this-project)
2. [Try It Out Yourself!](#try-it-out-yourself)
 
### Description for this Project

This project aims to provide a way to balance chemical reactions using Python! Alongside its relevance to chemistry, this project also makes use of linear algebra, a fascinating branch of math. Now, coming to the functionality, everything beings when information is extracted from a particular set of products and reactants provided by the user via graphical input. Upon further manipulation, data extracted from the chemical equation provided is converted into sets of linear equations. Thus, having obtained a set of linear equations, the technique of Gaussian Elimination helps solve these equations in order to obtain the solution for a balanced chemical equation. Upon discovery of the appropriate coefficients to go in front of the reactants and products, these results are displayed to the user graphically!
 
### Try It Out Yourself!

After cloning the repository, you must first enter the folder containing
the cloned repository. If an IDE is being used, this can be done through
the IDE itself, however, if not, then the following commands can be used
to run the program through the terminal:  

for Linux and Mac:
```
  cd Dynamic-Programming-and-the-Periodic-Table
  pip3 install -r requirements.txt
  python3 main.py    
```

for Windows:
```
  cd Dynamic-Programming-and-the-Periodic-Table
  pip install -r requirements.txt
  python main.py
```

The program should then execute! Cheers!
