'''             Iterators                   '''

# Program to implement an iterator called Even that returns the evrn numbers the even numbers pto a limit

from typing_extensions import Self


class Evens:
    def __init__(self,l):
        self._limit=l
        self._val=0

    # he __iter__ method makes his class iterable

    def __iter__(self):
        return self
    
    # The __next__ method makes this class an iterator

    def __next__(self):
        if self._val>self._limit:  
             raise StopIteration
        else:
            return_val=self._val
            self._val+=2
        return return_val

print('Start iterator  ')
n=int(input('Enter the limit  :  '))
print('Event from 0 to 20')
for i in Evens(n):
    print('i = ',i)
print('ENd of the iterator')



# Program to accept a value of n. Implement an iterator which returns factorials upto n

class fact:
    def __init__(self,l):
        self._limit=l
        self._val=0

    def __iter__(self):
        return self 
    
    # FInd the factorial of num 
    def fact(self,num):
        prod=1
        for i in range(1,num+1):
            prod*=i
        return prod
    def __next__(self):
        if self._val>self._limit:
            raise StopIteration
        else:
            return_val = self.fact(self._val)
            self._val+=1
            return return_val

print('Start Iterator')
print('Facctorials from 1 to n')
n = int(input('Enter the limit (n greater then 1) :'))

for i in fact(n):
    print('Factorial = ', i)

print('End of Iterator')
































