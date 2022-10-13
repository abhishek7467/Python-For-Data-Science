'''             ::::::: WELCOME TO MY MODULE   :::::::

    This Module Contain in Function 1 - Arithmetic Operations. 
                            Function 2 - String Operations. 
                            Function 3 - File Creating Operation. 
                            '''


def ArithmeticOperationFunction1(num1,num2):
    print('Welcome To My  Arithmetic Operations ')
    def addition(num1,num2):
        print('\nusing the addition operator')
        res = num1 + num2
        return print(f' The addition of {num1} , {num2} is {res}')
    
    
    def Substraction(num1,num2):
        print('\n using the Substraction operator')
        res = num1 - num2
        return print(f' The Substraction of {num1} , {num2} is {res}')
        
    def Multiplication(num1,num2):
        print('\nusing the Multiplication operator')
        res = num1 * num2
        return print(f' The Multiplication of {num1} , {num2} is {res}')
    def division(num1,num2):
        print('\nusing the division operator')
        res = num1 / num2
        return print(f' The division of {num1} , {num2} is {res}')
    def flooreDivision(num1,num2):
        print('\nusing the floore oprator operator')
        res = num1 // num2
        return print(f' The floore Division of {num1} , {num2} is {res}')
    addition(num1,num2)
    Substraction(num1,num2)
    Multiplication(num1,num2)
    division(num1,num2)
    flooreDivision(num1,num2)


def StringOperationsFunction1(string):
    print('Welcome To My  String Operations ')
    def Capital(string):
        return print(f'\n The first character to upper case ',string.capitalize())
    def Isnumer(string):
        return print(f'\n This string is digit :  ',string.isdigit())
    def  IsTitle(string):
        return print('\nThis string contains Title : ',string.istitle())
    def LesngthStr(string):
        return print('\nThe length of the string is ', len(string))
    def Reverse(string):
        return print('\nThe reverse  string is ', string[::-1])
    
    def UPPERcase(string):
        return print('\nThe Upper   string is ', string.upper())
    
    def Reverse(string):
        return print('\nThe lower  string is ', string.lower())
    def Split(string):
        return print('\nThe split  string is ', string.split())

    def Latter(str1):
        name=input('Enter Your Name : ')
        print(str1.replace('name1', name))

    Reverse(string)
    Capital(string)
    Isnumer(string)
    IsTitle(string)
    Reverse(string)
    UPPERcase(string)
    LesngthStr(string)
    Split(string)
    str1=''' Hey name1
                Greetings from Skill-Lync! 
                You are now successfully enrolled for the course Core and Advanced Python Programming
                With Skill-Lync, you are guaranteed a smooth learning experience that sets you on the path for a successful career. 
                If you are visiting for the first time, you can go through the log-in steps
                You can reach out to us anytime if you have any questions or concerns at support@skill-lync.com.

                Thank You,
                Team SKILL-LYNC
        '''
    Latter(str1)
def FileCreatingOperationFunction1(filename):
    print('Welcome To My  File Operations ')
    f1=open(filename,'w')
    f2=filename
    content=input('Enter your content with press the enter button (0 to exit)  :  ')
    while content!='0':
        content=content+'''
        '''
        
        f1.write(content)
        content=input('Enter your content with press the enter button (0 to exit)  :  ')
    f1.close()
    f1=open(filename,'r')

    print('The Content of file is : ',f1.read())
    
    # f2=open(f2,'r')
    # for i in f2:
    #     print(i,end=" ")





