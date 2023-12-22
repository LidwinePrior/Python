#introduction


first_name = "Lidwine" #String
last_name = "Careme" #String
age = 30  # Integer
weigth = 65.5 # Float
double_agent = True # Boolean => True and False are written with the first letter uppercase.
login = "007" # String
agent = [first_name, last_name, age, weigth, double_agent, login] # List => list is like an array, but you can store values of different types.
text = "My name is {}, {} {}." .format(last_name, first_name, last_name)

print ("My name is ", first_name)
print (text)
print(agent)

print(first_name, type(first_name))
print(last_name, type(last_name))
print(age, type(age))
print(weigth, type(weigth))
print(agent, type(agent))







# drill variables data types

#1. Create a variable name that contains the value "Alan Turing".

name = "Alan Turing"


#2. Create a variable age that contains the value 42.

age = 42

#3. Create a person variable that contains a list with the following values name, age and "mathematician"

person = [name, age, "mathematician"]

#4. Create a variable text that contains "Hello, my name is Alan Turing and i am 42 years old and i am a mathematician".
# Use the format method and the variable person to do this.

text = "Hello, my name is {} and i am {} years old and i am a {}." .format(person[0], person[1], person[2])

#5. Create a variable typeAge that contains type of variable age.

typeAge = type(age)


#testing code
import unittest
 
class TestNotebook(unittest.TestCase):
 
    def test_name(self):
        self.assertEqual(name, "Alan Turing")
    
    def test_age(self):
        self.assertEqual(age, 42)
    
    def test_person(self):
        self.assertEqual(person,["Alan Turing", 42, "mathematician"])
    
    def test_text(self):
        self.assertEqual(text,"Hello, my name is Alan Turing and i am 42 years old and i am a mathematician.")
        
    def test_type(self):
        self.assertEqual(typeAge,type(int()))
    

unittest.main(argv=[''], verbosity=2, exit=False)