
'''                      TUPLE REVISION             '''


'''Tuple is similar to list except that the objec in tuplr are 
immutable which means we cannot change the element of a tuple 
once assigned '''


'''When we do not want to change the data over time, tuple is a preferred data types.  '''

'''Iterating over the elements of a tuple is faster compared to iterating over a list.'''


# Creating Tuple


from cmath import pi
from ctypes import Union
from os import PRIO_PGRP
tup = ()
print("Empty Tuple is : ", tup)

tup2 = (1020, 30)
print(' \n \n  tup2 ', tup2)

tup3 = (3, 14, 30, 9.1, 0.1, 345, 21, 87, 45, 23, 2.1)
print(' \n \n tup3 :', tup3)

tup4 = ('one', 'two', "Three")
print(' \n \n ', tup4)

tup5 = ('Python', 35, [34, 543], [89, 892], 'apple')
print(' \n \n  tup5 ', tup5)

tup7 = ('Python', 45, [43, 567], [123, 890], {
        'R', 'A'}, {'India ', 'NewDelhi'}, (1, 2))
print(' \n   tup7 : ', tup7)


print(' \n', tup4[0])

print(' \n', tup7[2][1])

myTuple = ('one', 'two', 'Three', 'Four', 'Five', 'SIx', 'Seven', 'Eight')

print(' \n', myTuple)
print(' \n', myTuple[0:3])
print(' \n', myTuple[2:5])
print(' \n', myTuple[:3])
print(' \n', myTuple[:2])
print(' \n', myTuple[-3:])
print(' \n', myTuple[-2:])
print(' \n', myTuple[-1])
print(' \n', myTuple[:])


del myTuple  # deletes the entire tuple

# myTuple # we have already deleted


myTuple = ('one', 'two', 'Three', 'Four', 'Five', 'SIx', 'Seven', 'Eight')

for i in myTuple:
    print(i)

# samse as
# print([i for i in myTuple])

print(myTuple.index('one'))


for i in enumerate(myTuple):  # if you want to print the index
    print(i)

myTupleDuplicate = ('one', 'two', 'Three', 'Four',
                    'one', 'two', 'one', 'Three', 'one')
print(myTupleDuplicate.count('two'))  # occurence of item  "two " in table
print(myTupleDuplicate.count('one'))  # occurence of item 'one'  in table


MyTuple3 = (23, 443, 56, 34, 76, 34, 23)
print(sorted(MyTuple3))
print(sorted(MyTuple3, reverse=True))
print(MyTuple3)  # Original will not changed new tuples are created when you sort


'''                                SETS REVISION                  '''

# Set of number, duplicate not allowed
myset = {1, 2, 3, 4, 6, 3, 2, 7, 6, 43, 2, 5, 5, 5}
print(myset)


myset2 = {1.76, 3.43, 2.32, 2.534, 23.12, 7.0}  # Set of Float Numbers
print(myset2)

myset3 = {'VS Code', 'Jupiter', 'Anaconda', 'Uranus'}  # Set of String
print(myset3)

mysst4 = {10, 20, 'Abhi', 789.87, (11, 23, 43)}  # mixed Datatypes
print(mysst4)

print(type(mysst4))
myset5 = {}  # This is Empty Dictionary
print(type(myset5))
print(myset5)

myset6 = set()  # This is Empty set
print(myset6)
print(type(myset6))


my_set1 = set(('one', 'two', 'three', 'four'))
print(my_set1)


myset = {'one', 'two', 'Three', 'Four', 'one', 'two', 'one', 'Three', 'one'}
print(myset)
print(type(myset))

myset = {'one', 'two', 'Three', 'Four',
         'five', 'seven', 'eight', 'nine', 'ten'}
for i in myset:
    print(i)

for i in enumerate(myset):
    print(i)
print(myset)

myset = {'one', 'two', 'Three', 'Four',
         'five', 'seven', 'eight', 'nine', 'ten'}
myset.add('NINE')  # add one element at a time using add() method
print(myset)

# add  more than one element at a time using update() method
myset.update('TEN', 'ELEVEN', 'TWELVE')
print(myset)

myset.remove('NINE')  # remove item in a set uding remove () method

print(myset)

myset = {'one', 'two', 'Three', 'Four',
         'five', 'seven', 'eight', 'nine', 'ten'}
myset.discard('Three')  # remove item from a set using discard() method
myset.discard('Four')  # remove item from a set using discard() method
print(myset)


myset.clear()  # DElete all items in a set
print(myset)

# del myset # Delete the set object we have already deleted
# print(myset)

Newset = {'one', 'two', 'Three', 'Four', 'Five', 'SIx', 'Seven', 'Eight'}
print(Newset)

myset1 = Newset  # Create a new refrence "Newset"
print(myset1)

Newset = {'one', 'two', 'Three', 'Four', 'Five', 'SIx', 'Seven', 'Eight'}
my_set = Newset.copy()  # create  a copy of list
print(my_set)

Newset.add('nine')
print(Newset)

print(myset1)

print(my_set)


A = {1, 3, 5, 2, 1}
B = {1, 12, 3, 4, 6, 5}
C = {12, 3, 7, 6, 5}

print(A | B)
print(A.union(B))
print(A.union(B, C))

print(A.update(B, C))


a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a & b)

print(a.intersection_update(b))

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A-B)

print(A.difference(B))

print(A ^ B)

A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
B = {3, 4, 5, 6, 7, 8}
C = {10.20, 30, 40}

print(B.issubset(A))
print(A.issuperset(B))
print(C.isdisjoint(A))

print(sum(A), max(A), len(A), min(A))


D = sorted(A, reverse=True)
print(D)
