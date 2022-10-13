str1 = 'Hello world'
str2 = "Welcome to String"

str3 = '''
    This is a multiline string. 
    This is third line of string..
    '''

print('The first string is: ', str1)
print('The Second string is: ', str2)
print('The Third string is: ', str3)


print(' The type of str1 is : ', type(str1))
print(' The type of str2 is : ', type(str2))
print(' The type of str3 is : ', type(str3))


# Operations On Strings

# Concatenate
str1 = "Good"
str2 = "Day!"
str3 = str1+str2
print("The result of concatenation is : ", str3)

print('Hii, ' + ' Abhishek ' + 'Kumar')


# Length

print('The length of str1 is : ', len(str1))
print('The length of str2 is : ', len(str2))

# Accessing string character
str3 = 'Abhishek is a good boy.'
print(str3)

print('The third character on str3 : ', str3[2])
print('The 5th character on str3 : ', str3[4])

# slicing operation : Accessing a group of characters
str3 = 'hello world'
print(str3[4])
print(str3[1:5])
print(str3[:5])
print(str3[2:])
print(str3[:])


# Repeat The string

str4 = '#'*10
print(str4)

print('hello ' * 5)
