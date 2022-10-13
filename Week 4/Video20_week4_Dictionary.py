'''       Dictionaries         '''


from hashlib import md5


mydict = dict()  # Create Empty Dictionary
print(mydict)

# same as
mydict = {}  # Empty Dictionary
print(mydict)

mydict = {1: 'one', 2: 'two', 3: 'Three'}  # dictionary with integer keys
print(mydict)

# create dictionary using dict()
mydict1 = dict({1: 'one', 2: 'two', 3: 'Three'})
print(mydict1)

# dictionary with  Character keys
mydictChar = {'A': 'one', 'B': 'two', 'C': 'Three'}
print(mydictChar)

mydictMixed = {1: 'one', 'B': 'two', 3: 'Three'}  # dictionary with mixed keys
print(mydictMixed)

print(mydictMixed.keys())
print(mydictMixed.values())
print(mydictMixed.items())

# dictionary with mixed keys
mydict2 = {1: 'one', 2: 'two', 'A': ['Python', 'java', 'C']}
print(mydict2)
mydict2 = {1: 'one', 2: 'two', 'A': ['Python', 'java', 'C'], 'B': (
    'Python', 'Chemistry', 'Maths')}  # dictionary with mixed keys
print(mydict2)

keys = {'a', 'b', 'c', 'd'}
mydict3 = dict.fromkeys(keys)  # create a dictionary from a sequence of keys
print(mydict3)

keys = range(5)
mydict4 = dict.fromkeys(keys)
print(mydict4)

keys = {'a', 'b', 'c', 'd'}
value = 10
# craete a dictionary from a sequence of keys with value
mydict5 = dict.fromkeys(keys, value)
print(mydict5)

keys = {'a', 'b', 'c', 'd'}
value = [10, 20, 30]
# craete a dictionary from a sequence of keys with value
mydict6 = dict.fromkeys(keys, value)
print(mydict6)

value.append(40)
print(mydict6)

# dictionary with integer keys
mydict = {1: 'one', 2: 'two', 3: 'Three', 4: 'four'}
print(mydict)
print(mydict[1])

mydict1 = {'Name': 'ABX', 'ID': 190110,
           'DOB': 2000, 'Address': 'Uttar Pradesh'}
print(mydict1)

mydict1['Address'] = 'Delhi'
print(mydict1)

dict1 = {'DOB': 1995}
mydict1.update(dict1)  # UPDATE the value by the DOB key
print(mydict1)

mydict1.update({'Name': 'Abhishek Kumar'})
print(mydict1)

# Removing particular items ID from the dictionary using Pop Method
mydict1.pop('ID')
print(mydict1)
print(mydict1.popitem())  # Remove a random item and display it

print(mydict1)

del [mydict1['Name']]  # Removing item usonmg del method
print(mydict1)


mydict1.clear()  # Delete all the item of the dictionary
print(mydict1)

mydict2 = {'Name': 'ABX', 'ID': 190110,
           'DOB': 2000, 'Address': 'Uttar Pradesh'}
print(mydict2)
mydict1 = {'Name': 'Abhishek', 'ID': 19016781,
           'DOB': 2006, 'Address': 'Barabanki'}


# craete a new refrence "mydict2" anychanges does mydict2 will be reflected in both
mydict2 = mydict1

print(mydict2)
# mydict2.clear()
mydict3 = mydict1.copy()  # copy doesn't inherit the changes
mydict1['Address'] = 'Mumbai'
mydict2['DOB'] = 1990
print(mydict1)
print(mydict2)
print(mydict3)


mydict1 = {'Name': 'Abhishek', 'ID': 19016781,
           'DOB': 2006, 'Address': 'Barabanki'}

for i in mydict1:
    print(i, "  : ", mydict1[i])

mydict1 = {'Name': 'Abhishek', 'ID': 19016781,
           'DOB': 2006, 'Address': 'Barabanki'}
for i in mydict1:
    print(mydict1[i])  # Dictionary items
# same as
print([mydict1[i] for i in mydict1])

mydict1 = {'Name': 'Ridhi', 'ID': 9842,
           'Department': 'IT', 'Address': 'Barabanki'}
print(mydict1)

print('Name' in mydict1)
print('ID' in mydict1)
print('Ridhi' in mydict1)  # Only keys can be searched in dictionary

# double each value using dict comprehension
double = {i: i*2 for i in range(20)}
print(double)

# same as
double1 = {}
for i in range(20):
    double1.update({i: i**2})
print(double1)

# Creating dictionary with two separate datasets

key = ['one', 'two', 'three', 'four', 'five']
value = [1, 2, 3, 4, 5]
# using dict comprehension to create dictionary
mydict = {k: v for (k, v) in zip(key, value)}
print(mydict)

Dic = dict.fromkeys(key, value)
print(Dic)

mydict1 = {'a': 10, 'b': 20, 'c': '30', 'd': 40, 'e': 50}
# Divide all values in a dictionary by 10
mydict1 = {k: v/10 for(k, v) in mydict.items()}
print(mydict)

str1 = 'abcdefghijklmnopqrstuvwxyz'
mydict3 = {i: i.upper() for i in str1}  # lower to upper
print({i: i.upper() for i in str1})
print(mydict3)



# Comparison Operator
x = 20
y = 30
print('Is x greater than y: -', x > y)  # ()\nto push one line below \t is tab
print('\nIs x less than y: -', x < y)  # ()\nto push one line below \t is tab
print('\nIs x eqal to y: -', x == y)  # ()\nto push one line below \t is tab
# ()\nto push one line below \t is tab
print('\nIs x not equal to  y: -', x != y)
# ()\nto push one line below \t is tab
print('\nIs x greater  than or equal to y: -', x >= y)
# ()\nto push one line below \t is tab
print('\nIs x less than or equal to y: -', x <= y)


# Formatting
a = 50
b = 21

x = 'Python'
y = 'Programming'

# Addition
c = a+b
print('Addition of {} and {} will give : - {}\n'.format(a, b, c))

# concatenate string using plus operator
z = x+y
print('Concatenate string \'x\' and \'y\' using \'+\' operator :- {} \n'.format(z))

# Subsraction
c = a-b
print('Substracting {} from {} will give :- {}\n '.format(b, a, c))

# Multiplication
c = a*b
print('MultiPlying {} and {} will give :- {}\n'.format(a, b, c))

# Division
c = a/b
print('Dividing {} by {} will give :- {} \n '.format(a.b.c))


'''                          Python Indentation            '''
# IN other programming languagwe blocks are enclosed  with in curly braces or paranthyesis. In python, indentation serves
# the purpose of braces

a = 5
if a == 5:
    print('a is equal to 5')

# The same with out indentation will throw out an error
# a=5
# if a==5:
# print('a is equal to 5') # Indentation Error


for i in range(0, 5):
    print(i)
# This is eqal to
for i in range(0, 5):
    print(i)

# This is equal to
a = [i for i in range(0, 5)]
print(a)
