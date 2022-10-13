'''   Condition Statement  '''
# Relational Operators -->   <,><=,>=,==,!=

a = 10
b = 20
c = 20

print('a < b ', a < b)
print('a > b ', a > b)
print('c == b ', c == b)
print('c >= b ', c >= b)
print('c <= b ', a <= b)
print('a is not = b ', a != b)


# Logical OPerators -->  and, or, not

a = 10
b = 20
c = 30

print(a > b or a < c)
print(a > b or a > c)


print(a < b and a < c)
print(a > b and a < c)

print(a < b)
print(not a < b)
print(not a > b)


'''             Use of IF Statement            '''


# Check whether a number is positive or not

x = int(input('Enter an integer : '))
if x > 0:
    print('The number  (', x, ')  is positive number')
print(' Program completed ')


'''             Use of IF ELSE Statement            '''


# Check whether a number is positive or Negative number

x = int(input('Enter a non-zero integer : '))
if x > 0:
    print('The number  ', x, '  is positive number')
else:
    print('The number ', x, ' is negative number')

print(' Program completed ')


# Check whether an integer is even or odd

n = int(input('Enter a positive integer : '))
if n % 2 == 0:
    print('The number  ', n, '  is Even number')
else:
    print('The number ', n, ' is Odd number')

print(' Program completed ')


'''             Use of IF ELIF... ELSE Statement            '''


x = int(input('Enter a positive integer : '))
y = int(input('Enter a positive integer : '))
if x > y:
    print('The number  ', x, '  is Greater than ', y)
elif y > x:

    print('The number  ', x, '  is Less than ', y)

else:
    print('The number  ', x, '  is Equal to than ', y)
    print('')
print(' Program completed.... ')
