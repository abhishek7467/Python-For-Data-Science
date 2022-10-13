##  Question - 1 
# 1. Write a program to accept an integer n greater than 10. Then print all the odd numbers from 1 to n.



num = int(input('Enter Number your number : \t '))
if num>10:
    for i in range(num):
        if  i%2==1 : 
                print(f'The Even number is  : {i}')
else:
    print('You are entered number less than 10. Please try again')



##  Question - 2
# 2. Write a program to accept an integer n greater than 10. Then print all the prime numbers from 1 to n.
num = int(input('Enter Number your number : \t '))
if num>10:
    for i in range(num):            
            n = i
            for j in range(2, n):
                if (n % j) == 0:
                    break
            else:
                print('The prime number is : ', n)
else:
    print('You are entered number less than 10. Please try again')





##  Question - 3
#3. In this exercise you will create a program that computes the average of a collection of values entered by the user. 
#The user will enter 0 as a sentinel value to indicate that no further values will be provided. Your program should display an appropriate error message if the first value entered by the user is 0.
Sum=0
n= int(input('Enter Number your number : \t '))
for i in range(n+1):    
    zero=0
    num = int(input('Enter Number your number : \t '))    
    if (i==0 and zero==num):    
        print('You can not enter first value 0. Enter your first non-zero ')
        break
    else:
        Sum=Sum+num
print('Sum is : ',Sum)
avg=Sum/num
print(f'The average of {num} is :  {avg}')


##  Question - 4
# 4. Write a program that takes a number as input and prints its multiplication table. 
num= int(input('Enter Number your number : \t '))
print(f" The table of {num}")
for i in range(1,11):
    print(f" {i} * {num} = {i*num} ")







##  Question - 5
#5. Write a program that displays a temperature conversion table for degrees Celsius and degrees Fahrenheit. The table should include rows for all temperatures between 0 and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate headings on your columns.


print(' \n\ \n \n \n \t \t \t  Fahrenheit and convert into  Centigrade')
for i in range(0,101):
    Cetigrate = 5/9 * (i-32)

    print(f" Temperaure in Fahrenheit is {i} and convert into Centigrade  = {Cetigrate}")
    print(f"\n Temperaure in Fahrenheit is {i} and convert into Centigrade and that are multiples of 10 degrees Celsius. : {Cetigrate*10} \n ")

print(' \n\ \n \n \n \t \t \t    Centigrade and convert into Fahrenheit ')

for i in range(0,101):
    Fahrenheit_Out = i * (9/5)+32
    print(f" Temperaure in Centigrade {i} and convert into  Fahrenheit = {Fahrenheit_Out} \n")







##  Question - 6
# 6. A string is a palindrome if it is identical forward and backward. For example “anna”, “civic”, “level” and “madam” are all examples of palindrome words. Write a program that reads a string from the user and uses a loop to determine whether or not it is a palindrome. Display the result, including a meaningful output message.
str1=input(' Enter your words for check string is palindrome  :  \t')
rev=str1[::-1]
print('The reverse string is : ', rev)
for i in range (len(str1)):
    if str1[i]==rev[i]:
        print(f'The Word {str1} is a palindrome.')
        break
    else:
        print(f'The Word {str1} is not a palindrome.')
        break

    

##  Question - 7
'''
7. The greatest common divisor (GCD) of two positive integers, n and m, is the largest number, d, which divides evenly into both n and m. The following algorithm is used to find GCD of n and m :

Initialize d to the smaller of m and n.
While d does not evenly divide m or d does not evenly divide n do
Decrease the value of d by 1
Report d as the greatest common divisor of n and m

Write a program that reads two positive integers from the user and uses this algorithm to determine and report their greatest common divisor.

'''
num1= int(input('Enter Number1 your number : \t '))
num2= int(input('Enter Number2 your number : \t '))
d=min(num1,num2)
print(d)
while num1%d!=0 or num2%d!=0:
    d=d-1
    print(d)
print(f' The {d} as the Greatest common divisor of {num1}  and {num2}')

##  Question - 8
'''
The prime factorization of an integer, n, can be determined using the following steps:

Initialize factor to two
While factor is less than or equal to n do
If n is evenly divisible by factor then
           Conclude that factor is a factor of n
           Divide n by factor using integer division
Else
Increase factor by one

Write a program that reads an integer from the user. If the value entered by the user is less than 2 then your program should display an appropriate error message. Otherwise your program should display the prime numbers that can be multiplied together to compute n, with one factor appearing on each line.

'''
num= int(input('Enter Number1 your number : \t '))
import math 
if num<2 :
    print('You are entered the value is less than 2. Please try again...')
else:
    while num % 2 == 0:  
        print(2,)  
        num = num / 2    
    for i in range(3, int(math.sqrt(num)) + 1, 2):   
        while num % i == 0:  
            print(i,)  
            num = num / i  
    if num > 2:  
        print(num)    




##  Question - 9
'''
Write a program that converts a binary (base 2) number to decimal (base 10). Your program should begin by reading the binary number from the user as a string. Then it should compute the equivalent decimal number by processing each digit in the binary number. Finally, your program should display the equivalent decimal number with an appropriate message.

'''
# binary to decimal

num = input("Enter the string as binary like(1000111) : \t")
dec_value = 0
base1 = 1
len1 = len(num)
for i in range(len1 - 1, -1, -1):
	if (num[i] == '1'):	
		dec_value += base1
	base1 = base1 * 2
print(dec_value)
if dec_value==0:
    print('Your value is wrong')


##  Question - 10
# 10. Demonstrate the formatting capabilities of format function on integers, floats and strings.


# format function on integers
a=10
b=12
print(f'the sum of {a} and {b} is {a+b}') 
print(' sum  of  {}  and   {} is {} '.format(a,b,a+b))
print(' sum of {2} and {1} is {0}'.format(a+b, a, b))



# format function on Floats
a=12
b=6
print(f'the sum of {a} and {b} is {a/b}') 
print(' sum  of  {}  and   {} is {} '.format(a,b,a/b))
print(' sum of {2} and {1} is {0}'.format(a/b, a, b))
print('sum  of {0:10.2f} and {1:10.2f}  is {2:11.2f} '.format(a,b,a/b))


# format function on String
name='Abhishek Kumar'
middle='is a'
last='good boy.'
print(f' {name}  {middle}  {last}  ')
print(' {}  {}  {}  '.format(name, middle, last))
print(' {0} {1} {2}'.format(name, middle, last))