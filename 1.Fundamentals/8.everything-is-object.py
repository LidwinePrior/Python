# With Python, everything is object

txt = "hello, and welcome to my world."
capitalizeTxt = txt.capitalize()
print(capitalizeTxt) 


# create an immutable object with the class int.
x = 10 # Creating the int() instance
y = 10
print(id(x), id(y))
print(x is y) # comparing the types

# change the value of the variable x
x += 1
print(id(x), id(y))
print(x is y)

# create a mutable object with the List class.
person = ["James", "Bond", "007", "Secret agent"]
person2 = person
print(id(person), id(person))
# modify both lists
person += ["English"]
person2 += ["Man"]
print(id(person),id(person2))
print(person, person2)
# The changes affect both the variable person and the variable person2.