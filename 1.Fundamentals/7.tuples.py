# Lists, Tuples and dictionaries

# List
myList = ["a","b","c", "d"]
print(myList[0]) # a
print(myList[:2]) # ['a', 'b']
print(myList[::-1]) # ['d', 'c', 'b', 'a']

myList = myList * 5 
print(myList) 
# ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']

myList.append("Add Text")
print(myList) 
# ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'Add Text']

var = "Hello, i am a variable that contains String values"
otherList = [193.45, "Hello", ["Inception list", "Two elements"], 89, var]
print(otherList) 
# [193.45, 'Hello', ['Inception list', 'Two elements'], 89, 'Hello, i am a variable that contains String values']

x = [1, 2, 3, 4]
y = [4, 5, 1, 0]
x.extend(y)
print(x)
# [1, 2, 3, 4, 4, 5, 1, 0]

# OR 
x = [1, 2, 3, 4]
y = [4, 5, 1, 0]
xy = x + y
print(xy)
# [1, 2, 3, 4, 4, 5, 1, 0]


# Tuples
#  cannot be modified
# tupleExample = ("Moriarty", "Sherlock", "Watson")
# tupleExample.append("Lestrade")
# error => AttributeError: 'tuple' object has no attribute 'append'


# Dictionaries
# associative array
# they are editable like list
# access any of them using a specific index called a key
# can be of any type
# indexes will be strings of characters, unlike lists

heroes = {}
heroes["Batman"] = "Bruce Wayne"
heroes["Superman"] = "Clark Kent"
print(heroes) #{'Batman': 'Bruce Wayne', 'Superman': 'Clark Kent'}
# Batman is the key, Bruce Wayne is the value
print(heroes["Batman"]) # Bruce Wayne
# create a new key-value pair.
heroes["Spiderman"] = "Peter Parker"
print(heroes) #{'Batman': 'Bruce Wayne', 'Superman': 'Clark Kent', 'Spiderman': 'Peter Parker'}


# Drill

# 1. Choose 5 words from the English language and create dictionaries that associates each of these words with its French translation.
words = {}
words["world"] = "monde"
words["number"] = "nombre"
words["display"] = "afficher"
words["remove"] = "retirer"
words["add"] = "ajouter"
print(words)

# 2. Add an entry to the dictionary of the previous question (a new word and its definition)
words["happy"] = "content"
print(words)

# 3. How would you cut the following string at each space and put it in a list:
sentence = "I am the master of the world"
splitSentence = sentence.split()
listWords= [splitSentence]
print (listWords)

# 4. Transform this string "The_universal_number_is_42" by removing the underscores: "The universal number is 42"
universalNumber = "The_universal_number_is_42"
result = universalNumber.replace('_', ' ')
print(result)

# 5. Display only values of this dictionary.
heroes = {"Superman" : "Clark kent", "Batman" : "Bruce Wayne", "Spiderman" : "Tony Parker"}
for value in heroes.values():
    print(value)

# 6. Display only keys of this dictionary.
heroes = {"Superman" : "Clark kent", "Batman" : "Bruce Wayne", "Spiderman" : "Tony Parker"}
for key in heroes.keys():
    print(key)

# 7. Replace the value of "Spiderman" by "Peter Parker"
heroes = {"Superman" : "Clark kent", "Batman" : "Bruce Wayne", "Spiderman" : "Tony Parker"}
heroes['Spiderman'] = "Peter Parker"
print(heroes)

# 8. Create a dictionary to build the price base of the products corresponding to the following table:
price = {}
price['Laser sword'] = 229.0
price['Mitendo DX'] = 127.30
price['Linux cushion'] = 74.50
price['Goldorak briefs'] = 29.90
price['Nextpresso station'] = 184.60
print(price['Laser sword'])
#or
price = {
    'Laser sword': 229.0,
    'Mitendo DX': 127.30,
    'Linux cushion': 74.50,
    'Goldorak briefs': 29.90,
    'Nextpresso station': 184.60
}
print(price['Laser sword'])

# 9. Calculate the total price of the items of the dictionary
totalPrice = sum(price.values())
print(totalPrice)

#10. Remove one of the articles from the dictionary
price.pop('Laser sword')
print(price)