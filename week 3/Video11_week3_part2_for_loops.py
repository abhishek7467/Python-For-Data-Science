
'''        For loop        '''


# print a statment 5 times

print(range(5))


for i in range(0, 5):
    print('Welcome Abhishek Kumar in For Loop : ', i)


# print numbers from 0 to 9
for i in range(0, 10):
    print('i =  ', i)
print('This is Outside from for loop')


# Print numbers from 0 to 10 with an increment of 2
for i in range(0, 11, 2):
    print('Even Number is : ', i)

# --> Flow of Executon of the above loop
#  1. Initialization - only once - i = 0
#  2. Condition test -i<11
#  3. Execute the body
#  4. Increment i=i+2
#  5. Execute steps 2 to 4


for i in range(0, 31, 3):
    print('   ', i)


# print the numbers 9 to 1

for i in range(9, 0, -1):
    print('In Reverse order  ', i)


# Find the average of n numbers using for loop
n = int(input('Enter the value of n :  '))
Sum = 0
for i in range(0, n):
    num = int(input('Enter the value  :  '))
    Sum = num+Sum
avg = Sum/n
print('The Average is : ', avg)


# Break Statement
# Example of break using For loop

for i in range(0, 11):
    print(i)
    if i == 6:
        break
print('This is Outside from for loop......')
