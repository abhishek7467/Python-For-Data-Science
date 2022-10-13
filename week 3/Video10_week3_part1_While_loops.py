# Iterative Statements

'''        While Loop        '''


# print a message five times

count = 0

while count < 5:
    print('Welcome to iterative statements')
    count += 1
print('This is Outside from the while loops')


# print values from 0 to n

n = int(input('ENter the value of n : '))
count = 0
while count < n:
    print('Count : ', count)
    count += 1


# print values from 1 to n

n = int(input('Enter the value of n :  '))
count = 1
while count <= n:
    print('Count : ', count)
    count += 1


# Print numbers from 0 to 10 with an increment of 2

count = 0
while count <= 10:
    print(count)
    count += 2


count = 10
while count > 0:
    print(count)
    count -= 1

 # print value from m to n
m = int(input(' The value of m : '))
n = int(input(' The value of n : '))
while m <= n:
    print(m)
    m += 1


# Calculate average of n numbers
n = int(input(' The value of n : '))
Sum = 0
count = 0
while count < n:
    Sum = Sum+n

print('The sum of n numbers : ', sum)


# while True: # This is infinite loop
#     print('Abhishek Kumar is a good boy.')
count = 0
ssum = 0
while count < 9:
    n = int(input("Enter the number :  "))
    ssum = ssum+n
    print("Sum at each state : ", ssum)
    count += 1
print("The total sum : ", ssum)


# Break Statement
# Example of break using while loop

i = 0
print('Before while............... ')
while i < 9:
    print('i =  ', i)
    i += 1
    if i == 6:
        break
print('This is Outside from While loop  ')


# Example of continue with while loop

i = 0
while i < 10:
    i += 1
    if i == 7:
        continue
    print('i =  ', i)
print('This is Outside from  the loop...')
