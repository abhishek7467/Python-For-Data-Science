 # Create  a module called mymath in a file called mymath.py 

import mymath
x= int(input('Enter a first integer : '))
y= int(input('Enter a Second integer : '))

print(f'Sum of {x} and {y} is : ',mymath.add(x,y) )
print(f'Multiplication of {x} and {y} is : ',mymath.mul(x,y) )
print(f'Substractoin of {x} and {y} is : ',mymath.sub(x,y) )
print(f'Division of {x} and {y} is : ',mymath.div(x,y) )
print(f'Modulous of {x} and {y} is : ',mymath.mod(x,y) )


# Accessing Module Property

print('The name of the module is  :   ', mymath.__name__)
print('The Docstring of the module is  :   ', mymath.__doc__)
print('The nname of the file of the module is  :   ', mymath.__file__)
