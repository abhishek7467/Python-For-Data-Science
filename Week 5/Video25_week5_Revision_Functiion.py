
for i in range(10): # In-built function
    print(i)

def evenodd(num):
    '''evenodd Function :- This function will test whether a number is Even or Odd'''

    if num % 2==0:
        print('Even Number')
    else:
        print('Odd Number')

evenodd(123)
evenodd(122)
print(evenodd.__doc__)




var1=100 # variable with Global scope. 
def myfunc():
    print(var1) # value 100 will be displayed due to global of var1

myfunc()
print(var1)


def myfunce1():
    var2 = 10 # Variable with loacal scope
    print(var2)
# def myfunc2():
#     print(var2)#This will throw erroe because var2 has a local scope, var2 is only accessible in myfunc1() 
myfunce1()
# myfunc2()






var2 = 10 # Variable with Global scope
def myfunce1():
    print(var2)

def myfunc2():
    print(var2)
myfunce1()
myfunc2()


def sddtwonumber(x,y):
    return x+y
print(sddtwonumber(3,4))


def addthreenum(x,y,z):
    return x+y+z
print(addthreenum(2,4,1))

def addfournum(x,y,z,a):
    return x-a+y*z
print(addfournum(45,23,12,78))



def add(*args):
    return sum(args)
print(add(1,2,3))
print(add(1,2,3,4)) # *args take argument list. SO add() function will perform addition of any number 
print(add(1,2,3,4,5))
print(add(1,2,3,4,5,6,7))
print(add(1,2,3,4,5,6,7,8))



list1=[1,2,3,4,5,6,7]
tup1=(1,2,3,4,5,6,7)
print(add(*list1))
print(add(*tup1))



def add(*args):
    return sum(args)
list1=[1,2,3,4,5,6,7]
list2=[1,2,3,4,5,6,7]
list3=[1,2,3,4,5,6,7]
list4=[1,2,3,4,5,6,7]
list5=[1,2,3,4,5,6,7]
list6=[1,2,3,4,5,6,7]
list7=[1,2,3,4,5,6,7]
add(*list1,*list2,*list3,*list4,*list5,*list6,*list7) # list is sent as an argument


def UserDetails(*args):
    print(args)
UserDetails('Skill-Lync',7467,2342,34,'India','Abhishek')


def UserDetails1(**kwargs):
    for key,val in kwargs.items():
        print('{} :- {}  '.format(key,val))

UserDetails1(Name='Abhi',Coures='B.Tech',clgId="127891cs",pincode=243123 ,country='India',citu='Bareilly')


UserDetails1(Name='Skill-Lync',Coures='B.Tech')#here only two key word arguments were given 

mydict={'Name':'Abhi','Coures':'B.Tech','clgId':"127891cs",'pincode':243123 ,'country':'India',"city":'Bareilly'}
# passing the dictionary in kwargs
UserDetails1(**mydict)


def UserDets(licenseNo, *args, PhoneNo=0,**kwargs): #using all four arguments types
    print('License No :- ', licenseNo)
    j=' '
    for i in args:
        j=j+i
    print('Full Name :-  ',j)
    print('Phone Number:- ',PhoneNo)
    for key,val in kwargs.items():
        print("{} :- {} ".format(key,val))

    
name=['Skill',' ','Lync']
mydict={'Name':'Abhi','Coures':'B.Tech','clgId':"127891cs",'pincode':243123 ,'country':'India',"city":'Bareilly'}


UserDets('RANDI123',*name,PhoneNo=8756230912,**mydict)


# Filter

''' It is used to filter the iterables/sequence as per the condition'''
'''Filter function filters the original iterable the items that returns True for the function provided to filter '''
''' It is normally used with lambda function to filter list,tuple or sets'''









# Filter Function
'''Function - function tests if elements of an iterable returns true or false'''
''' Iterable - Sequence which needs to be filtered , could be sets, lists, tuples or, any iterators '''





# Map
# 'The map(' function applies a given function to each item often iterable(list, ,tuple etc )  and returns a list of iterable

''' Function: The function to execute for each item of given iterable.'''
'''Iterable :  It is a iterable which is to be mapped'''



# Lambda
'''A lambda function is an anonymous function without a name'''
'''Lambda function can have any number of arguments but only one expression. The expression is evaluated and returned'''
'We use lambda function when we require a nameless function for a dhort period of time'



addition = lambda a:a+10 #This lambda function adds value 10 to an argument.
print(addition(5))

product=lambda a,b:a*b #This lambda function takes two arguments (a,b) and returns their product (a*b).
print(product(5,5))

addition =lambda a,b,c:a+b+c  #This lambda function takes three arguments (a,b,c) and returns their sum (a+b+c).
print(addition(5,2,1))

res=(lambda *args:sum(args) ) # #This lambda function takes any number of arguments  and returns their sum.
print(res(10,20),res(10,20,30,40),res(10,20,30,40,50,60,70,80,90))

res1=(lambda **kwargs : sum(kwargs.values())) # #This lambda function takes any number of arguments  and returns 
print(res1(w=10,b=20,c=30), res1(a=10,b=20,c=30,d=40,e=50))

print("*"*50)
# User defined function to find product of numbers

