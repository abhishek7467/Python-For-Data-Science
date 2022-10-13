'''                        List  REVISION             '''


# creating Lists
from cmath import pi
import numbers
from unicodedata import decimal


list1 = []
a = (1, 2, 3)
b = list(a)
print(list1)
print(type(list1))
print(type(a))
print((a))
print(type(b))
print((b))

# list can be a collection of integers , strings, have nested lists, have dictionaries , tuples etc...
list2 = [19892, 877]
list3 = [3, 23, 45, 12, 43, 54, 12, 54, 32.2]
list4 = ['one', 'two', 'three']
list5 = ['Python', 25, [50, 100], [150, 90], 'apple']
list6 = [100, 'Python', 17.67, 'java']
list7 = ['Python', 25, [90, 789], [160, 70], {'A', "R"}, {'Abhishek', 'Kumar'}]

print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
print(list7)

mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(mylist)
print(mylist[0:3])
print(mylist[2:5])
print(mylist[:3])
print(mylist[-8])
print(mylist[-1])
print(mylist[:2])
print(mylist[:7])
print(mylist[1:4])
print(mylist[-6:-4])

mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
mylist.append('nine')  # add an item to the end of the list
print(mylist)
mylist.insert(1, 'ONE')  # Add item at index location 1
print(mylist)

mylist.remove('ONE')  # Remove item "ONE"
print(mylist)
mylist.pop()  # Remove  item from the last position of the list
print(mylist)
mylist.pop(6)  # Remove  item at index location 7
print(mylist)
mylist.pop(5)  # Remove  item at index location 6
print(mylist)

Nlist = ['one', 'two', 'three', 'Four', 'Five', 'Six']
print(Nlist)

del Nlist[5]  # Remove item at index location 6
print(Nlist)

mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
mylist[0] = 1
mylist[7] = 7
mylist[1] = 1
mylist[2] = 2

print(mylist)

mylist.clear()  # Empty Lit / Delete all items in the list
print(mylist)

tup = ('one', 'two', 'Three', 'Four', 'Five', 'SIx', 'Seven', 'Eight')
list1 = list(tup)
print(list1)
print(type(list1))
mylist = list1  # Create a new reference "list1"
mylist2 = list1.copy()
print(mylist)
print(mylist2)
print(list1)


# tupList=['one', 'two', 'Three', 'Four', 'Five', 'SIx', 'Seven', 'Eight']
list1[0] = 1
print(list1)
# note mylist1 also changed because we asked mylist1 to equated from list1 and we changed list1
print(mylist)
print(mylist2)
mylist[2] = 3
print(mylist)
print(mylist2)  # copy dosn't change
print(list1)  # note list1 also changed because we asked mylist is a equated from list and we changed mylist


list1 = ['one', 'two', 'three', 'four']
list2 = ['five', 'six', 'seven', 'eight']
list3 = list1+list2  # join two lists by '+' operator
print(list3)
list1.extend(list2)
print('This is extended list ; ', list1)


list1 = ['one', 'two', 'three', 'four']
print('List 1 is  : ', list1)
list1.reverse()  # reverse the list
print(list1)

list1 = list1[::-1]  # Another to reverse the list
print(list1)

mylist3 = [9, 5, 3, 12, 54, 67, 12, 9, 0, 56, 34.2]
print(mylist3)
mylist3.sort()  # Sort list in ascending order
print('Sort list in ascending order   : ', mylist3)
mylist3.sort(reverse=True)  # Sort list in descending order
print('Sort list in descending order    :', mylist3)

mylist4 = [88, 65, 34, 1290, 233, 334, 12, 34, 56, 678, 0, 97, 43]
print(mylist4)
# Return a new sorted list and doesn't change original list
print(sorted(mylist4))
print(mylist4)


list1 = ['one', 'two', 'three', 'four']
for i in list1:  # looping through lists
    print(i)


for i in enumerate(list1):  # element with index number
    print(i)


mylist7 = [i for i in range(40) if i % 2 == 1]
print(mylist7)

# is Exactly same as
mylist_7_b = []
for i in range(40):
    if i % 2 == 0:
        mylist_7_b.append(i)
print(mylist_7_b)


# calculate square of all numbers between 0-59 using list comprehension
mylist8 = [num**2 for num in range(60)]
print(mylist8)

# is exaectly same as
mylist8_b = []
for i in range(60):
    num = i**2
    mylist8_b.append(num)

print(mylist8_b)


list1 = [2, 3, 4, 5, 6, 7, 8, 9]
list1 = [i*10 for i in list1]  # multiplying whole list with 10
print(list1)


# is exaectly same as
list2 = [2, 3, 4, 5, 6, 7, 8, 9]
list3 = []
for i in list2:
    num = i*10
    list3.append(num)
print('This list3 is  :  ', list3)


# List all numbers divisible by 3,9 & 12 using nested "if" with List Comprehension
# This is combind 3 and conditions
mylist9 = [i for i in range(200) if i % 3 == 0 if i % 9 == 0 if i % 12 == 0]
print(mylist9)

# is exaectly same as
mylist9_b = []
for i in range(200):
    if i % 3 == 0 and i % 9 == 0 and i % 12 == 0:
        mylist9_b.append(i)
print(mylist9_b)

l1 = [print('{} is even Numbers'.format(i)) if i % 2 == 0 else print(
    '\t \t {} is odd numbers'.format(i)) for i in range(13)]


# is exaectly same as
for i in range(13):
    if i % 2 == 0:
        print(f"The {i} is even ")
    else:
        print(f" \t \tThe {i} is odd")

# Extract number from a string above

mystr = " One 1 two 2 three 3 four 4 six 6789"
numbers = [i for i in mystr if i.isdigit()]
print(numbers)

# is exaectly same as  above
# my_str='123 23 ia is one  1 is 2 ki 34 h 89'
my_str = input('Enter  alphabets with numbers (this is 23454 is 324) : ')
numbers2 = []
for i in my_str:
    if i.isdigit():
        print(i)
        numbers2.append(i)

print(numbers2)


mystr = " One 1 two 2 three 3 four 4 six 6789"
char = [i for i in mystr if i.isalpha()]
print(char)

# is exaectly same as   above
# my_str='123 23 ia is one  1 is 2 ki 34 h 89'
my_str = input('Enter  alphabets with numbers (this is 23454 is 324) : ')
char2 = []
for i in my_str:
    if i.isalpha():
        print(i)
        char2.append(i)

print(char2)


mystr = " One 1 two 2 three 3 four 4 six 6789"
decimal = [i for i in mystr if i.isdecimal()]
print(decimal)

# is exaectly same as above
# my_str='123 23 ia is one  1 is 2 ki 34 h 89'
my_str = input('Enter  alphabets with numbers (this is 23454 is 324) : ')
decimal2 = []
for i in my_str:
    if i.isdecimal():
        print(i)
        decimal2.append(i)

print(decimal2)


list10 = ['XS', 'S', 'M', 'N', 'L', 'XL']
[print('EXTRA SMALL') if i == 'XS' else(print('Small') if i == 'S'else(print('Medium') if i == 'M' else(
    print('Normal') if i == 'N' else(print('Large') if i == 'L' else(print('Extra Large')))))) for i in list10]


# is exaectly same as   above

list10 = ['XS', 'S', 'M', 'N', 'L', 'XL']
list12 = []
for i in list10:
    print(list12)
    if i == 'XS':
        list12.append("Exter Small")
    elif i == 'S':
        list12.append('Small')
    elif i == 'M':
        list12.append('Medium')
    elif i == 'N':
        list12.append('Normal')
    elif i == 'L':
        list12.append('Large')
    else:
        list12.append('Extera Large')
print(list12)
