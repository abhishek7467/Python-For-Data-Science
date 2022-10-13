''' Nested if statement'''

x = int(input('Enter the first number : '))
y = int(input('Enter the second number : '))


if x == y:
    print('x and y are eqal')
else:
    if x > y:
        print('x is greater than y ')
    else:
        print('x is less than y ')

print('Execution Completed....')


# Find if a number is a single digit positive integer


x = int(input('Enter the first number : '))
# y=int(input('Enter the second number : '))


if x > 0:
    if x < 10:
        print('x is a positive single digit number ', x)
else:
    print('x is not  a positive single digit number ')


# Another way
x = int(input('Enter the first number : '))
if x > 0 and x < 10:
    print('x is a positive single digit number ', x)
else:
    print('x is not  a positive single digit number ')


# Find the type of character that the user enters

ch = input("Enter a Charter : ")

if ch.isalpha():
    print('The Character entered is a letter')

    if ch.islower():
        print('The Character entered is in lower case ')

    elif ch.isupper():
        print('The Character entered is in Upper case ')

elif ch.isdigit():
    print('The Character entered is digit')

elif ch.isspace():
    print('The Character entered is a space ')

else:
    print('The Character entered is not a letter, digit or space')


# Accept name of a month , print the number of days in that month

month = input("Enter the name of month :  ")

# the month which have 31 days are : january, March, May, July, August, October, December
# the month which have 30 days are: April, June, September, November
# February has either 28 or 29 dyas

if month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
    print(month, '  has 31 days. ')
elif month == 'April' or month == 'June' or month == 'September' or month == 'November':
    print(month, 'has 30 days..')
elif month == 'Feburary':
    print(month, ' has 28 or 19 days')
else:
    print(month, ' is invalid')


# Accept the name of a month and display the season
# summer months : March, April, May, June
# Monsoon  months : July, August, September, October
# Winter months : November, December, January, Feburary
season = input("Enter the name of month for find season :  ")

if season == 'March' or season == 'April' or season == 'June' or season == 'September':
    print('It is summer season')
elif season == 'July' or season == 'August' or season == 'September' or season == 'October':
    print('It is monsoon season')

elif season == 'November' or season == 'December' or season == 'January' or season == 'Feburay':
    print('It is Winter season')
else:
    print('Enter Invalid month....')

x = int(input('Enter the first number : '))
y = int(input('Enter the Second number : '))
z = int(input('Enter the Third number : '))

if x > y and x > z:
    print(' x is greatest.')
elif y > x and y > z:
    print(' y is greatest.')
else:
    print(' z is greatest.')
