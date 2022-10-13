# Continue Statement


# Example to demonstrate continue statement

from doctest import Example

from pyparsing import alphas


for i in range(0, 10):
    if i == 7:
        continue
    print('i =  ', i)


''' PASS STATEMENT '''


n = int(input('Enter an integer : '))
if n == 10:
    pass
else:
    print('value entered is not 10   ')


# Elese Statement with for loop

for i in range(0, 10):
    print(' i =  ', i)

else:
    print('All iteration completed.......')


print('Outside from the loop')


# in break case the else part is not execute

for i in range(0, 10):
    print(' i =  ', i)
    if i == 7:
        break
else:
    print('All iteration completed.......')


print('Outside from the loop')


# Programmin Example

# WAP a program to accept an integer n greater than 10 .Then  print all the even number from 1 to n

n = int(input('Enter an integer greater than 10 : '))
if n > 10:
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i)


else:
    print('Invalid value of n ')


# WAP a program to accept a number n. Determine whether the number is prime or not

n = int(input('Enter the number :  '))
for i in range(2, n):
    if (n % i) == 0:
        print('The number ', n, ' is not prime')
        break
else:
    print('The prime number is : ', n)


# Write a programm to accept a string. Determine whether the string is palindrome or not
# Example of palindrome are : madam, civic, level

str1 = input('Enter the string : ')
rev = str1[::-1]
for i in range(len(str1)):
    if str1[i] != rev[i]:
        print('The string ', str1, 'is not a palindrome ')
        break
    else:
        print('The string ', str1, ' is palindrome...')


# Write a program to accept a string from the user. Count the number of spaces

str2 = input('Enter the string : ')
count = 0
for i in str2:
    if i.isspace():
        count += 1
print(f'The total count of number of spaces is : {count}')

# Write a program to accept a string from the user. Count the number of spaces, character , digit, special_character, alpha
# Lower case , upper case ,

str3 = input('Enter the string: ')
lcase = 0
Ucase = 0
space = 0
char = 0
digit = 0
special_char = 0
alpha = 0
allnum = 0
for i in str3:
    if i.isspace():
        space += 1
    if i.islower():
        lcase += 1
    if i.isupper():
        Ucase += 1
    # if i.ischr():
    #     char+=1
    if i.isdigit():
        digit += 1
    if i.isalpha():
        alpha += 1
    if i.isalnum():
        allnum += 1
    else:
        special_char += 1


print(f'The total count of number of spaces is : {space}')
print(f'The total count of number of Lower case lletter is : {lcase}')
print(f'The total count of number of Uper case  letter is : {Ucase}')
# print(f'The total count of number of Character is : {char}')
print(f'The total count of number of digit is : {digit}')
print(f'The total count of number of Alpha is : {alpha}')
print(f'The total count of number of all number is : {allnum}')
print(f'The total count of number of Special Charcter is : {special_char}')

for i in str3:
    if i.isspace():
        print(f'The total count of number of spaces is : {space}')
    elif i.islower():
        print(f'The total count of number of Lower case lletter is : {lcase}')

    elif i.isupper():
        print(f'The total count of number of Uper case  letter is : {Ucase}')

    # if i.ischr():
    # print(f'The total count of number of Character is : {char}')

    elif i.isdigit():
        print(f'The total count of number of digit is : {digit}')

    elif i.isalpha():
        print(f'The total count of number of Alpha is : {alpha}')
    elif i.isalnum():
        print(
            f'The total count of number of Special Charcter is : {special_char}')
    else:
        print(f'The total count of number of all number is : {allnum}')
