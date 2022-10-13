## Question -1
'''1. A set contains names which begin either with A or with B.
 Write a program to separate the names into two sets,
 one containing names beginning with A and the other containing names beginning with B'''


set1={'Abhishek','Bhavna','Baasu','Ankit','Bamamula','Ankur'}
print(f'The set contains names which begin either with A or with B::  \n \t{set1} ')

startwithA=set()
strtAl=list(startwithA)
startwithB=set()
strtBl=list(startwithB)
for i in set1:
    if i.startswith('A'):
        strtAl.append(i)  
                   
    else:
        strtBl.append(i) 
startwithA=set(strtAl)
startwithB=set(strtBl)
print(f'\n containing names beginning with A  :   {startwithA}')
print(f' containing names beginning with B  :   {startwithB}')



## Question 2
''' Create a list of tuples. Each tuple should contain an item and 
its price in float.
Write a program to print each item and its price in a proper format '''

price = [('Laptop', '50000.67'), ('Book', '341.78'), ('Pen ','12.23'),('Keyboard ','412.3'),('Mouse','300.43'),('Computer Cable','456.4'),('Mobile','10056.4'),('Software ','950.4'),('Window  ',' 10000.4'),('Computer chips','35000.4')]
print(sorted(price, key=lambda x: float(x[1])))


## Question 3
'''Write a program that reads integers from the user and stores them in a list. 
Your program should continue reading values until the user enters 0. 
Then it should display all of the values entered by the user (except for the 0)
in order from smallest to largest, with one value appearing on each line. 
Use either the sort method or the sorted function to sort the list.'''



list1=[]

num = int(input('Enter Number your number : \t '))    
while num!=0:    
    print('')
    num = int(input('Enter Number your number : \t '))    
    list1.append(num)
    print(f'Your Value is {num}')
    
print(' You are enterd 0 Value. \n  Exit...')
print(f'\nYour List is {list1}')
list2=sorted(list1)
print('\nYour List Sorted in ascending order using sorted Method : ', list2)
print('\nYour List in Descending orer : ',list2[::-1])

    
print('Using sort method',list1.sort())
print('The sort function  return only "none" value..  ')





## Question 4
''' 
Write a program to read a list of numbers from the user and remove the two largest and two smallest values from it. 
Display the list with the values removed, followed by the original list. 
Your program should generate an appropriate error message if the user enters less than 5 values. '''


list1=[]       
num=int(input('Enter Number your number : \t '))
while num>5:
    num = int(input('Enter Number your number : \t '))  
     
    list1.append(num)
print('')
print(list1)
removList=[]
try:
    list2=sorted(list1)
    print(list2)
    removList.append(list2.pop(0))
    removList.append(list2.pop(0))
    removList.append(list2.pop()) 
    removList.append(list2.pop())
    print('The final list is : ',list2)
    print('The  list Contain only removed item form the original list  : ', sorted(removList))
except:
    print('\nYou can not Enter less than 5 Value. \nExit........')



                                                                                        

## Question 5
'''
In this exercise, you will create a program that reads words from the user until the user enters a blank line. 
After the user enters a blank line your program should display each word entered by the user exactly once.
'''
 
words=[]
word = input('Enter a word (blank line to quit ) : \t')
while word!="":
    if word not in words:
        words.append(word)
    word = input('Enter a word (blank line to quit ) : \t')
print("You are entered blank line. \nExit....... ")
for word in words:
    print(word)





# Question - 6 
''' Write a program that reads numbers from the user until a 0 is entered. 
Your program should display the average of all of the values entered by the user. 
Then the program should display all of the below average values, 
followed by all of the average values (if any), followed by all of the above average values. 
An appropriate label should be displayed before each list of values. '''

list1=[]       
Sum=0
count=1
num=int(input('Enter Number your number : \t '))
while num!=0:
    num = int(input('Enter Number your number : \t '))       
    list1.append(num)
    Sum+=num 
    count+=1
avg=Sum/count
print('The average is : ', avg)
lesslist=[]
greatlist=[]
for i in list1:
    if i<avg:
        print('These value are below from avereage value : ', i)
        lesslist.append(i) 
    else:
        print('These value are above from  avereage value : ', i)
        greatlist.append(i) 
print('The average is : ', avg)
print('the value of this list is below from avereage value : ', lesslist)       
print('the value of this list is anove from avereage value : ', greatlist) 




## Question 7
''' Create a program that determines and displays the number of unique characters in a string entered by the user. 
For example, Hello World! has 9 unique characters while zzz has only one unique character. 
Use a dictionary to solve this problem.'''
str1=input('Enter the string : \t')
dict1={}
for i in str1:
    if i.isalpha():
        dict1[i]=1
print(dict1)
print('Unique Character is : ',len(dict1))
print('The Unique Dictionary is :  ',dict1)





## Question 8
''' Two words are anagrams if they contain all of the same letters, but in a different order. For example,
 “evil” and “live” are anagrams because each contains one e, one i, one l, and one v.
  Create a program that reads two strings from the user,
 determines whether or not they are anagrams, and reports the result.'''
str1=input('Enter the string : \t')
str2=input('Enter the string : \t')


if str1[::-1]==str2:
    print(f'Both words are anagrams. The words are {str1} and {str2}')
else:
    print(f'Both words are not anagrams. The words are {str1} and {str2}')





## Question 9
'''An integer, n, is said to be perfect when the sum of all of the proper divisors of n is equal to n. 
For example, 28 is a perfect number because its proper divisors are 1, 2, 4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28. 
Write a program that determines whether or not a positive integer is perfect. Your program will accept a number from the user.
 If that number is a perfect number then your program will display true. 
Otherwise it will display false.'''

num=int(input('Enter your Number to check the  sum of all of the proper divisors of n is equal to n :  \n\t'))
Sum=0
for i in range(1,num):
    if num%i==0:
        Sum=Sum+i
        print(i)
if Sum==num:
    print(f'The sum of all of the proper divisors of {num} is {Sum} :  TRUE ')
else:
    print(f'The sum of all of the not a proper divisors of {num} is {Sum} :  FALSE ')



## Question 10
''' Write a program that finds all of the keys in a dictionary that map to a specific value. 
The program will take the value to search for as its input. 
It will display a (possibly empty) list of keys from the dictionary that map to the provided value.'''



mydict1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50,'f':'', 'g':"",'h':10,'i':''}
print(mydict1.keys()) 
print(mydict1.values())
blanklist=[]
UNblanklist=[]
skey=input('Enter the key to find the value from the dictionary : ')
skey=input('Enter the key to find the value from the dictionary : ')
for key,value in mydict1.items():
    if key == skey:
        if value=="":
            blanklist.append(value)
        else:
            UNblanklist.append(value)
        print("Value by key:",value)
sval=int(input('Enter the key to find the value from the dictionary : '))
for key,value in mydict1.items():
    if value == sval:    
        print("key by value:",key)





