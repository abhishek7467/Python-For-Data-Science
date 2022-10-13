
'''Higher Order Function'''
'''A Function can take another as a parameter. such function are known as higher order function.'''


def apply(x,function):
    result =function(x)
    return result

def square(n):
    return n*n

print(apply(10,square))




# Function which return function as return value

def make_checker(s):
    if s=='even':
        return lambda n: n%2 ==0
    elif s=='positive':
        return lambda n: n>=0
    elif s=='negative':
        return lambda  n :n<0

f1= make_checker('even')
f2= make_checker('positive')
f3= make_checker('negative')

print('f1(3) = ' ,f1(3) )
print('f2(3) = ' ,f2(3) )
print('f3(3) = ' ,f3(3) )

# Filter Function

data=[1,3,5,2,7,4,6,9,10]
print('data : ',data)
def is_even(i):
    return i%2 ==0
#Filter for even numbers
even_data=list(filter(is_even,data))
print('The filted data is  :  ',even_data)


# MAP Function

data=[1,3,5,2,4,1,0,7]
print('Data  : ',data)

# apply the lambda function to each element in the list using the map function

d1=list(map(lambda i : i+1,data))
print('The result of map is   :  ',d1)



data1=[1,3,5,7]
data2=[2,4,6,8]
result=list(map(lambda x,y :x+y,data1 ,data2))
print('The result of map operation : ', result)




data=[1,3,5,7,4,15]
print('data  : ',data)

def square(n):
    return n*n 
result = list(map(square,data))
print('Result is  : ',result)



# rerduce Function

from functools import reduce
data= [1,3,4,67,10,6,3,7,9,0]
result = reduce(lambda total,value:total+value,data) 
print('The result of applying the reduce operation  :  ', result)
result = reduce(lambda total,value:total*value,data) 
print('The result of applying the reduce operation  * :  ', result)




