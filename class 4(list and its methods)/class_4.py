# Python Lists
name1: str = "Maryam"
name2: str = "Rimsha"
name3: str = "Bilal"
print(name1)
print(name2) # Old Way
print(name3)

# List...
# * dynamic length
# * hetrogenous data types (Multiple type)
# * idex
#     * postive 0 to n-1
#     * negtaive -1 to length
# * Slicing
#     * variable 'name[start:end:step]'
#     * start : int = include
#     * end : int = n-1
#     * step : int = sequence

#  ->       0          1          3     that is called index number (postive)
names = ["Maryam", "Rimsha", "Bilal"]
#  <-       -3        =2         -1      (negtive)
print(names[0])
print(names[-3])
print(names[-2])

mylist = ["apple", "cherry", "peach"]
print(mylist)
# ->                 0           2           3
names: list[any] = ["Qasim", "sir zia", "sir Inam"]
# <-                  -1       -2            -3
print(type(names))
print(type(names[-2]))
print(f'Founder of PIAIC {names[-3].upper()}')

character : list[str] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") # that is called Iteration
print(character)

# default slicing go from left to right

#                         0    1     2     3   4    5    6                                                                                            25
character : list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','z']
#                         -26  -25   -24                                                                                                          -2  -1
print(character[0:2]) # 0= include: index 2-1 = 1
print(character[5:9])
print(character[:3])  # not pass any number = all
print(character[-26:-24]) # 0= include: index -24-1 = 1

character : list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print(character[::]) # its mean all character includes
print(character[::2]) # that is called sequence
print(character[::-1]) # reverse <-

# List Methods
#                     0           1      2      3    4
names : list[any] = ["Maryam", "Ali", "Qasim", 20, True]
#                     -5         -4      -3    -2   -1
print(names)
print(names[3])
print(names[-3])
names[0] = "Maryam"  # mutable => editable
print(names)

#                     0           1      2      3    4
names : list[any] = ["Maryam", "Ali", "Qasim", 20, True]
#                     -5         -4      -3    -2   -1
print(names)
del(names[3])  # delet 3 index element
print(names)

a : str = print("pakistan") # non-return function
print(a)

a : str = id(names)      #  return function
print(a)


# list Methods
#  * 'pop'
#  * 'append'
#  * 'insert'
#  * 'clear'
#  * 'copy'
#  * 'count'
#  * 'append'
#  * 'reverse'
#  * 'sort'


#  Pop Methods
#                     0           1      2      3    4
names : list[any] = ["Maryam", "Ali", "Qasim", 20, True]
#                     -5         -4      -3    -2   -1
print(names)
a: str = names.pop()  # pop  return method

print(a)

#  Append Method

names : list[str] = [ 'a' ,'b']
names.append("Maryam") # append method add elements in last
names.append("Bilal")  # append method add elements in last
names.append("Sir Zia") # append method add elements in last

# Insert Method

names : list[str] = ['a','b', 'c', 'd']
print(names)
names.insert(1, "Maryam") # insert on porticular condition

print(names)

# Clear Method
a: list[int] = [1,2,3]

a.clear()  # remove all elements but object ramin
print(a)

# Cop Method
a : list[str] = ['a', 'b', 'c', 'f']
b = a  # shallow copy
print(a)
print(b)

b[0] = 'pakistan'  # change only b variable but both variables updated
print(a)
print(b)


a : list[str] = ['a', 'b', 'c', 'f']
b = a.copy() # Deep copy
print(a)
print(b)

b[0] = 'pakistan'  # change only b variable but both variables updated
print(a)
print(b)

# Count Method
names: list[str] = ['1', '1', '1', '2', '4', '4', '2']
print(names.count("3"))
print(names.count("2"))

# append Method
names: list[str] = ["Maryam", "Ali", "Rimsha"]
new_faculty_members : list[str] = ['sir zia', 'sir inam']
names.append(new_faculty_members)
print(names)

# extend Method

names: list[str] = ["Maryam", "Ali", "Rimsha"]
new_faculty_members : list[str] = ['sir zia', 'sir inam']
names.extend(new_faculty_members)
print(names)

# remove method

names:list[str] = ['Maryam', 'Ali', 'Rimsha', 'sir zia', 'sir inam']
names.remove("sir zia")
print(names)

# index method
#                       0        1       2          3          4
names : list[str] = ['Maryam', 'Ali', 'Rimsha', 'sir zia', 'sir inam']
print(names.index("sir zia"))

# reverse method

names:list[str] = ['Maryam', 'Ali', 'Rimsha', 'sir zia', 'sir inam']
print(names)
names.reverse() # in_memory = change real data
print(names)

# sort method

names : list[str] = list("ABCDEF")
print(names)
names.sort()
print(names)

names : list[str] = list("ABCDEF")
print(names)
names.sort(reverse = True)
print(names)
