# Built-in Functions

# print() function which allows you to display text
print("Hello world")
# input() method which allows the user to enter text.
age = input("How old are you?")
print("Your are", age)
# native function to check it
print(type(age))

# Functions that allow cast : str(), int (), float(), etc...
age = input("How old are you?")
print("string :", age, type(age))

age = int(age) # Cast(convertir) from string to integer
print("integer :", age, type(age))

age =  float(age)# Cast from int to float
print("float :", age, type(age))

age =  str(age)# Cast from float to string
print("string :", age, type(age))

# The len() function allows us to know how many elements are in a list or string.
print(len("Hello Word"))

arr = ["one", "two"]
print(len(arr))
with open('test.txt', 'w') as file:
    file.write("Hello world\n")
    file.write("Your age is: " + str(age) + "\n")
    file.write("String representation of age: " + age + "\n")
    file.write("Length of 'Hello Word': " + str(len("Hello Word")) + "\n")
    file.write("Length of the list 'arr': " + str(len(arr)) + "\n")



# Drill
# python built-in-Functions.py

# 1. Create a variable countAlpha that contains the number of characters contained in the string "Hello world!"
countAlpha = len("hello World!")
print (countAlpha)

# 2. Create a variable countFloat and cast the variable countAlpha in float
countFloat = float(countAlpha)
print(countFloat, type(countFloat))

# 3. Round the variable pi value to -10² and save it in a variable roundPi.
import math
roundPi = round(math.pi, 2)
print(roundPi)

# 4. Create a variable reversedText which contains the character string "Hello world !" upside down.
reversedText = list("Hello world !"[::-1])
print(reversedText)
# result= ['!', ' ','d', 'l', 'r', 'o', 'W', ' ', 'o', 'l', 'l', 'e', 'h']

# or
# reversedText = "Hello world !"
# reversedWords = reversedText.split()
# resultReverse = [word[::-1] for word in reversedWords]
# print(resultReverse)
# resut = ['!', 'olleh', 'dlroW']

# 5. Create a variable age and ask the user to enter his age. Then display it and display its type.
age = input("How old are you?")
print(age, type(age))

# 6. Create a variable sortNum that contains the sorted num list.
num = [2, 8, 1, 4, 6, 3, 7]
sortNum = sorted(num)
print(sortNum)

# 7. Create a variable sumOfList which contains the sum of all the elements in the list num
num = [2, 8, 1, 4, 6, 3, 7] 
sumOfList = sum(num)
print(sumOfList)

# 8. Create a variable minValue that contains a minimum value of list num
num = [2, 8, 1, 4, 6, 3, 7] 
minValue = min(num)
print(minValue)

# 9. Create a variable maxValue that contains a maximum value of list num
num = [2, 8, 1, 4, 6, 3, 7] 
maxValue = max(num)
print(maxValue)

# 10. Find a function that will interpret the string of the variable calc
calc  = "1 + 2"
stringInterpret = eval(calc)

print (stringInterpret)

import unittest
 
class TestNotebook(unittest.TestCase):
 
    def test_countAlpha(self):
        self.assertEqual(countAlpha, 12)
    
    def test_countFloat(self):
        self.assertEqual(type(countFloat), type(float()))
        
    def test_pi(self):
        self.assertEqual(3.14, roundPi)
    
    def test_reversed(self):
        self.assertEqual(reversedText, ['!', ' ', 'd', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'H'])
    
    def test_age(self):
        self.assertEqual(type(age), type(str()))
        
    def test_sorted(self):
        self.assertEqual(sortNum, [1, 2, 3, 4, 6, 7, 8])
    
    def test_sum(self):
        self.assertEqual(sumOfList, 31)
    
    def test_min(self):
        self.assertEqual(minValue, 1)
    
    def test_max(self):
        self.assertEqual(maxValue, 8)
    
unittest.main(argv=[''], verbosity=2, exit=False)