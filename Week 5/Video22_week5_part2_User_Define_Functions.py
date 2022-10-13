def display_meaasge(): # function Decleration
    '''This function display a hello world message....'''
    print('Hello World! , This is function definition') #function definition
display_meaasge()#function call

print('This is after the function call')
display_meaasge()
print('The description of display_msg function is : ',display_meaasge.__doc__)





# Function which take argument / parameters

def display_msg(msg):

    print(f'{msg} to the Function Module in python')

display_msg('Welcome')
display_msg('Bye')


# function with return value
def square(n):
    res=n*n
    return res
sqr=square(5)
print('The return value is  : ',sqr)

print('The square of 345 is  : ',square(345))


# Function to return the sum of two numbers
def sum(a,b):
    return a+b

print('The sum of two numbers is  :  ',sum(1,2))
print('The sum of two numbers is  :  ',sum(100,200))
print('The sum of two numbers is  :  ',sum(111,211))


def greeter(name,prompt='Welcome',msg='To Python'):
    print(f'{name} {prompt} {msg}')

n=input('Enter your name:   ')
greeter(n)
greeter('Abhishek',msg='World')
greeter(msg='World',name='kumar',prompt='Hello')



# Positionals Arbitrary argument functions
def greeter(*args):
    for name in args:
        print('Welcome ' , name)

greeter('Abhishek','Kumar','Mahesh','Suresh')
greeter('Abhi','Aniket','Kum','ar')


# Positional and keyword arguments
def my_func(*args,**kwargs):
    for arg in args:
        print('arg  :  ', arg)

    for key in kwargs.keys():
        print('Key   : ',key, ' has value : ', kwargs[key])

my_func('Ramesh','Abhi',name='Abhishek',name2='Sandhya')


my_func('Ramesh', 'Alice',son1='Andrew',son2='James',doughter='joselyen')



# Function with only keyword arguments 
def named(**kwars):
    for key in kwars.keys():
        print('arg : ',key , '  has value  :  ',kwars[key])
named(a=1,b=2,c=4,g=12)
































