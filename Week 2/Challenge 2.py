# Question 1

# 1. Demonstrate how to create simple and multi-line strings, and check whether a string can change after its creation.


import math
single_line_string = 'This is Single line String..'
Multi_line_string = '''
                    
                    This is Multi Line String.
                    Abhishek Is a Good Boy.
                    He is 21 years old.

                    '''


print(f"This is single line string :  {single_line_string} ")
print(f"This is Multi line string : {Multi_line_string} ")


s = 'Hii '
print(s)  # i
print(s[1])  # 2
print(s[2])  # 3
print(len(s))  # 2
print(s + ' Abhishek')  # hi there

# s[1]='l'  # TypeError: 'str' object does not support item assignment
# print(s)
print("We can not change or not modify the string. But Concatenate Two strings")


# Question 2
''' For a given string ‘Hello World!’, extract the following:

H W
o o
llorld
!dlroW olleH
World!
Hello

'''


str1 = 'Hello World!'
print(str1[0], str1[6])
print(str1[4], str1[7])
str3 = str1[2:4]+str1[7:11]
print(str3)
print(str1[::-1])
print(str1[6:])
print(str1[:-7])


# Question 3
'''
3. For the following strings, determine which contain only alphabets, only digits, alphanumeric, which are in lowercase, and which are in uppercase. Also check whether str3 begins or ends with the word “Now”.

Str1 = ‘Welcome’

Str2 = ‘Hello World!’

Str3 = ‘Now is the best time ever! ‘

Str4 = ‘500017’

Str5 = ‘IPhone 6’
'''


str1 = 'Welcome'
str2 = 'Hello Wolrd'
str3 = 'Now is the best time ever!'
str4 = '500017'
str5 = 'IPhone 6'


print(" str1 Contains Only alphabets  ", str1.isalpha())
print(" str2 Contains Only alphabets  ", str2.isalpha())
print(" str3 Contains Only alphabets  ", str3.isalpha())
print(" str4 Contains Only alphabets  ", str4.isalpha())
print(" str5 Contains Only alphabets  ", str5.isalpha())


print(" str1 Contains Only Digit ", str1.isdigit())
print(" str2 Contains Only Digit ", str2.isdigit())
print(" str3 Contains Only Digit ", str3.isdigit())
print(" str4 Contains Only Digit ", str4.isdigit())
print(" str5 Contains Only Digit ", str5.isdigit())

print(" str1 Contains Only alphanumeric ", str1.isalnum())
print(" str2 Contains Only alphanumeric ", str2.isalnum())
print(" str3 Contains Only alphanumeric ", str3.isalnum())
print(" str4 Contains Only alphanumeric ", str4.isalnum())
print(" str5 Contains Only alphanumeric ", str5.isalnum())

print("str3 begins with the word “Now” ", str3.startswith('Now'))
print("str3 ends with the word “Now” ", str3.endswith('Now'))


# Question 4
# 4. Accept a sentence from the user. Convert the case of the input into title case.

str1 = input('Enter The Sentence : ')
str2 = str1.title()
print(str2)
# Question 5
# 5. Write a program that reads an integer from the user. Then your program should display a message indicating whether the integer is even or odd.


n = int(input('Enter The Number : '))
if n % 2 == 0:
    print(f"The {n} number is even")
else:
    print(f"The {n} number is odd")


# Question 6

# 6. Create a program that reads a letter of the alphabet from the user. If the user enters a, e, i, o or u then your program should display a message indicating that the entered letter is a vowel. Otherwise, the program should display a message that the entered letter is a consonant


alphabet = input('Enter a letter of the alphabet : ')

if alphabet == 'a' or alphabet == 'A' or alphabet == 'e' or alphabet == 'E' or alphabet == 'i' or alphabet == 'I' or alphabet == 'o' or alphabet == 'O' or alphabet == 'u' or alphabet == 'U':
    print(f'{alphabet} letter is a vowel.')
else:
    print(f'{alphabet} letter is a consonant.')


# Question 7

# 7. The length of a month varies from 28 to 31 days. Create a program that reads the name of a month from the user as a string. Then your program should display the number of days in that month. Display “28 or 29 days” for February so that leap years is addressed.

month = input("Enter the name of month :  ")

# the month which have 31 days are : january, March, May, July, August, October, December
# the month which have 30 days are: April, June, September, November
# February has either 28 or 29 dyas

if month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
    print(month, '  has 31 days. ')
elif month == 'April' or month == 'June' or month == 'September' or month == 'November':
    print(month, 'has 30 days..')
elif month == 'Feburary':
    leepY = int(input("ENter The Yaer(like 2022)  : "))
    if (leepY % 4 == 0 or leepY % 400 == 0) and leepY % 100 != 0:
        print(f'{month} has 29 days and {leepY} is  Leep Year')
    else:
        print(f'{month} has 28 days and {leepY} is not a Leep Year ')
else:
    print(month, ' is invalid')


# Question 8

# 8. A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles triangle has two sides that are the same length, and a third side that is a different length. If all of the sides have different lengths then the triangle is scalene. Write a program that reads the lengths of 3 sides of a triangle from the user. Display a message indicating the type of the triangle.


side1 = float(input('Enter The lenght of First side of triangle : '))
side2 = float(input('Enter The lenght of Second side of triangle : '))
side3 = float(input('Enter The lenght of Third side of triangle : '))

if side1 == side2 and side2 == side3:
    print(
        f"This is an Equilateral Triangle Because All 3 sides are Same length.   :  {side1} ")

elif (side1 == side2 and side3 != side2) or (side2 == side3 and side1 != side2) or (side1 == side3 and side2 != side1):
    if (side1 == side2 and side3 != side2):
        print(
            f"This is an Isosceles Trianglee Because   Two sides are Same length - {side1} and {side2} , and  a third side that is a different length - {side3}. ")
    elif(side2 == side3 and side1 != side2):
        print(
            f"This is an Isosceles Trianglee Because   Two sides are Same length - {side2} and {side3} , and  a third side that is a different length - {side1}. ")
    else:
        print(
            f"This is an Isosceles Trianglee Because   Two sides are Same length - {side3} and {side1} , and  a third side that is a different length - {side2}. ")
else:
    print(
        f"This is Scalene Triangle Because All 3 sides are Different length.   :  {side1}  , {side2} and {side3}")


# Question 9
'''
9. The rules for determining whether or not a year is a leap year follow:

 

Any year that is divisible by 400 is a leap year.
Of the remaining years, any year that is divisible by 100 is not a leap year.
Of the remaining years, any year that is divisible by 4 is a leap year.
All other years are not leap years.
Write a program that reads a year from the user and displays a message indicating whether or not it is a leap year.

'''


leepYear = int(input("ENter The Yaer(like 2022)  : "))

if (leepYear % 4 == 0 or leepYear % 400 == 0) and leepYear % 100 != 0:
    print(f'Feburary has 29 days and {leepYear} is  Leep Year')
else:
    print(f'Feburary has 28 days and {leepYear} is not a Leep Year ')


# Question 10
# 10. Write a program that computes the real roots of a quadratic function. Your program should begin by prompting the user for the values of a, b and c. Then it should display a message indicating the number of real roots, along with the values of the real roots (if any).


a = float(input('Enter the value of "a" Your First coefficient      :      '))
b = float(input('Enter the value of "b" Your Second coefficient      :      '))
c = float(input('Enter the value of "c" Your Thrid coefficient      :      '))

discriminant = b*b-4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f'Cofficients is {a} , {b} and {c}')
    print(f'Real Root1 {root1}')
    print(f'Real Root2 {root2}')


elif discriminant == 0:
    root1 = root2 = -b / (2 * a)

    print(f'Cofficients is {a} , {b} and {c}')
    print(f'Real Root1 {root1}')
    print(f'Real Root2 {root2}')

else:
    realPart = -b / (2 * a)
    ImagPart = math.sqrt(-discriminant)/(2 * a)
    print(f'Cofficients is {a} , {b} and {c}')
    print(f'Imaginary Root1 {realPart} + {ImagPart}i')
    print(f'Imaginary Root2 {realPart} + {ImagPart}i')
