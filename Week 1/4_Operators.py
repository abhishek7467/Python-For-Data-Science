x = 10
y = 20
z = 5
# PEMDAS rule: Paranthesis, Exponent, Multiplication, division, addtion and substraction
res = x+y*z
print(res)

res = x-y*z
print(res)

# Assignment Operators --> =,+=,-=,/=,//=,%=,*=

x = 10
y = x
print("Value of x = ", x, "Value of y= ", y)

x += 2  # x=x+2

print("Value of after Increment = ", x)

x -= 3  # x =x-3
print("The Value after Decrement = ", x)

x *= 2  # x=x*2
print("Value of x after multiplication increment :", x)

x /= 3  # x=x/3
print("The Value of x after division assignment", x)

x = 13

x %= 4  # x=x%4
print("The Value of x after Molulo Assignment :  ", x)


x = 12

x //= 5  # x=x//5
print("The Value Of x : ", x)

x = 6
x **= 2  # x=x**2

print(" The Value of x is : ", x)
