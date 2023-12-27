#to run the code in anaconda powershell
# the command is: python basics-python-syntax.py  
#->go into the good file 
# cd BeCode
# cd Python
# cd drill
# and write the name of the file


# 1. Create a variable age that contains value 42
age = 42

# 2. Adds 10 to variable age
age += 10

# 3. Create a variable divAge and assign it the value of the age divided by 7 ( it must be an integer.)
divAge = age//7
print(divAge)

# 4. Create a variable textDiv that contains the character string "42 divided by 7 is equal 7".
textDiv = "{} divided by {} is equal {}" .format(age, divAge, divAge)
print(textDiv)

# 5. Create a variable restDiv that contains the rest of the variable age divided by 7
restDiv = age % 7
print(restDiv)

# 6. Create a variable expDiv that contains the value of restDiv exponent 3
expDiv = restDiv ** 3
print(expDiv)

# 7. Write a program that enters an integer and then displays the value entered and its type.
print("value: ", age, ", type: ", type(age))

# 8. Use variables to represent the price of materials.
milk = 0.45 * 2
cider = 3.85 * 3
flour = 0.9
butter = 0.77
nutella = 1.87
orderPrice = milk + cider + flour + butter + nutella

print(round(orderPrice, 2), "€")  #arrondi
#ou
print("{:.2f} €".format(orderPrice))  #formaté

# Create a variable allowanceMoney which has a value of 20 and then create an algorithm that calculates the available money by subtracting the price of the order.
allowanceMoney = 15
remaining_money = allowanceMoney - orderPrice
# Créer une variable message
message = ""

if remaining_money > 0:
    message = "You have spent {:.2f}€, you have {:.2f}€ left." .format(orderPrice, remaining_money)
elif remaining_money  < 0:
    #abs(remaining_money) pour obtenir la valeur absolue de la différence si elle est négative
    message = "Sorry you're missing {:.2f}€" .format(abs(remaining_money))
else:
    message ="You are broke!"

print(message)


# 9. Write a program that asks you to enter 2 values and displays the smallest of the 2 values
user_input1 = input("Enter an number: ")
user_input2 = input("a second one: ")

# Convert user inputs to floats
num1 = float(user_input1)
num2 = float(user_input2)

# Compare the numbers and print the smallest one
if num1 < num2:
    print("The smallest number is:", num1)
else:
    print("The smallest number is:", num2)


# 10. Write a script that asks you to enter 2 strings and displays the largest of the 2 strings (the one with the most characters).
def find_longest_word(word_list):
    longest_word= max(word_list, key=len)
    print (longest_word)

word_user_input1 = input("Enter a word: ")
word_user_input2 = input("An other one: ")
word_list = [word_user_input1, word_user_input2]
find_longest_word(word_list)
#or
# word_user_input1 = input("Enter a word: ")
# word_user_input2 = input("Enter another one: ")

# if len(word_user_input1) > len(word_user_input2):
#     print("The longest word is:", word_user_input1)
# elif len(word_user_input1) < len(word_user_input2):
#     print("The longest word is:", word_user_input2)
# else:
#     print("Both words have the same length.")




# 11. Write a script that converts euros into dollars.
# The program will start by asking the user to indicate with a character 'E' or '$' depending on the currency of the amount they are entering.
# Then the program will ask you to enter the amount and display the conversion.

# bibliothèque currencyconverter pour simplifier la conversion de devises
# with this command: pip install currencyconverter

from currency_converter import CurrencyConverter

# Fonction pour obtenir le taux de change en temps réel
def get_exchange_rate():
    c = CurrencyConverter()
     # Conversion d'1 euro en dollars
    exchange_rate = c.convert(1, 'EUR', 'USD')
    return exchange_rate

# Demander à l'utilisateur de choisir la devise
currency_choice = input("Choose currency ('E' for euros, '$' for dollars): ")
# Demander à l'utilisateur d'entrer le montant
amount = float(input("Enter the amount: "))

# Obtenir le taux de change en temps réel
exchange_rate = get_exchange_rate()

# Effectuer la conversion
if currency_choice.upper() == 'E':
    converted_amount = amount * exchange_rate
    print(f"{amount} euros is equal to {converted_amount:.2f} dollars.")
elif currency_choice == '$':
    converted_amount = amount / exchange_rate
    print(f"{amount} dollars is equal to {converted_amount:.2f} euros.")
else:
    print("Invalid currency choice. Please enter 'E' or '$'.")

#or
# Taux de change fixe
exchange_rate = 1.18

currency_choice = input("Choose currency ('E' for euros, '$' for dollars): ")

amount = float(input("Enter the amount: "))

if currency_choice.upper() == 'E':
    converted_amount = amount * exchange_rate
    print(f"{amount} euros is equal to {converted_amount:.2f} dollars.")
elif currency_choice == '$':
    converted_amount = amount / exchange_rate
    print(f"{amount} dollars is equal to {converted_amount:.2f} euros.")
else:
    print("Invalid currency choice. Please enter 'E' or '$'.")



# 12. Check if the variable name is in the studentsTuring list. (Without making a loop)
studentsTuring = ["Redouane", "Justine", "Ruben", "Edouard"]
name = "Julie"

if name in studentsTuring:
    print("You are at the turing's")
else:
    print("You are not part of the turing's")


# 13. Calculate the volume of a sphere using the formula (4π/3) x R³. The radius is 10.

# imports the math module to access the value of pi
import math
R = 10
volume =  (4 * math.pi / 3) * R**3
# f avant une chaîne de caractères indique que c'est une "formatted string". Les chaînes de format permettent d'incorporer des expressions Python à l'intérieur des chaînes en utilisant la syntaxe {}
print(f"The volume of the sphère with radius {R} is: {volume:.2f}")