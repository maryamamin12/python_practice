name:str = "Maryam"
print(name)
father_name:str = "Amin_Ullha"
print(father_name)

# String Data Types in python
# boundries:
# 'string text' , "string text" , '''string text''', """string text"""

name:str = 'Maryam' # single_quote_string
print(name)
print(type(name))

message : str = "PIAIC Student Card \n father's Name"
print(message)

# convert any special character into simple character, place \ before character
message : str = 'PIAIC Student Card \n father\'s Name' # In single_quote_string
print(message)

name : str = "Maryam"
fname : str = "Amin"
education : str = "Matric in science"
age : str = 18

card : str = "PIAIC Student Card\nstudent Name: " + name +\
"\nage:" + str(age)+ "\n" +\
 "education: " + education

print(card)

print(7 + 8 + 2)
# "\" Line Cotinue
print(2 + \
      5 + \
        3)

# Define Multiple String """ """  ''' '''

name : str = "Maryam"
fname : str = "Amin"
education : str = "Matric in science"
age : str = 18
# f_string pyton

card : str = f"""
PIAIC Student Card
student Name: {name}
Father's Name: {fname}
Age: {age}
Education: {education}
"""
print(card)
# Single Triple Quotes (''')
card : str = f'''
PIAIC Student Card
student Name: {name}
Father's Name: {fname}
Age: {age}
Education: {education}
'''
print(card)
 
# Dir Functions.

[i for i in dir(str) if "__" not in i]

name : str = "maRYaM"
print(name.capitalize())
print(name.lower())
print(name.upper())

a = 7
b = 8
# {} place holder
#                    0          1         0 1      
"pakistan value a = {} and b = {}".format(a,b)


name : str = "Maryam"
fname : str = "Amin"
education : str = "Matric in science"
age : str = 18

card : str = """
PIAIC Student Card
student Name: {1}
Father's Name: {0}
Age: {3}
Education: {2}
""".format(fname, name, education, age)
#           0      1      2          3
print(card)


student_code : str = """
print("My name is Maryam")
a:int = 7
b:int = 8
print(a+b)
"""

exec(student_code)

a: list[str] = [i for i in dir(str) if "__" not in i]
print(a)
print(len(a))

name: str = "Maryam"
# variable-name.method()
print(name)
print(name.casefold())

# Lstrip Function

name: str = "         Maryam     "
print(name)
print(name.lstrip()) # lstrip remove the extra spaces the left sides.


name: str = "         Maryam     "
print(name)
print(name.rstrip()) # rstrip remove the extra spaces the right sides.

name: str = "Ada Lovelace"
print(name.upper())
print(name.lower())

# \n
# \t
# \b

print("Name:\t\t Maryam Amin")
print("Name:\n Maryam Amin")
print("Name:\b Maryam Amin")


nostarch_urlist:str = 'https://nostarch.com'
nostarch_urlist.removeprefix('https://')       # prefix function remove beginner