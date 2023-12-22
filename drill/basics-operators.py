# Arithmetic operators

a = 10
b = 20

# Addition
add = a + b

print(add)


# Substraction
sub = b - a

print(sub)

# Multiplication
multi = a * b

print(multi)

# Division
# Note that in this case, python returns a float.
div = b / a

print(div)

# Floor division
# To obtain an integer, you can use the floor division operator.
floorDiv = b // a

print(floorDiv)

# Modulus
# To obtain the rest of a division.
modulus = b % a

print("modulus :", modulus)

modulus2 = 21 % 2

print("modulus2 :", modulus2)

# Exponent
exp = a**2

print(exp)






# Comparison Operators

# Equals
print(a==b)
print(a==10)


# Not Equals
print(a!=b)
print(a!=10)

# Not equals but <> has now been removed in Python 3
# print(a <> b)  =>error
# print(a <> 10)  =>error

# Bigger than
print(a>b)
print(b>a)

# Bigger or equal than
print(a>=b)
print(b>=a)

# Smaller than
print(a>b)
print(b>a)

#  Smaller or equal than
print(a>=b)
print(b>=a)





# Assignment Operators


# Add AND
a = 10
name = "Alan Turing"
print(a)
print(name)
a +=10
name += " is a good mathematician"
print(a)
print(name)
# !!! we can only add variables of the same type
# name += a  =>error


# Subtract AND
a = 20
a -= 10
print(a)

# This operator does not work with strings, unlike the += operator
# name -="Alan Turing" => error


# Multiply AND
# This operator works with strings.
a = 10
a *= 10
print(a)

text = "Alan Turing"
text *= 10
print(text)


# Divide AND
# This operator does not works with character strings
a = 100
a /= 10
print(a)


# Modulus AND
# This operator does not works with character strings.
a = 100
a %= 3
print(a)


# Exponent AND
# This operator does not works with character strings.
a = 2 
a **= 3 # ( 2 * 2 * 2)
print(a)


# Floor Division AND
# This operator does not works with character strings.
a = 20
a //= 3
print(a)