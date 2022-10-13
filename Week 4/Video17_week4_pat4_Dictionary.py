'''                       Dictionary               '''

# create a dictionary called capitals

from sys import implementation

from numpy import histogram, number


capitals = {'Telangana': 'Hyderabad', 'Tamil Nadu': 'Chennai', 'Andhara Pradesh': 'Hydrabad',
            'Karnataka': 'Bengaluru', 'Maharashtra': 'Mumbai', 'Uttar': ''}
print(' Capitals : ', capitals)


# create dictionary from other collection types
dict1 = dict(uk='London', irland='Dubin', France='Paris')
print('Dict1    :  ', dict1)


# from List of tuples

dict2 = dict([('uk', 'London'), ('irland', 'Dubin'), ('France', 'Paris')])
print('Dict 2: ', dict2)

# from tuple of List
dict3 = dict((['uk', 'London'], ['irland', 'Dubin'], ['France', 'Paris']))
print("dict3   : ", dict3)

print('The capitals dictionary   :    ', capitals)
print('The capitals of Telangana   :    ', capitals['Telangana'])

# Add a new key :  value pair to the dictionary

capitals['Kerala'] = 'Thiruvananthapuram'
print('The modified capitals dictionary :   ', capitals)


# Modify an Existing element

capitals['Andhara Pradesh'] = 'Amaravati'
print('After Modified dictionary is : ', capitals)
print('After Modified values is : ', capitals['Andhara Pradesh'])


# in and not in operators

print('Assam ' in capitals)
print('Odisha' not in capitals)

print('The length of dictionary is  :         ', len(capitals))

# removing items from dictionary

print('\n \n \n ', capitals)
print('The last item inserted , which is deleted item from dictionary  :  ',
      capitals.popitem())


print('The capital of Maharastra is : ', capitals.pop('Maharashtra'))

del capitals['Karnataka']
print('\n \n \n', capitals)

capitals.clear()
print(' \n \n The clear all the item from the dictionary     :     ', capitals)


# Iterate over keys and values

capitals = {'Telangana': 'Hyderabad', 'Tamil Nadu': 'Chennai', 'Andhara Pradesh': 'Amaravati',
            'Karnataka': 'Bengaluru', 'Maharashtra': 'Mumbai', 'Uttar': '', 'Kerala': 'Thiruvananthapuram'}
print('Capitals :   ', capitals)

for state in capitals:
    print(state, end=',')
    print(capitals[state])


print('\n \n \n ')


for cap in capitals:
    print(cap)

print('The value are :', capitals.values())

print('\n \n The Keys are ', capitals.keys())
print('\n \n The Items are ', capitals.items())


# Nested Dictionary

seasons = {'Spring': ('Mar', 'Apr', 'May'),
           'Summer': ('June', 'July', 'August'),
           'Autumn': ('September', 'October', 'November'),
           'Winter': ('December', 'January', 'February')
           }

print(seasons)
print(seasons['Autumn'])
print('\n \n ')
print(seasons['Autumn'][2])


# implement a histogram to count number of letters in a sentence
sentence = input('Enter the sentence  :    ')

d = dict()

for c in sentence:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1

print(' The Histogram :   ', d)
