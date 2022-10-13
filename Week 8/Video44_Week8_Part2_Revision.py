# Implementation Decorator 
from cv2 import split


def UpperString(ref):
    def process(): # creating  a nested function 
        data = ref()
        return data.upper()

    return  process # referencing to another function and function retuning another function 
def skilllynce():
    return  'This is a edutech'


result=UpperString(skilllynce)#Function as a parameter
print(result()) 

skilllynce()# original function unchanged



@UpperString
def MyFunction():
    return 'This is good' 

print(MyFunction())


def this_is_dec(func):#  We are using the same skilllynce program and now wrapping it with two more sentence 
    def googlecolab():
        print('Welcome to skill-Lync')
        func()
        print('Thanks for choosing us')
    return googlecolab

print(this_is_dec(skilllynce))


# They can also be called like this 
skilllynce=this_is_dec(skilllynce)
print(skilllynce)



# Double -click  (or enter to edit)

def UpperString(ref):
    def process(): # creating  a nested function 
        data = ref()
        return data.upper()
    return  process # referencing to another function and function retuning another function 


def Split(ref):
    def process(): # creating  a nested function 
        data = ref()
        return data.split()
    return  process # referencing to another function and function retuning another function 

@UpperString 
def skillynce1():
    return 'This is a edutech'

result=Split(skillynce1)
print(result())





# Double -click  (or enter to edit)

def UpperString(ref):
    def process(): # creating  a nested function 
        data = ref()
        print(data.upper())
        return data.upper()
    return  process # referencing to another function and function retuning another function 


def Split(ref):
    def process(): # creating  a nested function 
        data = ref()
        return data.split()
    return  process # referencing to another function and function retuning another function 
@Split
@UpperString 
def skillynce1():
    return 'This is a edutech'

print(skillynce1())


def UpperString(ref):
    data=ref
    return data.upper()

@UpperString 
def skillynce1():
    return 'This is a edutech'

print(skillynce1())


# Decorator with a parameter


def OuterFunction(string):
    def UpperString(ref): # creating  a nested function 
        def process():
            data = ref()
            return data.upper() + ' '+string
        return  process # referencing to another function and function retuning another function 
    return UpperString
    
@OuterFunction('We teach Data Sciences')
def skillynce1():
    return 'Welcome to skil lynce'
print(skillynce1())

@OuterFunction('We teach cfd')
def skillynce1():
    return 'Welcome to skil lynce'
print(skillynce1())
@OuterFunction('We teach Python')
def skillynce1():
    return 'Welcome to skil lynce'
print(skillynce1())




# more examples of  decorator



def OuterFunction(B):
    def UpperString(ref): # creating  a nested function 
        def process():
            data = ref()
            Total_salary =1.6*B
            return data.upper() + ' '+' Your salary is '+ ' '+ str(Total_salary)
        return  process # referencing to another function and function retuning another function 
    return UpperString
    
@OuterFunction(10000)
def skillynce1():
    return 'Welcome to skil lynce'
print(skillynce1())











def OuterFunction(dept_name):
    def UpperString(ref): # creating  a nested function 
        def process():
            data = ref()
            if dept_name=='cse':
                Total_salary =150000
            elif dept_name=='it':
                Total_salary=160000000
            elif dept_name=='ME':
                Total_salary=240000000            
            return data.upper() +' '+dept_name  + ' '+' Your have to pay us a total of '+ ' '+ str(Total_salary)
        return  process # referencing to another function and function retuning another function 
    return UpperString
    
@OuterFunction('cse')
def skillynce1():
    return 'Welcome to skil lynce'
print(skillynce1())
    
@OuterFunction('it')
def skillynce1():
    return 'Welcome to skil lynce'
print(skillynce1())
    
@OuterFunction('ME')
def skillynce1():
    return 'Welcome to skil lynce'
print(skillynce1())






def OuterFunction(ref):
    def Innerfunction(*args):
        return ref(*args).upper()

    return Innerfunction

def MyFunction(str1,str2):
    return "Hello {} and {} ".format(str1,str2)

obj=OuterFunction(MyFunction)
print(obj('apple','banana'))





class MyDeocrator:
    def __init__(self,ref):
        self.ref=ref
    
    def __call__(self,*args):
        return self.ref(*args).upper()


def MyFunction(str1,str2):
    return "Hello {} and {} ".format(str1,str2)

obj=MyDeocrator(MyFunction)
print(obj('apple','banana'))






class MyDecorator1:
    def __init__(self,ref):
        self.ref=ref
    
    def __call__(self,*args):
        return self.ref(*args).upper()


    def MyFunction(str1,str2):
        return "hii {} and {} ".format(str1,str2)

obj=MyDecorator1(MyFunction)
print(obj('apple','banana'))




''' Iterable (generally all classes in python are iterable by default )

Iterator (we set an iterator that is why this moving one by one)
Iteration (The process is called iteration)


'''

a='apple'# int is not iterables
b=128979218
for i in a:
    print(i)
b=128979218
for i in b:  #TypeError: 'int' object is not iterable
    print(i)


a='apple'
print(a.__iter__())

b=1526172
print(b.__iter__())


# When you  create a class and want to iterate it you have to create a iter method so that you can see the next. 
# __next__()  # takes the one and prints. 

my_list=[1,2,3,4,5]
for i in my_list:
    print(i)
my_list=iter(my_list)
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(my_list.__next__())



class Even(object):
    def __init__(self,l):
        self._limit=l 
        self._val=0

    def __iter__(self):
        return self 
    def __next__(self):
        if self._val>self._limit:
            raise StopIteration
        else:
            return_value=self._val
            self._val+=2
            return return_value
for i in Even(20):
    print(i)


#########
list1=[]
for i in range(20):
    if i%2==0:
        list1.append(i) 

print(list1)



# Even when you write it as a function it is created when the function is being called. 
def Even2(a):
    lst2=[]
    for i in range(20):
        if i%2==0:
            lst2.append(i) 
    return ( lst2)

print(Even2(520))
