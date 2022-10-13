
# Accessing the properties of the sys module
import sys
print('  \nversion of the system is \n  :  ', sys.version)
print('  \nversion info of the system is \n  :  ', sys.version_info)
print(' \n Maxsize of the system is   \n:  ', sys.maxsize)
print('  \npath of the system is  \n  :  ', sys.path)
print(' \n  platform of the system is \n   :  ', sys.platform)







import myPack.mymath as mm
import myPack.mystr as ms 


# Create a package called mypack with the modules mymath anf mystr

str1=input("Enter astring")
str2=input("Enter astring")


print(f'Lenght of {str1} is ', ms.str_len(str1))
print(f'Lenght of {str2} is ', ms.str_len(str2))


print(f'The concatenate {str1 } with {str2} is ',ms.str_cat(str1,str2))
print(f'The comparision {str1 } with {str2} is ',ms.str_cmp(str1,str2))


x= int(input('Enter a first integer : '))
y= int(input('Enter a Second integer : '))

print(f'Sum of {x} and {y} is : ',mm.add(x,y) )
print(f'Multiplication of {x} and {y} is : ',mm.mul(x,y) )
print(f'Substractoin of {x} and {y} is : ',mm.sub(x,y) )
print(f'Division of {x} and {y} is : ',mm.div(x,y) )
print(f'Modulous of {x} and {y} is : ',mm.mod(x,y) )


# Accessing Module Property

print('The name of the module is  :   ', mm.__name__)
print('The Docstring of the module is  :   ', mm.__doc__)
print('The nname of the file of the module is  :   ', mm.__file__)

import myPack.myfile as mf 

filename =input('Enter  the filename  :  '   )
print('The size of the file is : ',mf.file_size(filename))



