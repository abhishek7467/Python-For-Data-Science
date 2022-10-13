'''             ::::::: WELCOME TO MY MOD MODULE   :::::::

    This Module Contain in Function 1 - modulous. 
                            Function 2 - Check Whether is even or not.  
                            Function 3 - calculate average of n numbers.. 

                            '''

def f1(num1, num2):
    print('Welcome To My  Mod Operations ')

    return print(f'The modulus of {num1} and {num2} is   :    {num1%num2} ')

def f2(num):
    print('Welcome To My  Odd Even  Operations ')
    if num%2==0:
        return print(f'The {num} is Even...')
    else:
        return print(f'The {num} is Odd...')

def f3(num):
    print('Welcome To average of n numbers. ')
    s=0
    for i in range (num):
        s+=i

    return print ('The average of n numbers is  :  ', s/num)
















