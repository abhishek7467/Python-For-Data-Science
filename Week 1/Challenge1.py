
# Question 1:

# displays your name
print(" My name is  Abhishek Kumar")


# complete mailing address formatted in the manner
email = '''Dear Abhishek,

Welcome to Skill Lync and thank you for choosing Post Graduate Program in Data Analytics and Data Science.

Your dedicated relationship manager is Arti, who will connect with you within 24-48 hrs. You may feel free to reach out to him/her at +914448130100 or raise a support ticket at support@skill-lync.com

Happy Learning!

Click here to book a one-on-one technical session with your technical engineer.

Regards,
Team Customer Experience
SKILL-LYNC 

'''

print(email)


# Question 2
user = input("Enter Your Name : ")
print(f"Hello, {user}")


# QUESTION 3

# Calculate area and circumference of a circle by accepting radius as input

radius = float(input("Enter Radius of the circle : "))
tp = type(radius)
print(f"Type of radius is : {tp}")
area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius
print(f"The area of the circle is : {area}")
print(f"The circumference of the circle is : {circumference}")


# QUESTION 4

lenght = float(input("Enter lenght of the Rectangle : "))
breadth = float(input("Enter Width of the Rectangle : "))
l_type = type(lenght)
w_type = type(breadth)
print(f"Type of radius is : {l_type}")
print(f"Type of radius is : {w_type}")
area = lenght * breadth
perimeter = 2 * lenght + 2 * breadth
print(f"The area of rectangle is : {area}")
print(f"The perimeter of rectangle is : {perimeter}")


# QUESTION 5


side = float(input("Enter side of the Square : "))
s_type = type(side)
print(f"Type of radius is : {s_type}")
Area = side * side
Perimeter = 4 * side
print(f"The area of square is : {Area}")
print(f"The perimeter of square is : {Perimeter}")


# QUESTION 6

# temperature=float(input("Enter temperature  : "))
Fahrenheit = float(input("Enter Fahrenheit  : "))
Cetigrate = 5/9 * (Fahrenheit-32)
print(f" Temperaure  into Centigrade , {Cetigrate},C")
Cetigrate_Input = float(input("Enter Fahrenheit  : "))
Fahrenheit_Out = Cetigrate_Input * (9/5)+32
print(f" Temperaure  into Centigrade , {Fahrenheit_Out},C")


# QUESTION 7

a = 5+10j
b = 4+3j
addition = a+b
print(f"The addition of {a} and {b} is : {addition} ")
subtraction = a-b
print(f"The Substraction of {a} and {b} is : {subtraction}")
multiplication = a*b
print(f"The Multiplication of {a} and {b} is : {multiplication}")


# QUESTION 8

name = input("Enter Your Name : ")
basic_Sal = float(input("Enter Your Basic Salary : "))

dearness_allowance = 0.4 * basic_Sal
house_rent_allowance = 0.2 * basic_Sal
gross_salary = basic_Sal + dearness_allowance + house_rent_allowance
print(f"The Name of Employee is {name}")
print(f"The basic salary is {basic_Sal}")
print(f" The Dearness Allowance is {dearness_allowance}")
print(f" The House Rent Allowance is {house_rent_allowance}")
print(f" The gross salary  is {gross_salary}")

# QUESTION 9
posistive_integers = int(input("Enter The Number (n) : "))
sum = (posistive_integers)*(posistive_integers + 1) / 2

print("The sum of the first", posistive_integers, "positive integers", sum)


# QUESTION 10

a = int(input("Enter The Number : "))
b = int(input("Enter The Number : "))

sum = a+b
print(f"The sum of {a} and {b} is {sum}")
diff = b-a
print(f"The difference when {b} is subtracted from {a} is {diff}")
mul = a*b
print(f"The product of {a} and {b} is {mul}")
div = a/b
print(f"The quotient when {a} is divided by {b} is {div}")
rem = a % b
print(f"The remainder when {a} is divided by {b} is {rem}")
power = a**b
print(f"The result of {a}**{b} is {power} ")
