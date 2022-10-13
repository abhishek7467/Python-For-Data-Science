'''Adding and Removing Element from a List'''


t = [1, 'abc', 2.3, 'x', 'y', 123, 'abhishek']
print(t)

# x=input('En?ter something :  ')
# t.append(x)
print('The list t after adding the element is   :   ', t)


t.insert(2, 'Kumar')
print('The list t after inserting the element is   :   ', t)

t.remove('abc')
print('The list after removing element ', t)

t.pop(2)
print('After removing element at index 2', t)

t.pop()
print('Pop element at the last index', t)

del t[1:3]
print('After edleting range of element ', t)


# Other list method

# clear() --> delet all the item

t.clear()  # delet all item of t list
print(t)

t1 = [1, 23, 'x', 'y', 'abhishek', 89.8]
# copy

t2 = t1.copy()  # copy t into list t2
print('This is t2 list', t2)
t2.append('y')
print(t2)


# count()
print('Number of occurances of object y is : ', t2.count('y'))


t1 = [1, 23, 'x', 'y', 'abhishek', 89.8]
t2 = [4, 65, 'u', 's', 'abc', 90.78, True, False]

# Extend()
print(t1)
print(t2)

t2.extend(t1)

print('t2 after extending it with the elements of t1 : ', t2)


print('The index of 1 in t2  :  ', t2.index(1))
print('The index of 1 in t2  :  ', t2.index('abc'))

t1 = [1, 23, 'x', 'y', 'abhishek', 89.8]
t2 = [4, 65, 'u', 's', 'abc', 90.78, True, False]

print(' t2 list before reverse operations  :  ', t2)

t2.reverse()

print('t2 list after reverse  : ', t2)


t4 = [1, 23, 45, 6, 23.4, 1.2, 34.1, 345]
print(t4)
t4.sort()
print('t4 after sorting order   :  ', t4)


# Iterating over a list
names = ['Abhishek', 'Ankit', 'Riddhi', 'Kumar', 'abhi']
print('List of names : ', names)

for i in names:
    print("Hello ", i)

name_val = input('Enter a name to search in the name list')
if name_val in names:
    print(f'The name {name_val} is present in the list.')
else:
    print(f'The name {name_val} is present in the list.')


'''                             Tuples                                     '''''


# Creating a Tuple
tup1 = (1, 2, 3, 5, 8)
print(tup1)

print('The type of tuples ', type(tup1))


list1 = [4, 7, 3, 8]
print('This is list 1 : ', list1)
t1 = tuple(list1)
print(t1)
print('The type of list1 ', type(list1))
print('The type of tuples ', type(t1))

# Accessing Element from a tuple

tup1 = (1, 2, 3, 5, 8)
print(tup1)

print(f'tup1 of 0 index :  {tup1[0]}')
print(f'tup1 of 3 index :  {tup1[3]}')
print("length of tup1 : ", len(tup1))
