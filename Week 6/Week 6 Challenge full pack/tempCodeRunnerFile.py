

info='''
        f1 contains Mod Opration
        f2 contains Even Operation
        f3 contains Average of the Numbers 
'''
print(info)
#This is form Three to import module
from mod import *
print('This form one to import module')
num1=float(input(' Enter First Number for Mod  : '))
num2=float(input(' Enter Second Number for Mod : '))
f1(num1,num2)

num= int(input('Enter Number for Check number is Even or not    :       '))
f2(num)

num= int(input('Enter Number for calculate average of n numbers :       '))
f3(num)


