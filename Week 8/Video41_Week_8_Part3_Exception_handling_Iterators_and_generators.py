
'''Use of ELSE Block'''
from numpy import square


def my_function(x,y):
    res=x/y
    return res


try:
    print('The result of division is : ',my_function(6,2))
except ZeroDivisionError as e:
    print(e)

else:
    print('No exception was raised. Everything worked Ok........ ')

'''Use of Finally Block'''
def my_function(x,y):
    res=x/y
    return res

try:
    print('The result of division is : ', my_function(6,2))
except ZeroDivisionError as e:
    print(e)

else:
    print('No exception was raised. Everything worked Ok........ ')

finally:
    print('This code always runs........')


'''Use of Raise an exception Block'''

x=6
y=0

def my_function(x,y):
    res=x/y
    return res
try:
    if y==0:
        raise ValueError('Division is not possible by 0')

    print('The result of division is : ', my_function(x,y))
except ValueError as e:
    print(e)

else:
    print('Everthing worked OK........')





'''  ###################### Assertions ########################## '''

x=6
y=2
def my_function(x,y):
    res=x/y
    return res
assert y!=0,' Denominator should not be 0'
print('After assert statement ')
my_function(x,y)



# Programm to accept  n positive intigers as input and print the suares of numbers from 1 to n. 
# If a negative numbers is entered, then raise ValueError exception and display a relevant error 
# message and exit 

class Squares(object):
    def __init__(self,l):
        self._limit = l
        self._val =0
    
    def __iter__(self):
        return self 
    def __next__(self):
        if self._val > self._limit:
            raise StopIteration
        
        else:
            return_val =self._val * self._val
            self._val +=1
            return return_val

print('Start..........')
n= int(input('Enter the value of n :  '))
try :
    if n<0:
        raise ValueError()

except ValueError:
    print('Enter a positive value for n ')
m=0
for i in Squares(n):
    print( f'The Square of {m} is ',i)
    m+=1
print('\nEnd......')






















