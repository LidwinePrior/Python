# While

i = 1
while i <= 10:
    print(i)
    i += 1

while True:
    n = int(input("Give a integer > 0: "))
    print("You have provided", n)
    if n > 0:
        break
print("correct answer")

# For
# A "for" loop is used for iterating over a sequence: a list, a tuple, a dictionary, a set, a string

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
#result = 
# apple
# banana
# cherry
for x in "banana":
    print(x)
#result = 
# b
# a
# n
# a
# n
# a





# Range
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number

for i in range(10):
    print(i)
#result = 
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
    
for i in range(2**3):
    print(i)
# result = 
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
    
# With starting sprecified
for i in range(4,10):
    print(i)
# result = 
# 4
# 5
# 6
# 7
# 8
# 9
    
#whith step
for i in range(0,10,2):
    print(i)
# result = 
# 0
# 2
# 4
# 6
# 8
    



# Continue and Break
    
#continue
for i in range(4):
    print("Start of iteration", i)
    print("Hello")
    if i < 2:
        continue
    print("End of iteration", i)
print("After the loop")

#break
for i in range(10):
    print("Start of iteration", i)
    print("Hello")
    if i == 2:
        break
    print("End of iteration", i)
print("After the loop")




# Else
i = 1
while i < 10:
    print(i)
    i += 1
else:
    print('Finally finished!, i=', i)


for i in range(1, 10):
    print(i)
else:
    print('Finally finished!, i=', i)


# Drill

# 1. Display all students in the "students" list in alphabetical order
students = ["Merouane", "Baptiste", "Caroline", "Joe", "Sophie", "Nathan", "Raphaël", "Axel", "Mathieu"]      
sortedStudents = sorted(students)
for x in sortedStudents:
    print(x)

# 2. Display only those whose first name begins with the letter M
students = ["Merouane", "Baptiste", "Caroline", "Joe", "Sophie", "Nathan", "Raphaël", "Axel", "Mathieu"]      
for student in students:
    #vérifie si le premier caractère du prénom de l'étudiant est égal à 'M'
    if student[0] == 'M':
        print(student)

# 3. Display integers from 0 to 15 not included, using a "for"loop and the range() instruction.
for i in range(0, 15):
    print(i)

# 4. Use the "break" instruction to interrupt a "for" loop to display integers from 1 to 10 included, when the loop variable is 5
for i in range(1, 11):
    print(i)
    if i == 5:
        break

# 5. Use the "continue" instruction to modify a "for" loop to display intergers from 1 to 10 included, when the loop variable is 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# 6. Follow the instructions :
    
# display the last element using a negative indication.
listOfnum = [17, 38, 10, 25, 72]

# sort and display the list;
sortedList = sorted(listOfnum)
print(sortedList)

# add item 12 to the list and display the list;
listOfnum.append(12)
print(listOfnum)

# reverse and display the list;
reverseList = listOfnum[::-1]
print(reverseList)

# display the index of element 17;
for i in listOfnum:
    if i == 17:
        print(i)

# remove item 38 and display the list;
if 38 in listOfnum:
    listOfnum.pop(listOfnum.index(38))
print(listOfnum)

# display the sub-list of the 2nd to 3rd element;  
subList = listOfnum[1:3] # selects the elements from index 1 (inclusive) to index 3 (exclusive) 
print(subList)

# display the sub-list from the beginning to the 2nd element;
subList = listOfnum[:2] # selects the elements from the beginning up to the 2nd element (index 2 exclusive)
print(subList)

# display the sub-list of the 3rd element at the end of the list;
subList = listOfnum[2:] # selects the elements from index 2 (inclusive)
print(subList)

# display the complete sub-list of the list;
completeSubList = listOfnum[:] # selects all elements of the list
print(completeSubList)

# 7. Write an algorithm that asks the user to enter a number. Then make sure that your program displays all the numbers up to 0, for example, if the user enters the number 3, then your program will display something like this: 3,2,1,0
inputNumber = int(input ("please enter a number"))
while inputNumber >= 0: 
    print (inputNumber)
    inputNumber -= 1

# 8.The price is right ! Create a variable that will contain the number to be found. Then create an algorithm that will ask the user to find this price. If the user enters a number that is too high, he will have the sentence: "It's less". If he enters a number that is too low, he will have the sentence: "It's more". If the user finds the right price he will have the sentence: "Well done, you won".
rightPrice = 265
while True:
    askPrice = int(input("Find the right price to win! Please enter a price between 0 to 500: "))

    if askPrice < 265:
        print("It's more")
    elif askPrice > 265:
        print("It's less")
    else:
        break
print("Well done, you won")

# 9. Display all students with the sentence "NAME is a alumni. "
allStudents =  [["David", "Justine", "Valentin","Axel", "Redouane"], ["Julie", "Stéphane", "Mostapha", "Claudiu", "Son"]]
for group in allStudents:
    for student in group:
        print(f"{student} is an alumni.")

# 10. Display all elements. If the element is part of the first table display - "PHP is a backend language" - and if the element is part of the second language, display - "HTML is a Frontend language" ...
languages = [["PHP", "Java", "C#"], ["HTML", "CSS", "Javascript"]]
for backend_language in languages[0]:
    print(f'{backend_language} is a backend language')
for frontend_language in languages[1]:
    print(f'{frontend_language} is a backend language')