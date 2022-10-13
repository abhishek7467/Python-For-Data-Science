
import math
a = float(input('Enter the value of "a" Your First coefficient      :      '))
b = float(input('Enter the value of "b" Your Second coefficient      :      '))
c = float(input('Enter the value of "c" Your Thrid coefficient      :      '))

discriminant = b*b-4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f'Cofficients is {a} , {b} and {c}')
    print(f'Real Root1 {root1}')
    print(f'Real Root2 {root2}')


elif discriminant == 0:
    root1 = root2 = -b / (2 * a)

    print(f'Cofficients is {a} , {b} and {c}')
    print(f'Real Root1 {root1}')
    print(f'Real Root2 {root2}')

else:
    realPart = -b / (2 * a)
    ImagPart = math.sqrt(-discriminant)/(2 * a)
    print(f'Cofficients is {a} , {b} and {c}')
    print(f'Imaginary Root1 {realPart} + {ImagPart}i')
    print(f'Imaginary Root2 {realPart} + {ImagPart}i')
