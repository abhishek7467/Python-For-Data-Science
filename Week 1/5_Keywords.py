# I am importing set of modules I will be using in this brushing up.
from pickletools import string4
import string
import sys
import keyword
import operator
from datetime import datetime
import os

from more_itertools import lstrip


# no keyword what are the keywords of Python?
# Kindly do not name any variable with the following name. Python will throw error

print(keyword.kwlist)

# variable name can not start with a number

# 1a='apple' # This is wrong way to define variables

# except_ (underscore ) no others special character can be used to make a variable
# numerals can follow after the alphabet.
a_1 = 'apple'
print(a_1)

# a@2='Apple' # This is wrong way ti define variable

# Single line comment
temp1 = 28
print(temp1)

# This
# is
# Miltiline
# comment

'''This 
is 
Miltiline 
comment'''

"""
Another 
way to 
define
multiple 
line comment"""
temp = 10
print(temp)

t1 = """This 
is 
Multiline 
String
"""

print("\n\n")
temp4 = 10
print(temp4, t1)

a1 = 12+13
print(a1)
s2 = ['a', 'b', 'c', 'd']
print(s2)
s3 = 20+30\
    + 40+50 +\
    +70+80
print(s3)
s4 = ['a',
      'b',
      'c',
      'd'
      ]

print(a1, s2, s3, s4)

print("\n\n")
# integer
a = 5
print(type(a))
print(a)


# Float to include  decimal numbers
a = 5.5
print(type(a))

# string to include characters
c = 'an apple a day keeps doctor away'
print(type(c))
# Complex
d = 5+7j
print(type(d))

# Boolean
e = True
print(type(e))


# String

# various operations can be performed on string . A string once defined can only be rewritten fully.
# It can not be partially changed
# Every time a operation is done on string, we need to store it another variable to retrive it again.
string1 = 'apple is a red fruit'
string2 = 'banana is  a yellow fruit '

print("\n\n")
print(string1+string2)
print(string1 + ' ' + string2)  # note the gap due to ' '

print("\n\n")

print(string1.upper())
print(string1)  # note string1 is still lower.


print("\n\n")
string7 = string1.upper()
string5 = string1.title()
string6 = string1.split()  # remove all the spaces and gives the words alone
print(string7, ' --- ', string5, ' --- ', string6)
# Will remove a at the start from string1 (you can give any chracter if it is there it will remove)
string8 = string1.lstrip('a')
print(string8)
# Will remove a at the start from string1 (you can give any chracter if it is there it will remove)
string9 = string1.rstrip('t')
print(string8)
string10 = string1.lstrip('b')  # nochange
print(string8)
string11 = string1.rstrip('c')
print(string8)
print(string10, '----', string11)  # nochange

print(string2)

print("\n\n")
print(string2.islower())
print(string2.isupper())
print(string2.istitle())
print(string2.isdigit())
print('String2 strat with ', string2.startswith('banana'))
print('String2 ends with ', string2.endswith('fruit'))

print("\n\n")
print(len(string2), '<-- String Length -->', len(string10))


string11 = string1 + string2
print(string11)
print("\n \n \t \t")
print(string11[::-1])
print(string11[::-2])
print(string11[::2])
print(string11[2:9])
print(string11[2])
print(string11.replace(' ', '*'))

print("\n\n")
form = '''Hi,
        I This is name
        This is my offer  for you... '''
print(form)
nm = input("Enter your name : ")
print(form.replace('name', nm))

print("\n\n")
mystr1 = "Hello, Abhishek kumar"
for i in mystr1:
    print(i)


print("\n\n")
for i in enumerate(mystr1):  # This will give the index number along with the Varable

    print(i)


print("\n\n")
lst = list(enumerate(mystr1))
print(lst)


print("\n\n")
# String Membership
mystr1 = "Hello Everyone"
# check whether substring "Hello"  is present in string "mystr1"
print('Hello' in mystr1)
# check whether substring "Everyone"  is present in string "mystr1"
print("Everyone" in mystr1)
# check whether substring "Hii"  is present in string "mystr1"
print("Hii" in mystr1)

print("\n\n")
str5 = "This is a very long sentence and the sentence is stupid"
l = str5.partition("and")  # spliting at first end
print(l)

print("\n\n")
str5 = "This is a vary long sentence and the sentence is stupid"
l = str5.rpartition("and")  # spliting from the last end
print(l)

print("\n\n")
# Combing  string & numbers using format method

item1 = 40
item2 = 55
item3 = 77

res = "Cost of item1, item2 and item3 are {} , {} and {}"
print(res.format(item1, item2, item3))

print("\n\n")

res = "Cost of item1, item2 and item3 are {0} , {1} and {2}"

print(res.format(item1, item2, item3))

print("\n\n")
str2 = " Python is a nice pogramming language "
print(str2.center(100))
print(str2.center(150))
print(str2.center(200))
print(str2.center(100, '*'))
print(str2.rjust(100))
print(str2.ljust(50))


print("\n\n")

mystr6 = "123456789"
print(mystr6)
# Return True if all the characters in the text are letters
print(mystr6.isalpha())
print(mystr6.isalnum())  # Return True if a  contains only letters or numbers
print(mystr6.isdecimal())  # Return True if all the characters are decimal(0-9)
print(mystr6.isnumeric())  # Return True if all the characters are numeric(0-9)


print("\n\n")
mystr6 = 'abcde'
print(mystr6)
# Return True if all the characters in the text are letters
print(mystr6.isalpha())
print(mystr6.isalnum())  # Return True if a  contains only letters or numbers
print(mystr6.isdecimal())  # Return True if all the characters are decimal(0-9)
print(mystr6.isnumeric())  # Return True if all the characters are numeric(0-9)


print("\n\n")
mystr7 = 'ABCDE'
print(mystr7.isupper())  # Return True if all the characters are Upper case
print(mystr7.islower())  # Return True if all the characters are lower case

print("\n\n")
mystr8 = 'abcde'
print(mystr7.isupper())  # Return True if all the characters are Upper case
print(mystr7.islower())  # Return True if all the characters are lower case
