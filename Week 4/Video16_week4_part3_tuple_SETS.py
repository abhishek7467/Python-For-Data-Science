tup2 = (1, 'Abhishek', True, -23.45)
for i in tup2:
    print(i)

if 'abhishek' in tup2:
    print('Abhishek is present.')


# Nested Tuple
tupl1 = (1, 2, 3, 4, 5, 7)
tupl2 = ('Abhishek', 'Kumar', 'Ridhi', 'Ramesh')
print('tupl1 is : ', tupl1)
print('tupl2 is : ', tupl2)

tuple3 = (42, tupl1, tupl2, 'Suresh', 'Mahesh')
print('The Nested Tuple 3 is : ', tuple3)

print('tuple 3[2] :  ', tuple3[2])
print('Access Element in Nested Tuples is : tuple 3[2][2] :  ', tuple3[2][2])


# Comparing Tuples

print((0, 1, 20000000) < (0, 4, 2))


'''                      SETS                          '''


s1 = {1, 'abc', 2.3334, 56}
s2 = set()
print('Set s1 is :  ', s1)
print('Set s2 is :  ', s2)


l1 = [1, 2, 3, 4]
s3 = set(l1)
print('S3 is created using the list is  :  ', s3)


basket = {'apple', 'orange', 'pear', 'orange', 'banana'}
print(basket)


for i in basket:
    print('The Fruit is  :   ', i)

if 'orange' in basket:
    print('Orange is present')


if 'graps' in basket:
    print('graps is present')

basket.add('apricot')
print(basket)

basket.update(['graps', 'water melon'])
print(basket)

print('Number of items present in basket :  ', len(basket))


s1 = {12, 24, 2, 56, 90, 34, 12}
print('The Maximum values in s1 set is :   ', max(s1))
print('The Minimum values in s1 set is :   ', min(s1))


basket = {'banana', 'water melon', 'apple',
          'pear', 'graps', 'orange', 'apricot'}
print(basket)
basket.remove('apple')
print('After removing the apple from the basket  : ', basket)


s3 = {'abc', (1, 33, 5, 2), 'abhishek'}
print('the s3 with the tuple   :    ', s3)


# Mathematical set operations

s1 = {'apple', 'orange', 'banana'}
s2 = {'grapefruit', 'Lime', 'banana'}

print('set1 is : ', s1)
print('set2 is : ', s2)

print('Union between s1 and s2 : ', s1 | s2)
print('Intersaction  between s1 and s2 : ', s1 & s2)
print('Difference between s1 and s2 : ', s1 - s2)
print('Symmetric Difference between s1 and s2 : ', s1 ^ s2)

print('\n\ \n \n ')

print('Union between s1 and s2 : ', s1.union(s2))
print('Intersaction  between s1 and s2 : ', s1.intersection(s2))
print('Difference between s1 and s2 : ', s1.difference(s2))
print('Symmetric Difference between s1 and s2 : ', s1.symmetric_difference(s2))


s3 = {1, 4, 2, 5, 3}
s4 = {1, 9, 2, 9, 7}
print('Union between s1 and s2 : ',  s3 | s4)
print('Intersaction  between s1 and s2 : ', s3 & s4)
print('Difference between s1 and s2 : ', s3 - s4)
print('Symmetric Difference between s1 and s2 : ', s3 ^ s4)
