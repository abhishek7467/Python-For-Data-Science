'''                     Decorators                        '''

# A simple decorator 

def  my_function(func):
    def wrapper():
        print('$'*70)
        func()
        print('~'*70)
    return wrapper


@my_function 
def display ():
    print('Welcome  to Decorators !!!!!! ')

display()

# Demonstrate Multiple Decorators 

def star(func):
    def inner(*args, **kwargs ):
        print('*'*100)
        func(*args,**kwargs)
        print('*'*100)
    return inner 

def percent(func):
    def inner(*args,**kwagrs):
        print('%'*100)
        func(*args,**kwagrs)
        print('%'*100)
    return inner

@star
@percent
def printer(msg):
    print(msg)

printer('Multiple Decorators')


# Implement the timer decorator 


import time
def timer(func):
    def calculate(*args,**kwargs):
        start_time =time.perf_counter()
        value = func(*args,**kwargs)
        end_time = time.perf_counter()
        runtime = end_time-start_time
        print('Execution time      ::: {0:20.10f}sec '.format(runtime))
        return value
    return calculate

@timer
def Factorial(n):
    fact = 1
    for i in  range(n):
        fact = fact * (i+1)
    return fact

print(Factorial(5))

print('The decorated my_function is ')


























