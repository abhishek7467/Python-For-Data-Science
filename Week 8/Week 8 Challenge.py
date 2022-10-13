# Question 1

'''

Write a program that accepts two integers and displays the result 
of dividing the first number by the second number. 
It should raise ZeroDivisionError if the denominator is zero.

'''



def divide(a,b):
    try:
        a/b
        raise ZeroDivisionError
    except ValueError as e:
        print('Invalid Input........') 
    except ZeroDivisionError as e:
        print(e)
a=int(input('Enter the  a :'))
b=int(input('Enter the  b  :    '))
divide(a,b)




# Question 2
'''
Implement the above program with the help of Assertion

'''

x=int(input('Enter the  a :'))
y=int(input('Enter the  b  :    '))
def divide(x,y):
    res=x/y
    return res
assert y!=0,' Denominator should not be 0'
print('After assert statement ')
divide(x,y)






# Question 3

'''

Write a program that accepts n positive integers as input 
and prints their square. If a negative number is entered, then 
raise ValueError exception and 
display a relevant error message and make an exit.

'''
x=int(input('Enter the  a :'))
try:

    while x>0:
        print(f'The square of {x} is : {x*x}')
        x=int(input('Enter the  a :'))    

    raise ValueError
except ValueError:    
    print("You are entered negative numbers or blank line. \nExit....... ")



# Question 4 

'''

Write a program that receives an integer as input and finds its factorial.
 If a non-integer input is entered, then report an error and accept the input again. 
Continue this process until correct input is entered.


'''

import math
from random import randrange  
def mainfact():
    try:
        num=int(input('Enter the  a :'))
        while num>=0:
            print("Factorial of", num, "is", math.factorial(num))  
            num = int(input("Enter the number:"))  
    except ValueError:    
        print("You are entered non-integer value or blank line. \n\n Please Enter Valid value.........    ")
        mainfact()    
mainfact()




# Question 5 
'''

Create an iterator that returns numbers, starting with 1, and
 each sequence will increase by one (returning 1,2,3,4,5 etc.):


'''


b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 ]
for i in b:
    print(i)
print(b.__iter__())




# Question 6
''' 
Write a program that implements iterator 
class called Prime and which prints prime numbers up to n.

'''

class Prime:
    start_val = 1
    n = int(input("Enter the n number:"))
    list1=[]
    for i in range(n+1):
        list1.append(i) 
    for num in list1:
        if(num>1):
            for i in range(2,num):
                if(num%i)==0:
                    break
            else:
                print(f' The Prime number is        :             {num}')
            print(str(num).__iter__())



# Question 7

'''

Define a class, Circle, which takes two arguments when defined — a sequence and a number. 
The idea is that the object will then return elements the defined number of times. 
If the number is greater than the number of elements, then the sequence repeats as necessary.

'''







class Circle():
    def __init__(self,Seq,num):
        self.Seq=Seq
        self.num=num
class Count(Circle):
    def __init__(self,Seq,num):
        super().__init__(Seq,num)
        

    def Seque(self,Seq,num):
                    return self.num    

Seq=[1,2,3,4,5,6,6,7,8,6,5,4,3,2,1,2,3,4,5,6,7,8,9,0,7,5,6,3,2,1,2,4,5]
num=1
a=Count(Seq,num)
print('The object is', a.num)












# Question 8 


'''Write a Python program to demonstrate working of iterators using an 
example type that iterates from 10 to given value
'''






giv_Val=int(input('Enter your value (Value to be greater 10) :  '))
b = []
if giv_Val>10:
    for i in range(10,giv_Val+1):
        b.append(i)


iterable_obj = iter(b)

while True:
	try:

		item = next(iterable_obj)
		print(item)
	except StopIteration:

		break


# Question 9
'''

Write a program to illustrate the concept of multiple decorators


'''



def UpperString(ref):
    def process():
        data = ref()
        print(data.upper())
        print('@@@@@@@@')
        return data.upper()
    return  process

def LowerString(ref):
    def process():
        data = ref()
        print(data.lower())
        print('########')
        return data.lower()

    return  process

def Split(ref):
    def process(): 
        data = ref()
        print('&&&&&&&&')
        return data.split()
    return  process
@Split
@UpperString 
@LowerString
def skillynce1():
    return 'This is a edutech'


print(skillynce1())






# Question 10 
'''
Write a decorator called timer that calculates
the time required to execute a function. Its
wrapper function called calculates should take all the
parameters that are passed to the decorated function.

'''



import time
def timer(func):
    def wrapper(*args,**kwargs):
        start_time =time.perf_counter()
        value = func(*args,**kwargs)
        end_time = time.perf_counter()
        runtime = end_time-start_time
        print('Execution time      ::: {0:20.10f}sec '.format(runtime))
        return value
    return wrapper

@timer
def Factorial(n):
    fact = 1
    for i in  range(n):
        fact = fact * (i+1)
    return fact

print(Factorial(5))

print('The decorated my_function is ')
