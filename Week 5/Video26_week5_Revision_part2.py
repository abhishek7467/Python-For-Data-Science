from ast import operator
from numpy import double


print("*"*50)

# User defined function to find product of numbers

def product (nums):
    total=1
    for i in nums:
        total*=1
    return total




# This lambda function can take any number of arguments and return their product. 
res1 =(lambda **kwargs : product(kwargs.values()))
print(res1(a=10,b=20,c=30),res1(a=10,b=20,c=30,d=40,e=50))

print("*"*50)


def myfunc(n):
    return lambda a:a+n

qdd10=myfunc(10)
qdd20=myfunc(20)
qdd30=myfunc(30)

print(qdd10(5))
print(qdd20(5))
print(qdd30(5))


list1=[1,2,3,4,5,6,7]
def odd(n):
    if n%2==1:return True
    else :return False
odd_num=list(filter(odd,list1)) # This FIlter function filters list1 and passs all odd numbers to filter(). 
print(odd_num)


def twice(n):
    return n*2

double = list(map(twice,odd_num))# The map function will aply user definrd "twice()" function on all items of  the list
print(double)
doubleset=set(map(twice,odd_num))
print(doubleset) 


doublees=list(map(lambda n: n*2,odd_num)) # This map function will double all items of the list using lambda function



print(doublees)





from functools import reduce
dlist=[2, 6, 10, 14]
def add(a,b):
    return a+b

sum_all= reduce(add,dlist) # This reduce function will perform sum of all items in the list using user defined  "add()" func. 
print(sum_all)



## same as 
# the below reduce() function will perform summ of all items in the list using  lambda function. 
sum_all2 = reduce(lambda a,b:a+b,dlist)
print(sum_all2)


# all together
sum_all = reduce(lambda a,b:a+b, list(map(lambda n:n*2,list(filter(lambda n:n%2==1, dlist)))))
print(sum_all)


# Map filter Lambda and reduce function i Strings
list1=[2,3,4,4,5,6,7,8,9,10]
even = list(filter(lambda n: n%2==0,list1)) # FIlter even numbers from the list
odd = list(filter(lambda n: n%2!=0,list1)) # FIlter odd numbers from the list

print('--------------')
print(even)
print(odd)
print('---------------')

list2=['one','two','three','four']
upper =list(filter(lambda x:x.isupper(),list2))# filter upprecase strings from the list
lower =list(filter(lambda x:x.islower(),list2))# filter lowercase strings from the list

print(upper)
print(lower)
print("---------")


list3=['one','two2','three3','08','99','100']
numeric =list(filter(lambda x:x.isnumeric(),list2))# filter Numeric strings from the list
alpha =list(filter(lambda x:x.isalpha(),list2))# filter Alpha strings from the list
alnum =list(filter(lambda x:x.isalnum(),list2))# filter Numbers & Characters strings from the list

print(numeric)
print(alpha)
print(alnum)

print("----------------")


list1=['soap','sharp','shy','ship','summer','sheep']
print(list(filter(lambda x:x.startswith('s')  & x.endswith('p'),list1)))

list1=[1,2,3,4]
list2=[5,6,7,8]

def double(x):
    return x+x
def add(x,y):
    return x+y 
def square(x):
    return x*x
print("------------")
print(list(map(double,list1))) # DOuble each number using map & Usewr defined funcyion
print(list(map(add,list1,list2))) # Add two number using map & Usewr defined funcyion
print(list(map(square,list1))) # Square number using map & Usewr defined funcyion

print("------------")

print(list(map(lambda x: x+x, list1))) # DOuble each number using map & Lambda
print(list(map(lambda x,y: x+y, list2,  list1)))# add two number using map & Lambda
print(list(map(lambda x: x*x, list1))) # Square number using map & Lambda

print('-------------')





coutris=['India','Pakistan','Australia','Dubai']
print(list(map(lambda x:x.capitalize(),coutris)))


from functools import reduce
list2=[1,2,3,4]
import operator
add=reduce (operator.add,list2) # add of all numbers ina list
product=reduce (operator.mul,list2) # Product of all numbers ina list

concat_str= reduce(operator.add , ['Python',' ','Abhishek'])# Concatenate string using reduce
prid=reduce(operator.mul,('Hello', 3)) # Repeat a string multiple times
min_num = reduce(lambda a,b: a if a<b else b, list2)# Minimum numbers in the list using reduce () & lambda
max_num = reduce(lambda a,b: a if a>b else b, list2)# Maximum numbers in the list using reduce () & lambda


print(product)
print(add)
print(concat_str)
print(prid)
print(min_num)
print(max_num)




from functools import reduce
list2=[1,2,3,4]
def min_func(a,b):
    return a if a<b else b
def max_func(a,b):
    return a if a>b else b
min_num=reduce(min_func,list2) # Minimum number in the list using reduce () & User defined min function
max_num=reduce(max_func,list2) # Maximum number in the list using reduce () & User defined max function
print(min_num,max_num)
