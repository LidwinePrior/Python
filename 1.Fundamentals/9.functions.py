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



# Scope of variables
#global variable = able to access 
myVar = "This is a global variable"
def printMyVar():
    print(myVar)
printMyVar()
#local variable = only on local function
def declare():
    varLocale = "This is local variable"
    print(varLocale)
declare()
# print(varLocale) => error

# if variable don't return a value, it's mean that's a PROCEDURE


# DRILL


# 1. Say hello
def hello (name = 'anonymous'):
    return 'hello {}!'.format(name)
print(hello('Lidwine'))
print(hello())


# 2. Count students
def sumOfStudents(students):
    # "(len(group) for group in students)" pour obtenir la longueur de chaque sous-liste (groupe d'étudiants)
    # sum() pour additionner toutes ces longueurs
    sumStudents = sum(len(group) for group in students)
    return sumStudents

students_list = [
    ["Jean", "Alice", "Edwige", "Peter", "James"],
    ["Redouane", "Justine", "Adrien", "Nicolas", "Pierre"]
]

result = sumOfStudents(students_list)
print(result)


# 3. is divisible?
# Create a function isDivisible(n, x, y) that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero digits.
def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0

print(is_divisible(12, 2, 6))


# 4. Abbreviate a Two Words Name
def abbrevName(name):
    # Utilise la méthode join() pour fusionner les initiales avec un point.
    # [0] sélectionne la première lettre de chaque mot.
    # upper() convertit la lettre en majuscule.
    # split() divise le nom en mots.
    return '.'.join([word[0].upper() for word in name.split()])

print(abbrevName('Lidwine Careme'))


# 5. Sum of positive
def positive_sum(numbers):
    # Variable pour stocker la somme des nombres positifs
    sum_positives = 0
    # Parcourir tous les nombres dans la liste
    for number in numbers:
        # Vérifier si le nombre est positif
        if number > 0:
            # Ajouter le nombre à la somme des positifs
            sum_positives += number
    return sum_positives

print(positive_sum([1, -4, 7, 12]))


# 6. Sum mixed array
arr = ['5', '0', 9, 3, 2, 1, '9', 6, 7]
def sum_mix(arr):
    # Convertire chaque élément de la liste en nombre (int) et additionne
    # génère une nouvelle liste avec tous les éléments de arr convertis en entiers.
    return sum(int(x) for x in arr)
print(sum_mix(arr))


# 7. Return the day
# convertir la saisie de l'utilisateur en un nombre entier.
num = int(input("Enter a number between 1 and 7: "))

def whatday(num):
    if num == 1:
        day = "Sunday"
        return day
    elif num == 2:
        day = "Monday"
        return day
    elif num == 3:
        day = "Tuesday"
        return day
    elif num == 4:
        day = "Wednesday"
        return day
    elif num == 5:
        day = "Thuesday"
        return day
    elif num == 6:
        day = "Friday"
        return day
    elif num == 7:
        day = "Saturday"
        return day
    else :
        return "Wrong, please enter a number between 1 and 7"
    
print(whatday(num))


# 8. Summation
def summation(num):
    # total initialisée à zéro pour stocker la somme
    total = 0
    # itérer sur les nombres de 1 à num inclus.
    for i in range(1, num +1):
        # À chaque itération, la valeur actuelle est ajoutée à la variable total
        total += i
    return total

print(summation(8))

# 9. If you can't sleep, just count sheep!!
def count_sheep(n):
    #result initialiser à 0 pour stocker la somme
    result = ""
    # itérer de 1 à n inclus
    for i in range(1, n+1):
        # ajouter chaque itération à la variable result
        result +="{} sheep ...".format(i)
    return result
print(count_sheep(5))


# 10. Student's final grade
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and exam < 90 and projects >= 5:
        return 90
    elif exam > 50 and exam < 75 and projects >= 2
        return 75
    else :
        return 0