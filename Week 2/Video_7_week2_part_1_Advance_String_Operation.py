# Split Operation

from gettext import find


str1 = "Welcom, To the Abhishek Kumar , City Bareilly "
print(str1)
print('The split using comma : ', str1.split(','))
print('The split using a or A : ', str1.split('a' or 'A'))
print('The split using i : ', str1.split('i'))


strin2 = 'Welcome : to the exciting world : of python programming : language'
print('Split string using : ', strin2.split(':'))
print('Split string using : ', strin2.split())
print('Split string using : ', strin2.split(' '))


# Count
my_str = 'Count, the number of spaces'

print('No. of s in my_string', my_str.count('s'))
print('No. of e in my_string', my_str.count('e'))


# Replace
welcome_message = 'Hello world!'
str1 = welcome_message.replace('Hello', 'Bye ')
print(str1)

# find
str1 = 'welcome , to the exciting world, of python Programming Laguage and This is Abhishek Kumar '
print(str1.find('to'))
print(str1.find('Abhishek'))
print(str1.find('Hello'))
print(str1.find('python'))

# String Comparision

str1 = 'Ridhi Jaiswal'
str2 = 'Abhishek kumar'

print(str1 == str2)
print(str1 != str2)


str1 = 'Hello Abhishek'
print('The string is : ', str1)

# Start With Operation
print("str1 startswith('H') : ", str1.startswith('H'))
print("str1 startswith('A') : ", str1.startswith('A'))

# Endswith Operation

print("str1 endswith('k') : ", str1.endswith('k'))
print("str1 endswith('H') : ", str1.endswith('H'))

# istitle
print("str1.istitle()", str1.istitle())
print("str2.istitle()", str2.istitle())

str1 = 'Hello, Abhishek kumar'
print("str1.istitle()", str1.istitle())


# islower , isupper

print("str1.islower() : ", str1.islower())
print("str1.isupper() : ", str1.isupper())

str2 = 'abhishek '
str3 = 'RIDHI'
print("str2.islower() : ", str2.islower())
print("str3.isupper() : ", str3.isupper())


# isalpha

print("str1.isalpha :", str1.isalpha())
print("str2.isalpha : ", str2.isalpha())
print("str3.isalpha : ", str3.isalpha())


# upper and lower
print("String 2", str2)
print("String 3", str3)

print("In Upper case str2 : ", str2.upper())
print("In lower case str3 : ", str3.lower())


str2 = " hello world "
print(str2.istitle())
print(str2.title())


# Swapcase

str3 = 'Good Day '

print("Str3 : ", str3)
print("str3.swapcase : ", str3.swapcase())


# strip
str2 = '    Hello Ridhi Jaiswal , how are you ?          '
print(str2)
print(str2.strip())
