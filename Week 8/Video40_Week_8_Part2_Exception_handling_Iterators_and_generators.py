'''                    Exception Handling                   '''

from turtle import pensize


def runclac(x):
    x/0
    
try:
    runclac(6)

except ZeroDivisionError:
    print('Zero Division Error in runcalc function ') # Exception Handler



# here is not raised 
def runclac(x):
    x/1
    
try:
    runclac(6)

except ZeroDivisionError:
    print('Zero Division Error in runcalc function ') # Exception Handler








# Multiple  Exception Handler 

def runclac(x):
    x/0

try:
    runclac(6)

except ZeroDivisionError as z:
    print(z, ' Zero Division Error in runcalc function ') # Exception Handler 1

except IndexError as i:
    print(i , ' Error has occurred') # Exception Handler 2
except FileNotFoundError as f:
    print(f , ' Error has pccurred')# Exception Handler 3

except Exception:
    print(' An unkown error has occurred') # Exception Handler 4





def my_func(x,y):
    print('Enter my function')
    result=x/y
    print('Exiting my Function')
    return result

print('Satrting........')
try:
    print('Before fuction call.......')
    res= my_func(6,0)
    print('The result returned is : ', res)
    print('After the function call.')
except ZeroDivisionError as exp:
    print(exp , ' error has raised.' )

print('END.......')





try:
    my_func(6,0)
except IndexError as e:
    print(e)
except:
    print('Something went wrong.......')
















































































