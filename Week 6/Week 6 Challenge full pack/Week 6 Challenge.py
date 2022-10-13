# Question 1 
'''
Write a program that read contents of the file ‘messages’
 one character at a time and prints each character that is read.

'''
"""
message_contain_in_text_File='''
Hii, Good Morning..
This is Abhishek Kumar.
Welcome to Python /....
How can help you?
This is the message to you from Abhishek Kumar..
'''
"""
readfile=open('.\Week 6\message.txt','r')
str1=''
for i in readfile:
    str1+=str(i)
print(f'This is whole message :  " {str1} "')
for i in str1:
    print(f'This is One Character at a time from the message :  " {i} " ')
readfile.close()






# Question 2 

'''
Write a Python program that searches for a file, obtains its size and 
reports the size in bytes/ KB/ MB as appropriate

'''



from pathlib import Path

def convert(num):
    for x in ['bytes','KB','MB','GB']:
        if num<1024.0:
            return(num, x)
        num/=1024

def FileName(file_path):
    file_size = Path(file_path).stat().st_size
    return  convert(file_size)
file_name =input('Enter  the filename  :  '   )
print('Enter your path like - E:\Telegram Desktop\Shiddat (2021) Hindi 720p WEBRip DSNP x264 AAC 800MB - ShortRips (1).mkv ')
print('The size of the file is  : ',FileName(file_name))









# QuesTion 3 
'''
Write a program to accept a filename from the user, create a file with that
 name(if it does not exist) and write some content into the file

'''
# Random File Access 
fileName=input('Enter The name of file with extension  :   ')
try:
    f=open(fileName,'x')
    content=input('What you write in the file  :  ')
    f.write(content)
    print('     ::::The content of file is ::::      ')
    with open (fileName,'r') as f:
        for line in f:
            print(line,end=' ')

    f.close()
except FileExistsError:
    print(f'{fileName} File is already exists..')

fileName.close()



# Question 4
'''
Write a program to read a file and display 
its contents along with line numbers before each line

'''


fileName=input('Enter The name of file ( read a file ) :   ')
m=1
with open (fileName,'r') as f:
    for line in f:
        print(f'{m} --> {line}')
        m+=1    

fileName.close()









# Question 5 
'''
Write a program to 
copy the contents of one file into another

'''

AlreadyContentName=input('Enter The name of file (in which contains content for the copy ) :   ')
EmptyName=input('Enter The name of file ( Empty File ) :   ')

emptFile=EmptyName
AlreadyFileName= open(AlreadyContentName,'r')
EmptyFile=open(EmptyName,'w')
print(f'The Content in file {AlreadyFileName}')
print('\n')
for i in AlreadyFileName:
    print(i,end=" ")
    EmptyFile.write(i) 
AlreadyFileName.close()
EmptyFile.close()
print("*"*50)
print('\n')
EmpFile=open(emptFile,'r')
print(f'The Content in file {EmpFile}')
for line in EmpFile:
    print(line, end=" " )







# Question 6
'''
Write a program to append the contents of one file into another
'''
firstfile = input("Enter the name of first file(must file exist) ")
secondfile = input("Enter the name of second file(must file exist) ")
f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')
print('content of first file before appending -', f1.read())
print('content of second file before appending -', f2.read())
f1.close()
f2.close()
f1 = open(firstfile, 'a+')
f2 = open(secondfile, 'r')
f1.write(f2.read())
f1.seek(0)
f2.seek(0)
print('content of first file after appending -', f1.read())
print('content of second file after appending -', f2.read())
f1.close()
f2.close()




# Question 7
'''
Suppose a file contains student records, with each record 
containing name and age of student. Write a program to read 
these records and display them in sorted order by name

'''

firstfile = input("Enter the name of first file(must file exist) ")
f1=open(firstfile,'r')
a=sorted(f1)
for i in a:    
    print(i)


# Question 8 
'''
Suppose there are three modules m1.py, m2.py and m3.py 
containing functions f1(), f2() and f3() respectively.
 Write a program to use these functions

'''
from myPackA import m1
from myPackA import m2
from myPackA import m3 

num1=float(input(' Enter the First Number : '))
num2=float(input(' Enter the Second Number : '))

print("The Addition from f1 is define in m1 ", m1.f1(num1,num2))
print("The Addition from f2 is define in m2 ", m2.f2(num1,num2))
print("The Addition from f3 is define in m3 ", m3.f3(num1,num2))
print('\n')

print('The name of the module m1 is  :   ', m1.__name__)
print('The Docstring of the module m1 is  :   ', m1.__doc__)
print('The nname of the file of the module m1 is  :   ', m1.__file__)
print('\n')

print('The name of the module m2 is  :   ', m2.__name__)
print('The Docstring of the module m2 is  :   ', m2.__doc__)
print('The nname of the file of the  m2 module is  :   ', m2.__file__)
print('\n')

print('The name of the module m3 is  :   ', m3.__name__)
print('The Docstring of the module is m3  :   ', m3.__doc__)
print('The nname of the file of the module m3 is  :   ', m3.__file__)


#  Question 9 
'''
Write a program containing functions fun1(), fun2() and fun3() and some statements.
Add suitable code to the program such that you can use it as a module or a normal program

'''


from myPackA import func_1_2_3
num1=float(input(' Enter First Number for perform various Arithmatic operation on your Number : '))
num2=float(input(' Enter Second Number for perform various Arithmatic operation on your Number : '))
func_1_2_3.ArithmeticOperationFunction1(num1,num2)

from myPackA import func_1_2_3
str1=input('Enter your string for perform various operation on your string   ')
func_1_2_3.StringOperationsFunction1(str1)

from myPackA import func_1_2_3
fname=input('Enter your file name   ')
func_1_2_3.FileCreatingOperationFunction1(fname)






# Question 10 
'''
Suppose a module called mod.py contains functions f1(), f2() and f3(). 
os.write three forms of import statements to use these functions in your program 
'''


info='''
        f1 contains Mod Opration
        f2 contains Even Operation
        f3 contains Average of the Numbers 
'''
print(info)
# This is form one to import module 
import mod
print('This form one to import module')
num1=float(input(' Enter First Number for Mod  : '))
num2=float(input(' Enter Second Number for Mod : '))
mod.f1(num1,num2)

num= int(input('Enter Number for Check number is Even or not    :       '))
mod.f2(num)

num= int(input('Enter Number for calculate average of n numbers :       '))
mod.f3(num)





info='''
        f1 contains Mod Opration
        f2 contains Even Operation
        f3 contains Average of the Numbers 
'''
print(info)

# This is form Two to import module
from mod import f1 
from mod import f2 
from mod import f3 

print('This form Two to import module')
num1=float(input(' Enter First Number for Mod  : '))
num2=float(input(' Enter Second Number for Mod : '))
f1(num1,num2)

num= int(input('Enter Number for Check number is Even or not    :       '))
f2(num)
num= int(input('Enter Number for calculate average of n numbers :       '))
f3(num)



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





































