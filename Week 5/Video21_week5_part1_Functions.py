'''                                FUNCTIONS                 '''
###             Built-in function

list1=[12,23,34,45,56,43,21,12,23]
print(f'The list is :  {list1}')

print('The max element in the list is  ' , max(list1))
print('The min element in the list is  ' , min(list1))
print('The len of the list is  ' , len(list1))
print('The type of the list is  ' , type(list1))


a=32.09

b=int(a)

c=str(b)
print(f'a : {a} , b : {b} , c  : {c}')
print('Type of  a ',type(a))
print('Type of  b ',type(b))
print('Type of c ',type(c))

# math function

import math

from numpy import mat
n=int(input('Enter a number to find the square root  :  ' ))

print('The square root is  : ' , math.sqrt(n))


import random
print('A random  number between 0.0 and 1.0 : ', random.random())


low = int(input('Enter the low value : '))
high = int(input('Enter the high value : '))
print(f'A rndom number between {low}  and {high} values : ', random.randint(low,high))


import random
t=(1,2,3,4,5,6,7,8,10,122,43)

print('The Tuple is  : ', t)
print(f'A random value from {t} is  : ', random.choice(t))




































































































