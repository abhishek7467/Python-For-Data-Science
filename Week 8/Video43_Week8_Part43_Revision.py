'''  Error and Handling  '''

'''
1. try--> It tries to something , execute a block of statement and  checks if there  an issue  in excution. if there is an error , then it gives to except. 
2. except--> In general there are different types of except. 
3. finally--> no matter whether it fails in try or not finally will finish

'''



from string import printable
from tkinter import Y


print(T)
for i in range (1,10):
    print('The Square of i is ', i**2)




x=input('Enter a number')
y=input('Enter a number')

z=x*y 
print(z)   #TypeError: can't multiply sequence by non-int of type 'str'


# Assume we have a code containing 10 lines. With same error in second line . Then the error is thrown out and the process is 
# terminated and does not proceed to the remaining lines. So to figure out where the error is we use error handling. 



try:
    print(T)
    for i in range (1,10):
        print('The Square of i is ', i**2)
except NameError:
    print('The variable is not declared')




try:
    print(T)
except NameError: 
    print('The variable is not declared')

finally:    
    for i in range (1,10):
        print('The Square of i is ', i**2)



# Except is invoked when try fails. Finally works no matter what. 
# ofcourse if there is an error in it, there will be a problem. 



try:
    T=10
    print(T)
except NameError: 
    print('The variable is not declared')

finally:    
    for i in range (1,10):
        print('The Square of i is ', i**2)


num = int(input('Enter a number'))# if input alphanumeric value # ValueError: invalid literal for int() with base 10: '4e'
print(num)



# Assume that this person will make some mistake 
try:
    num = int(input('Enter a number'))# if input alphanumeric value # ValueError: invalid literal for int() with base 10: '4e'
    print(num)
except:
    print('Invalid Input')



# Let us add a division by zero
val=100/0 # ZeroDivisionError: division by zero
try:
    num = int(input('Enter a number'))# if input alphanumeric value # ValueError: invalid literal for int() with base 10: '4e'
    print(num)
except:
    print('Invalid Input')




# Let us add a division by zero
try:
    val=100/0 # Remove the error
    num = int(input('Enter a number'))# if input alphanumeric value # ValueError: invalid literal for int() with base 10: '4e'
    print(num)
except ZeroDivisionError:
    print('You are trying to divide by zero')
except ValueError:
    print('Invalid Input')

'''  Assertion '''
''' 
Get input from user and print it. Let us assume we gat age from the user. 
Age can nevwe be negative or zero. So we are going to use it as an '''


def age(value):
    print("'The person's age is'", value)
value = int(input("'Enter the personn's age : "))
age(value)
age(10)




''' Our programme printed all values. So we are going to use an assert to tell user 
that age can not be negative. assert expression, print
'''
def age(value):
    assert value>0,'Enter a age greater than zero ' #AssertionError: Enter a age greater than zero
    print("'The person's age is'", value)
value = int(input("'Enter the personn's age : "))
age(value)



''' Catching exception : So that aour program can run. Python terprertor will show us the mistake but wont stop further computation.'''

a=[2,3,4,5,'a',8,0]
for i in a:
    c=2/i #TypeError: unsupported operand type(s) for /: 'int' and 'str'
    print(c)



# So now there is an error because of presence of a. 
import sys 
a=[2,3,4,5,'a',8,0]
for i in a:
    try:
        c=2/i 
        print(c)
    except:
        print('Problem occured')
        print('Problem',sys.exc_info()[0],'occured')# This just tells you tha kind of error that occured



import sys
a=[2,3,4,5,'a',8,0]
for i in a:
    try:
        c=2/i 
        print(c)
    b=x
    except:
        # print('Problem occured')
        print('Problem',sys.exc_info()[0],'occured')# This just tells you tha kind of error that occured



import sys
a=[2,3,4,5,'a',8,0]
for i in a:
    try:
        # c=2/i 
        print(c)
    
    except:
        # print('Problem occured')
        print('Problem',sys.exc_info()[0],'occured')# This just tells you tha kind of error that occured




# number guessing game 
# we have to guess the number 
class Error(Exception):
    pass
class TooSmallError(Error):
    pass
class TooLargeError(Error):
    pass

num=10 
while True:
    try:
        choice = int(input('Enter a number : '))
        if  choice<num:
            raise TooSmallError
        elif choice >num:
            raise TooLargeError
        break 
    except TooSmallError:
        print('You have entred a small number')

    except TooLargeError:
        print('You have entred a big number ')
    print('The correct number is 10. ')





'''    Decorator '''
'''
Ability to modify a function with out changing its code. 
we call a function by giving another as a input. 

'''


def skilllynce():
    print('This is a edutech')

'''
So who ever calls skilllynce will the a statement This is a edutech. 
Now if suppose i want to print additional lines but i dont want to change the function , then i have to use decorators. 
Any python callable object that is used to modify a function or class is called a decorator 
There are two types function and class decorator.  
giving additional functionality to a function
you need to learn these four concepts to understand what a decorator is
nested function --(in the example inner is nested inside outer )
function returing another function 
function as reference -- in the return statement inner is reffernce to the functio inner. 
functios as parameter 
consider the funstion given below. The moment we call the function outer, n1 is initialised to 3 the inner function is not yet invoked because it 
is not yet called . We are only defining the function . 
return inner will now call the function . inner is now called as reference and stored  in the variable called object.  


'''


# nested function in the function below the function inner is nested inside the outer. 
# the output of the outer is return inner, it returns a functions as output. 



def outer():
    n1=3    # When we run outer n1=3 initialised . inner is not yet invoked . inner invoked only at return statement.    
    def inner():
        n2=6
        res=n1+n2
        return res 
    return inner  # Please note the inner function is returned here. and the outer function returs the inner . Now inner function will.. 


obj=outer() # the out out of outer is stored at OBJ
print(obj()) # The final result is 9 
print(obj.__name__)# The function inner is called 
print(obj)






# passing function as  parameter 

def func1():
    print('Hello this is function 1')
def func2(apple): # here the function is passed as a argument
    print('Hello this is function 2 calling function 1')
    apple()

func2(func1)


''' 
Decorator --> 1. Function decorator and 2. Class decorator'''

# Single decorator muliple decorator 
# With argument without argument 


# Implementation of a decoarator 









