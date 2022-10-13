str1 = input("Enter Your Name : ")
print("The Entered String is : ", str1)

print("Hello, ", str1)

print("The Type of str1 is : ", type(str1))


# Accept two numbers from the user and find their sum

num1 = input("Enter 1st Number : ")
num2 = input("Enter 2st Number : ")
# So , Here Python accept input as the string

res = num1+num2
print("The sum of the two given numbers is : ", res)


num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2st Number : "))

res = num1+num2
print("The sum of the two given numbers is : ", res)


# Calculate area and circumference of a circle by accepting radius as input

radius = int(input("Enter Radius of the circle : "))

area = 3.14 * radius * radius
circum = 2 * 3.14 * radius
print("The area of the circle is : ", area)
print("The circum of the circle is : ", circum)


# Arithmetic operation on complex numbers

a = 3+8j
b = 10-7j
c = a+b
print("The Value of a : ", a)
print("The Value of b : ", b)
print("The sum of a and b : ", c)
