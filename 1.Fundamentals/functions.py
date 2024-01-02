# Functions


# rules to define a function in Python:
# Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).
# Any input parameters or arguments should be placed within these parentheses. 
# The code block within every function starts with a colon (:) and is indented
# L'instruction return quitte une fonction, en renvoyant éventuellement une expression à l'appelant

def hello():
    print("Hello and welcome")
    
hello()



# The parameters
def hello(name): # <- Parameter
    print("Hello {} and welcome".format(name))
    
hello("Lidwine") # <- Argument

def increaseMe(a):
    return a + 2

increaseMe(1)



# dictionary for the parameters
name = {}
name["firstName"] =  "Lidwine"
name["lastName"] = "Careme"

def hello(firstName, lastName):
    print("Hello {} {} and welcome".format(firstName, lastName)) 
    
hello(**name)



# A parameter is required
# possibility to assign a default value in case the user does not pass an argument
def hello(name = "Anonymous"): # <- Parametre
    print("Hello {} and welcome".format(name))
    
hello() # <- Not argument



# operator splat
def multiply(*elements): # Add "*" to indicate that the parameters are infinite
    # 1 comme valeur initiale, la fonction garantit que lorsqu'elle multiplie les éléments, la première multiplication utilise la valeur initiale de res (qui est 1) et n'altère donc pas le résultat attendu.
    res = 1
    for element in elements:
        res = res * element
    return res # 1 * 2 * 3 * 4 = 24
multiply(1,2,3,4)


# list as a parameter
# prend un liste en paramètre
def doubleStuff(aList):
    # itère sur chaque position (indice) de la liste 
    for position in range(len(aList)):
        # À chaque itération de la boucle, l'élément à la position actuelle est multiplié par 2
        aList[position] = 2 * aList[position]

things = [2, 5, 9]
print(things)
# quand fonction est appelée, modifie la liste "things" en doublant chaque élément
doubleStuff(things)
print(things) # [4, 10, 18].

