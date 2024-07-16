# Python divides the operators in the following groups:

# Arithmetic operators

a : int = 7
b : int = 8
print(a + b) # Addition
print(a - b) # Subtraction
print(a * b) # Multiplication
print(a / b) # Dibision
print(a % b) # Modulus
print(a ** b) # Exponention
print(a //b) # Floor Division

print(2 ** 2)
print(2 ** 3)

print(12 / 3)
print(14 / 3)
print(14 // 3)

# Python Assignment Operators
# +=, -=, *=, /=,........
a :int = 7
b :int = 3
print(a)   # old method
a += 2
print(a)
a *= 3
print(a)

# Python Comparison Operators
# ==, !=, >, <, >=, <=
a :int = 12
b :int = 11
print(a == b)

a :int = 11
b :int = 11
print(a == b)

a :int = 12
b :int = 11
print(a != b)
print(13 !=22)

a :int = 14
b :int = 16
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Python Logical Operators
# and, or, not operator
# and = lazmi
# or = optional
#1          2       3       4
True and True and True and True
True and False and True and True
print(True and True and True and True)
print(True and True and True and True)

#1          2       3       4
True or True or True or True
True or False or True or True
print(True or True or True or True)
print(True or True or True or True)
not True

name: str = "Maryam"
print(not name=="Maryam")

# Python Identity Operators
# is, is not operator
x : str = 'abc'
z : str = 'abc'
print(id(x))
print(id(z))

x : str = 'abc'
z : str = 'xyz'
print(id(x))
print(id(z))
print(x is z)
print(x is not z)

# Python Membership Operators
# in, not in operator

name: list[str] = [chr(i) for i in range(65,91)]
print(name)
print("D" in name)

x = ["bnana", "apple", "orange"]
print(x)
print("bnana" in x)
print("peach" not in x)

name: list[str] = [chr(i) for i in range(65,91)]
print(name)
print("pakistan" in name)


name : list[str] = ['maryam', 'rimsha', 'amina']
uinput : str = input("Enter your name")
print(uinput in name)
print(uinput not in name)

# Operator Precedence
# PEMDAS 
print(3 + 2 - 2 * 4 / 2 + 2)
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)

# Underscore in Number
universe_age:int = 14_000_000_000
print(universe_age)

a , b , c = 'Maryam', 7, 3.0
print(a)
print(b)
print(c)


a , b , c = ['Maryam', 7, 3.0]
print(*a, b, c)

"""
asdf
asd
f
"""
print("hello")
import this