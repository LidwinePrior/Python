# Conditions


#indentation!!!!!
age = 23

if age >= 18:
    print("You are an adult!")
elif age == 17:
    print("You are one year short of being an adult!")
else:
    print("Come back later!")



# Conditions & Logical operators
student1 = "John"
student2 = "Eric"

if student1 == "John" or student2 == "Eric":
    print("Your name is either John or Eric")
else:
    print("Welcome Anonymous")


# "in" opérator
# The "in" operator could be used to check if a specified object exists within an iterable object container, such as a list
name = "Valérian"
coach = ["Valérian", "Ludovic"]

if name in coach:
    print("You are coach!")
else:
    print("You are not coach!")


#  "not" operator
# Using "not" before a boolean expression inverts it
name = "Ayaan"
if name not in ["Valérian", "Ludovic"]:
    print("You are not coach")
else:
    print("You are coach")


# 'is' operator
# Contrairement à l'opérateur double égal "==", l'opérateur "is" ne correspond pas aux valeurs des variables, mais aux instances elles-mêmes.
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)