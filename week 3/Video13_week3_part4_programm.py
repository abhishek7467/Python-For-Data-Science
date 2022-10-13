# Write a programm to find ou whether a multi-word sentence is a panidrom or not

from unittest import result


str1 = input('Enter a sentence : ')
str2 = str1.replace(' ', '')


rev = str2[::-1]

for i in range(len(str2)):
    if str2[i] != rev[i]:
        print(f'{str1} is not a palindrome')
        break
else:
    print(f'{str1} is a palindrom string')


# print(str1)
# print(str2)


# Write a programm to accept a decimal integer and print its binary equivalent

'''
5-101
6-110
7-111
10-1010
15-1111
'''


result = ' '  # result will hold final binary equivalent number
q = int(input('Enter number(Only 0<) for find binary code : '))
while q != 0:
    r = q % 2
    result += str(r)
    q //= 2
result = result[::-1]
print(f'The binary eqivalent  is {result}')


'''    Consol Input       '''

a, b, c = input('Enter the value of a, b and c').split()

print(f"{a} {b} {c}")


'''    Console Output '''

a, b, c = input('Enter the values of a,b and c').split()

print(a, b, c, sep=' : ')
print(a, b, c, sep=' , ', end=' ')

print('This is a new statement ')
print(a, b, c, sep=' , ', end='\t ')
print('This is a new statement ')


# Formatted Output

r, l, b, name = 1.5678, 10.5, 8.678, 'Shubash Chandra Bose'
print(f'radius : {r}')
print(f'length :  {l}')
print(f'breadth :  {b}')
print(f'name :  {name}')

for i in name.split():
    print(i)
    print(f'{i:10}')


print('radius = {}, length = {} , breath = {} , name = {}'.format(r, l, b, name))

name, age, salary = 'Abhishek ', 21, 300890.23
name1, age1, salary1 = 'Riddhi ', 22, 99999999.87
print('name = {} , age = {}, salary= {} '.format(name, age, salary))
print('name1 = {} , age1 = {}, salary1= {} '.format(name1, age1, salary1))


# print in any desired order

print('radius = {2} , lenght {1}, breath = {0}'.format(b, l, r))
print('name = {2} , age {1}, salary = {0}'.format(salary, age, name))


# print name is 15 columns and salary in 10 columns
print('name = {0:15}, age = {1:10} ,salary ={0:5} '.format(name, age, salary))


# print radius in 10 columns with only 2 decimal spaces

r = 672.3
print('radius = {0:10.2f}'.format(r))
