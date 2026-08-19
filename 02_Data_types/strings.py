#string data type in python is used to store text (ssequence of characters)

name = "Maryam"
city = "Lahore"
language = "python programming"

print(name)
print(city)
print(language)

#More examples of strings...
first_name = "Maryam"
last_name = "Amin"
country = "Pakistan"

for character in country:
    print(character)

print("first_name:", first_name)
print("last_name:", last_name)
print("country:", country)

#checking the data type....
print("The type of first_name is:", type(first_name))
print("The type of last_name is:", type(last_name))
print("The type of country is:", type(country))

#using triple sinle quotes to define a string...
message = '''I am Maryam Amin.
I am a student of BSIT.
I am learning python programming language and
i want to become a python developer.'''
print(message)

for character in message:
    print(character)

#checking the indexing number of strings....
print(name[0])
print(name[1])
print(name[2])
print(name[3])

#Looping through a string...
for character in name:
    print(character)

    


