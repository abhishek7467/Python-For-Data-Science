'''   # COllection Data Types  '''
'''                      1. List                '''

# Creating a List

l1 = [10, 20, 30, 40]
print(l1)
print(type(l1))


l2 = ['Python', 2.3, 54, 23.4, 'Abhishek', [12, 34]]
print(l2)

student = []

print('Student list is : ', student)

student = ['Abhishek Kumar', 'B.tech(CSE) ', 1904760100008]
print(f'After Modification of list : {student}')

s = 'Hello World'

# create a list from string object
l3 = list(s)
print('String is ', s)
print('List create from string is : ', l3)

l4 = list()
print('List l4 is :', l4)

print(f'The length of l1 l2, l3, l4 and student lists are : ',
      len(l1), len(l2), len(l3), len(l4), len(student))


a = 'abcdefghijklmnopqrstuvwxyz'
allist = list(a)
print('the string is : ', a)
print('the list is : ', allist)


# Accessing element form the list through the indexing

print('The Student List : ', student)
print('The First Element of list is ', student[0])
print('The Second Element of list is ', student[1])
print('The Third Element of list is ', student[2])
# print('The Fourth Element of list is ', student[3]) # This is Out Of Range

# This is negative indexing
print('The Third Element of list is ', student[-1])
print('The First Element of list is ', student[-3])


# List Slices


print(allist)

print(allist[1:4])
print(allist[5:20])
print(allist[:10])
print(allist[10:])
print(allist[::3])
print(allist[::2])
print(allist[::])  # Return all the element from the list
print(allist[::-1])  # Return  Reverse List


print('\n \n')
# Modifying List Element
newL = allist[:8]
print('This is new List derived from the allist ', newL)
newL[1] = 'cc'
print('new List     ', newL)

newL[2:4] = ['r', 'r']
print(newL)


t1 = [1, 'abhishek', 2.3]
t2 = ['Kumar', 'is', 56, 34.3]
concatenate = t1+t2
print('This is concatenated List         :          ', concatenate)
