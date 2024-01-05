# Quizz 1 - Python basics

# a) type
# Create a variable 'string' containing "toto" and a variable 'number' containing the number 10.

string = "toto"
number = 10

# Convert 'string' to unicode and 'number' in float

import re
# Using re.sub() and ord() method
# re (pour les expressions régulières) pour remplacer chaque caractère de la chaîne string par une séquence d'échappement Unicode. La fonction re.sub() est utilisée pour effectuer le remplacement.
# unicode_replacement est définie pour prendre un objet de correspondance (match) et retourner la séquence d'échappement Unicode pour ce caractère spécifique. La fonction ord(char) renvoie le point de code Unicode du caractère char.
def unicode_replacement(match):
    char = match.group()
    return r'\u{:04X}'.format(ord(char))

result = re.sub(r'.', unicode_replacement, string)
print(result, type(result))

float_number = float(number)
print(float_number, type(float_number))
# ce code prend un nombre, le convertit en float, puis prend une chaîne de caractères et la transforme en une nouvelle chaîne où chaque caractère est représenté par sa séquence d'échappement Unicode.

# Reverse the contents of the variables 'string' and 'number' (in 1 line).
reverse_string = string[::-1]
reverse_num = str(number)[::-1]
print(reverse_string)
print(reverse_num)

# b) List
# Create a list A containing the following integers: 1, 3, 2, 7, 4, 10, 46.
A = [1, 3, 2, 7, 4, 10, 46]
# Display the first 3 items in list A - in one line of code
print(A[0:3])
# Create a list B that contains only the 3rd, 4th and 5th elements of A . Your line of code should only contain 8 characters (not including spaces) - Check your result carefully!
B = A[2:5] #2 include 5 non-include
print(B)
# Concatenate lists A and B to form list C
C = A + B
print(C)

# Using the zip function, associate the values of A and B in the variable D
# liste1 = [1, 2, 3]
# liste2 = ['a', 'b', 'c']
# sortie -> [(1, 'a'), (2, 'b'), (3, 'c')]
D = list(zip(A, B))
print (D)

# Add the number 5 to list A
A.append(5)
print(A)

# Add a null element to the C list
C.append(None)
print(C)

# Write a function that takes as arguments a list 'lst' and an integer 'n' and returns the result of n concatenations of 'lst' with itself (e.g. lst=[1,2,3], n=2 --> [1,2,3,1,2,3]).
lst = [1,2,3]
n = 2

def arg(lst, n):
    result = lst * n
    return result
print(arg(lst, n))

# You want to make parameter 'n' optional and set its value to 2 by default. How do you do it?
def arg(lst, n = 2):
    result = lst * n
    return result
print(arg(lst))

# With a 'while' loop, print each element of the C list up to the null element.
index = 0
while C[index] is not None:
    print(C[index])
    index += 1
# Calculate, with a 'for' loop, the number of even integers present in the list A
count_even = 0
for num in A:
    if num % 2 == 0:
        count_even += 1
print("A: ", count_even)

# Rewrite the following expression with a multi-line 'for' loop
# C = [element for element in A if element %2 == 0]
C = []
for element in A:
    if element % 2 == 0:
        C.append(element)
print(C)

# Create a function that takes a string as input and returns the first single letter of the string
user_input = input("Enter a string: ")

def first_letter(input_str):
    words = input_str.split()
    letter = [word[0] for word in words]
    return letter

print(first_letter(user_input))



# c) Dictionaries

# Create a car dictionary with the following keys and values:
# key	value
# brand	Ford
# model	Mustang
# year	1964

car = {}
car['brand'] = "Ford"
car['model'] = "Mustang"
car['year'] = 1964

# Access to the "year" value
print(car['year'])

# Use a loop to display all the dictionary keys
for key in car.keys():
    print(key)

# Use a loop to display all the dictionary value
    
for value in car.values():
    print(value)

# Use a loop to display all the items in the dictionary.    
# Display also the index of each loop iteration (enumerate function).

   # utiliser fonction enumerate  pour obtenir l'indice et l'élément (sous forme de tuple).
    #séquence générée par la méthode items() du dico car. Cette méthode renvoie une vue d'ensemble des paires clé-valeur du dictionnaire.
    # chaque itération, index prend la valeur de l'indice actuel et (key, value) prend la valeur du tuple (clé, valeur) correspondant à l'élément du dictionnaire.

for index, (key, value) in enumerate(car.items()):
    print(f"Index: {index}, Key: {key}, Value: {value}")
# for avec enumerate est utilisée pour parcourir toutes les paires clé-valeur du dictionnaire car tout en affichant également l'indice de chaque paire.
    


# With the help of a comprehension dictionary create a dictionary with the following keys and values :
# key	value
# cle_1	dictionary 'car'
# cle_2	dictionary 'car'
# cle_3	dictionary 'car'
# exemple de dictionnaire comprehension :
# dict = {key:value for key, value in list_1, list_2}
    
# Définir le dictionnaire de base
dict = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# Créer un nouveau dictionnaire avec les clés 'cle_1', 'cle_2', 'cle_3' et des valeurs copies du dictionnaire de base
# f'cle_{i}' : insérer la valeur de i dans une chaîne de caractères en utilisant une f-string
# base_dict.copy() : Cette partie crée une copie du dictionnaire 
res = {f'cle_{i}': dict.copy() for i in range(1, 4)}
print(res)

# d) Functions
# Create a fibonacci function (fibonacci sequence: 0 1 1 2 3 5 8 13 ...)
# Ex : fibonacci(13) return [0,1,1,2,3,5,8,13]

def fibonacci(num):
    # deux premiers termes de la séquence Fibonacci
    sequence = [0, 1]
    # while  ajouter des termes à la séquence tant que la somme des deux derniers termes est inférieure ou égale au nombre donné num
    while sequence[-1] + sequence[-2] <= num:
        # À chaque itération, nous calculons le prochain terme en additionnant les deux derniers termes et l'ajoutons à la séquence.
        next = sequence[-1] + sequence[-2]
        sequence.append(next)
    return sequence
print(fibonacci(13))

# Execute your function (fibonacci(100) must be executed in less than 1 second)
print(fibonacci(100))

# Create a fibonacci function using a generator
# Ex : generate_fibonacci(10)
def generate_fibonacci(num):
    # Initialisation des deux premiers termes de la séquence
    a, b = 0, 1
    # Variable pour compter le nombre de termes générés
    count = 0

    while count < num:
        # Utilisation de yield pour retourner le terme actuel de la séquence
        yield a
        # Mise à jour des valeurs de a et b pour le prochain terme
        a, b = b, a + b
        # Incrémentation du compteur
        count += 1

# Utilisation du générateur pour obtenir les termes de la séquence
result = list(generate_fibonacci(5))
print(result)