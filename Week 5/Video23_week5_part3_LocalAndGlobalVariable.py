'''
Variables which are defined outside all functions are called global variables.
Global variables are accessible from anywhere (or globally) in the programm.'''

''' A Varibale which is defined whithin a function is called a local variables. 
Local variables are scoped only to that function and are not accessible or visible outside of the  function. '''

# Local Variables

def my_func():
    a_variable =100
    print(a_variable)

my_func()
# print(a_variable)    # NameError: name 'a_variable' is not defined 





# Global Variable

a_variable=200 # Global Variable
def my_func1():
    b_variable =100 # Local Variable
    print('This is Local Variable',b_variable) #Local Variable
    print(' This is Global Variable',a_variable) # Global Variable
    

my_func1()

print('This is Global Variable and outside from the function  :  ',a_variable) #Global Variable





# Access a global variable from within a function

# x=200 #Global Variable
# def m_func():
#     x=x+1
#     print('The value after increment : ',x)

# m_func()

# above statement  throw the error


x=200 #Global Variable
def m_func():
    global x
    x=x+1
    print('The value after increment : ',x)

m_func()



#function within a function  - nonlocal variables
#without using nonlocal variable
def func1(): #Outer Function
    x=100
    print('x  =  ',x )#  Local to func1
    def func2(): # inner function
        x=x+1
        print('x in func2 = ',x)
    func2()
func1()


# Using nonlocal variable

def func1(): #Outer Function
    x=100
    print('x  =  ',x )#  Local to func1
    def func2(): # inner function
        nonlocal x
        x=x+1
        print('x in func2 = ',x)
    func2()
    print('The value of x after call to func2   ', x)
func1()



'''Recursion'''''



'''A recursion solution in programming laguage such as python is one in which a function 
calls itself one or more times in order to solve a particular problem '''
'''In many cases the result of calling itself is combined with the
functions current state to return a result'''



# Factorial of a number
 # Example  5! = 5*4*3*2*1 =120
def fact(n):
    if n==0:
        return 1
    else:
        
        return n*fact(n-1)

n=int(input('Enter the number to find factorial : ' ))

print(f'The factorial of {n}! is  : ', fact(n))


# Anonymous Function /  Lambda Function 

square = lambda i:i*i
print(square(5))


func0 =lambda : print('Lambda function without arguments')

func1 = lambda  x:x*x
func2 = lambda x,y :x*y
func3 = lambda x,y,z  :x+y+z
func0()
print(func1(4))
print(func2(2,3))
print(func3(4,5,6))








