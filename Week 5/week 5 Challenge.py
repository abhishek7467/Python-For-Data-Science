# Question 1

'''
Write a function that takes the lengths of the two shorter sides of 
a right triangle as its parameters. Return the hypotenuse of the triangle, 
computed using Pythagorean theorem, as the function’s result.


'''



import math
def main():
    print('This will Calculate hypotenuse of the triangle...')
    len1=float(input('Enter lengths of shorter side 1 :  '))
    len2=float(input('Enter lengths of shorter side 2 :  '))
    if len1>0 and len2>0 :
        func=HypotenuseTriangle(len1,len2)
        print(f"The length of the hypotenuse is: {func}")
    else:
        print('The both variable side1 and side should be positive or greater than 0. ')


def HypotenuseTriangle(side1,side2):

    a=side1*side1
    b=side2*side2 
    res=math.sqrt(a+b)
    return res

if __name__ =="__main__":
    main()



# Question 2 
'''

An online retailer provides express shipping for many of its items at a rate of $10.95 
for the first item, and $2.95 for each subsequent item. Write a function that takes the 
number of items in the order as its only parameter. Return the shipping charge for the 
order as the function's result. Include a main program 
that reads the number of items purchased from the user and displays the shipping charge.

'''
def main():
    print('This will calculate shipping Charge.  $10.95 Price for the first item, and $2.95 for each subsequent item  ')
    name=input('Enter Your Name : \t ')
    number_of_items_In_Order=int(input('Enter number of items for  the order : \t '))
    charge=ShippingCharge(number_of_items_In_Order)
    print(f' {number_of_items_In_Order} purchased By {name}. \n The Shipping Charge is : ${charge} .')
      

def ShippingCharge(number_of_items):
    On_fisrt_Item = 10.95 
    On_each_Subsequent_Item=2.95
    Shipping_Charge_For_Order=On_fisrt_Item+(On_each_Subsequent_Item*(number_of_items-1))
    return Shipping_Charge_For_Order



if __name__ =="__main__":
    main()









# Question 3

'''
Write a function that takes three numbers as parameters, and 
returns the median value of those parameters as its result. Include 
a main program that reads three values from the user and displays their median.

'''
def main():
    print('This will Calculate Median Of the Value ')
    num1=float(input('Enter First Number  : \t '))
    num2=float(input('Enter Second Number  : \t '))
    num3=float(input('Enter Third Number  : \t '))

    median=MedianValue(num1, num2, num3)
    print(f' The median of {num1}, {num2} and {num3} is  {median}')


def MedianValue(num1,num2,num3):
    if num1>num2:
        if num1<num3:
            medianVal=num1
        elif num2>num3:
            medianVal=num2
        else:
            medianVal=num3 
    else:
        if num1>num3:
            medianVal=num1
        elif num2<num3:
            medianVal=num2
        else:
            medianVal=num3

    return medianVal


if __name__ =="__main__":
    main()









# Question 4

'''
Write a function that determines whether or not three lengths can form a triangle. 
The function will take 3 parameters and return a Boolean result. 
In addition, write a program that reads 3 lengths from the user 
and demonstrates the behavior of this function. 
In general, if any one length is greater than or equal to the sum of the other two then 
the lengths cannot be used to form a triangle.
Otherwise they can form a triangle.
'''

def main():
    print('This will determines whether or not three lengths can form a triangle.   ')
    a=float(input('Enter First Number  : \t '))
    b=float(input('Enter Second Number  : \t '))
    c=float(input('Enter Third Number  : \t '))


    result=Triangle(a, b, c)
    if result==True:
        print(f' {result} - The Triangle is in a form and The side of of triangle is {a}, {b},  {c}.  ')
    else:
        print(f' {result} - The Triangle is not in a form and The side of of triangle is {a}, {b},  {c}.  ')
def Triangle(a,b,c):
    if( ((a+b)<=c) or ((b+c)<=a) or ((c+a)<=b) ): 
        return False
    else:
        return True


if __name__ =="__main__":
    main()





# Question 5 
''' 
In this exercise you will write a function named isInteger that determines 
whether or not the characters in a string represent a valid integer. 
When determining if a string represents an integer you should ignore 
any leading or trailing white space. Once this white space is ignored, 
a string represents an integer if its length is at least 1 and it only contains digits, 
or if its first character is either + or - and the first character is followed by one
 or more characters, all of which are digits. Write a main program that reads 
 a string from the user and reports whether or not it represents an integer.
 
'''
def main():
    print('This will determines whether or not  string represents an integer   ')
    str1=input('Enter First Number  : \t ')
    if isInteger(str1):
        print('The string represents an integer.')
    else:
        print('The string is not represents an integer.')


def isInteger(str1):
    str1 = str1.strip()
    if (str1[0]=='+' or str1[0]=='-') and str1[1:].isdigit():
        return True
    if str1.isdigit():
        return True

    return False
if __name__ =="__main__":
    main()









# Question 6 

'''

In this exercise you will create a function named nextPrime that finds and 
returns the first prime number larger than some integer, n. 
The value of n will be passed to the function as its only parameter. 
Include a main program that reads an integer from the user and displays 
the first prime number larger than the entered value.
 

'''

def main():
    print('This will first prime number larger than some integer, n. ')
    num1=int(input('Enter  Number  : \t '))
    nextprime(num1)

def nextprime(n):
    prime=0
    n+=1
    for i in range(2,int(n**0.5)+2):
        if n%i==0:
            prime=0
            break
        else:
            prime=1
    if prime==1:
        print(n)
        return n
    else:
        nextprime(n)
        return n     
if __name__ == '__main__':
    main()




# Question 7 



'''
In this exercise you will write a function that determines 
whether or not a password is good. We will define a good password to be a one 
that is at least 8 characters long and contains at least one uppercase letter,
at least one lowercase letter, and at least one number. Your function should 
return true if the password passed to it as its only parameter is good. 
Otherwise it should return false. Include a main program that reads a 
password from the user and reports whether or not it is good.'''



def   checkPassword(password):
   has_upper   = False
   has_lower   = False
   has_num  = False

   for   ch  in  password:
      if  ch  >=  "A"   and   ch  <=  "Z":
         has_upper   = True
      elif ch  >=  "a"   and   ch  <=  "z":
         has_lower   = True
      elif ch  >=  "0"   and   ch  <=  "9":
         has_num  = True

   if len(password) >= 8 and has_upper and has_lower and has_num:
      return    True

   return    False

def   main():
    p  = input ("Enter      a  password:     ")
    worn='''Worning : 
                    1. A good password contains at least 8 characters long.
                    2. A good password contains at least one uppercase letter.
                    3. A good password contains at least one lowercase letter.
                    4. A good password  at least one number'
            '''      
    if  checkPassword(p):
        
        print ("That's      a  good   password.")
    else :
        print ("That      isn't   a  good   password.")
        print ("\n",worn)
if  __name__   == "__main__":
   main()













# Question 8
'''
Write a program that reads values from the user until a blank 
line is entered. Display the total of all of the values entered by the user 
(or 0.0 if the first value entered is a blank line). 
Complete this task using recursion. Your program may not use any loops. 
The body of your recursive function will need to read one value from the user, 
and then determine whether or not to make a recursive call. Your function 
does not need to take any parameters,
but it will need to return a numeric result.'''



def myFunction():
    num=input('Enter Your Number : \t')
    if  num=="":    
        return 0.0
    else:
        n=int(num)
        return (n+myFunction())

def main():
    print('Total of all the values = ',myFunction())

if  __name__   == "__main__":
   main()         



#  Question 9


'''
In this exercise you will write a recursive function that determines whether 
or not a string is a palindrome. The empty string is a palindrome, 
as is any string containing only one character. 
Any longer string is a palindrome if its first and last characters match, 
and if the string formed by removing the first and last characters is also a palindrome. 
Write a main program that reads a string from the user. Use your recursive function to 
determine whether or not the string is a palindrome. 
Then display an appropriate message for the user.
'''


def  isPalindromeStr(s):
    if   len (s)    <=  1:
        return True
    return  s[0] == s[len (s)  - 1] and isPalindromeStr(s[1 : len (s) - 1])


def main():

    str1=input('Enter Your String to check is palindrom or not  :  \t')
    if   isPalindromeStr(str1):
        print (f"That   '{str1}'  is  a  palindrome!")
    else :
        print (f"That  '{str1}'  is   not   a  palindrome.")

if  __name__   == "__main__":
   main()         




# Question 10  

'''
Write a function that takes a list of strings as its only parameter. 
Your function should return a string that contains all of the items in
the list formatted in the manner described previously as its only result.
While the examples shown previously only include lists containing four elements
or less, your function should behave correctly for lists of any length. Include a 
main program that reads several items from the user, formats them by calling your 
function, and then displays the result returned by the function. Consider the following 
four lists:

apples

apples and oranges

apples, oranges and bananas

apples, oranges, bananas and lemons

'''


def formatList(items):
    if len(items) == 0:
        return "<empty>"
    if len(items) == 1:
        return str(items[0])
    result = ""
    for i in range(0, len(items) - 2):
        result = result + str(items[i]) + ", "

    result = result + str(items[len(items) - 2]) + " and "
    result = result + str(items[len(items) - 1])
    return result

def main():
    items = []
    line = input("Enter an item (blank to quit): ")
    while line != "":
        items.append(line)
        line = input("Enter an item (blank to quit): ")
    print("The items are ",  formatList(items),' . ')

if  __name__   == "__main__":
   main() 

