
# Question 1 
'''

Create a class called number which contains an integer. 
It should contain various methods to set the value of the integer, return the integer value, 
print the integer value, check whether the integer is negative.

'''

class NUMBER:
    def ValueIsInteger(self,num):
        if num>0:
            return print(f' The {num} is positive...')
        elif num<0:
            return print(f' The {num} is negative....')
        else:
            return print(f' The {num} is zero....')

n=float(input('Enter your number  :  '))
result=NUMBER()
result.ValueIsInteger(n)






# Question 2
'''
Create a class that can calculate the perimeter/ circumference and area of a regular shape. 
The class should also have a provision to accept the data relevant to the shape.

'''

from itertools import count
import math
class circumferenceAndArea:
    def  TriangleCircumference(self,s1,s2,s3):
        P=s1+s2+s3
        return print(f'The Perimeter of  Triangle of {s1} , {s2} and {s3} is   :   {P}  ')
    def TriangleArea(self,b,h):
        A= 0.5*b*h 
        return print(f'The Area of  Triangle of {b} and {h} is :   {A}')
    
    
    def  RectangleCircumference(self,l,w):
        P=2*(l+w)
        return print(f'The Perimeter of  Rectangle of {l} and {w}  is   :   {P}  ')
    def RectangleArea(self,l,w):
        A= l*w 
        return print(f'The Area of  Rectangle of {l} and {w} is :   {A}')
    
    
    def  SquareCircumference(self,s):
        P=4*s
        return print(f'The Perimeter of  Square of {s}  is   :   {P}  ')
    def SquareArea(self,s):
        A= s*s
        return print(f'The Area of  Square of {s}   is :   {A}')
    
    
    def  ParallelogramCircumference(self,l,w):
        P=2*(l+w)
        return print(f'The Perimeter of  Parallelogram of {l}  and {w} is   :   {P}  ')
    def ParallelogramArea(self,b,h):
        A= b*h 
        return print(f'The Area of  Parallelogram of {b} and {h} is :   {A}')
    
    
    def TrapezoidCircumference(self,s1,s2,s3,s4):
        P=s1+s2+s3+s4
        return print(f'The Perimeter of  Trapezoid of {s1}, {s2}, {s3}  and {s4} is   :   {P}  ')
    def TrapezoidArea(self,a,b,h):
        A= 0.5*h*(a+b)
        return print(f'The Area of  Trapezoid of {a} and {b} , {h} is :   {A}')
    
    
    def  CircleCircumference(self,r):
        P=2*(math.pi)*r
        return print(f'The Perimeter of  Circle of {r}    :   {P}  ')
    def CircleArea(self,r):
        A= (math.pi)*r*r
        return print(f'The Area of  Circle of {r} is :   {A}')

    
    
    def  RegularPolygonnSidesCircumference(self,n,s):
        P=n*s
        return print(f'The Perimeter of Regular Polygon n-sides of {n} and{s}    :   {P}  ')


PA=circumferenceAndArea()

s1=float(input('Enter side 1 of the triangle to find Perimeter      :        '))
s2=float(input('Enter side 2 of the triangle to find Perimeter     :        '))
s3=float(input('Enter side 3 of the triangle to find Perimeter     :        '))
PA.TriangleCircumference(s1,s2,s3)
b=float(input('Enter width  of the triangle to find Area     :        '))
h=float(input('Enter height  of the triangle to find Area     :        '))
PA.TriangleArea(b,h)

l=float(input('Enter length  of the Rectangle  to find Perimeter    :        '))
w=float(input('Enter width  of the Rectangle to find Perimeter     :        '))
PA.RectangleCircumference(l,w)
l=float(input('Enter width  of the Rectangle to find Area     :        '))
w=float(input('Enter height  of the Rectangle to find Area     :        '))
PA.RectangleArea(l,w)



s=float(input('Enter side  of the square  to find Perimeter    :        '))
PA.SquareCircumference(s)
s=float(input('Enter side  of the square  to find Area    :        '))
PA.SquareArea(s)


l=float(input('Enter length  of the Parallelogram  to find Perimeter    :        '))
w=float(input('Enter width  of the Parallelogram to find Perimeter     :        '))
PA.ParallelogramCircumference(l,w)
b=float(input('Enter width  of the Parallelogram to find Area     :        '))
h=float(input('Enter height  of the Parallelogram to find Area     :        '))
PA.ParallelogramArea(b,h)



s1=float(input('Enter side 1 of the Trapezoid to find Perimeter      :        '))
s2=float(input('Enter side 2 of the Trapezoid to find Perimeter     :        '))
s3=float(input('Enter side 3 of the Trapezoid to find Perimeter     :        '))
s4=float(input('Enter side 3 of the Trapezoid to find Perimeter     :        '))
PA.TrapezoidCircumference(s1,s2,s3,s4)
a=float(input('Enter base1  of the triangle to find Area     :        '))
b=float(input('Enter base2  of the triangle to find Area     :        '))
h=float(input('Enter height  of the triangle to find Area     :        '))
PA.TrapezoidArea(a,b,h)


r=float(input('Enter radius  of the square to find Perimeter     :        '))
PA.CircleCircumference(r)
r=float(input('Enter radius  of the square to find Area     :        '))
PA.CircleArea(r)

n=float(input('Enter side  of the Trapezoid to find Perimeter      :        '))
s=float(input('Enter value of n  of the Trapezoid to find Perimeter      :        '))
PA.RegularPolygonnSidesCircumference(n,s)



















# Question 3
'''
Create a class called student which contains the data members called rollno, 
sname and branch. The class should contain methods to initialize the data members 
and to set and display data members. Finally, the class should contain the __del__ method 
to release the memory at the time of object destruction. 
Test your class with at least two objects of the student class.

'''

class Students:
    def __init__(self,roll_no=None,Student_name='',Branch=''):
        self.Roll_no=roll_no 
        self.Sname=Student_name  
        self.Branch = Branch

    def set_data(self,roll_no,Student_name,Branch):
        self.Roll_no=roll_no 
        self.Sname=Student_name  
        self.Branch = Branch

    def display_data(self):

        print('\n Name  :  ', self.Roll_no  )
        print('Age  : ', self.Sname)
        print('Salary :  ',self.Branch)
    def __del__(self):
        print(f"\n Roll No- {self.Roll_no} \t Name-  {self.Sname} \tStudent's details are deleted........")

S1=Students()
S1.set_data(101,'Abhishek','Computer Science')
S2=Students()
S2.set_data(102,'Kumar','Information Technology')
S1.display_data()
S2.display_data()
S3=Students()
S3.set_data(103,'Ridhi','CS')
S3.display_data()



# Question 4 
'''

Modify the student class defined in Q.
No. 1 in so that it now includes a class variable to count 
the number of student objects created from this class and 
also add a class function in order to display the value of 
the class variable. 
The modified class should be named as student1 class.

'''

class student1:
    no_of_students=0
    def __init__(self,roll_no=None,Student_name='',Branch=''):
        self.Roll_no=roll_no 
        self.Sname=Student_name  
        self.Branch = Branch
        student1.no_of_students+=1
    def set_data(self,roll_no,Student_name,Branch):
        self.Roll_no=roll_no 
        self.Sname=Student_name  
        self.Branch = Branch
    def display_data(self):

        print('\n Name  :  ', self.Roll_no  )
        print('Age  : ', self.Sname)
        print('Salary :  ',self.Branch)

    def __del__(self):
        
        print(f"\n Roll No- {self.Roll_no} \t Name-  {self.Sname} \tStudent's details are deleted........")

S1=student1()
S1.set_data(101,'Abhishek','Computer Science')
S2=student1()
S2.set_data(102,'Kumar','Information Technology')

S1.display_data()
S2.display_data()

S3=student1()
print('\n \t Total Number of students is  : ',student1.no_of_students)

S3.set_data(103,'Ridhi','CS')
S3.display_data()













# Question 5 

'''

Apply the vars() and dir() global 
function on student and student1 classes

'''






class Students:
    def __init__(self,roll_no=None,Student_name='',Branch=''):
        self.Roll_no=roll_no 
        self.Sname=Student_name  
        self.Branch = Branch

    def set_data(self,roll_no,Student_name,Branch):
        self.Roll_no=roll_no 
        self.Sname=Student_name  
        self.Branch = Branch

    def display_data(self):

        print('\n Name  :  ', self.Roll_no  )
        print('Age  : ', self.Sname)
        print('Salary :  ',self.Branch)

S1=Students()
S1.set_data(101,'Abhishek','Computer Science')
S2=Students()
S2.set_data(102,'Kumar','Information Technology')
S1.display_data()
S2.display_data()
S3=Students()
S3.set_data(103,'Ridhi','CS')
S3.display_data()




class student1:
    no_of_students=0
    def __init__(self,roll_no=None,Student_name='',Branch=''):
        self.Roll_no=roll_no 
        self.Sname=Student_name  
        self.Branch = Branch
        student1.no_of_students+=1
    def set_data(self,roll_no,Student_name,Branch):
        self.Roll_no=roll_no 
        self.Sname=Student_name  
        self.Branch = Branch
    def display_data(self):

        print('\n Name  :  ', self.Roll_no  )
        print('Age  : ', self.Sname)
        print('Salary :  ',self.Branch)


S1=student1()
S1.set_data(101,'Abhishek','Computer Science')
S2=student1()
S2.set_data(102,'Kumar','Information Technology')

S1.display_data()
S2.display_data()

S3=student1()
print('\n \t Total Number of students is  : ',student1.no_of_students)

S3.set_data(103,'Ridhi','CS')
S3.display_data()


print('\n \n \n  \n \n \n ')

print('\n  Using vars on Students \n ')
print(vars(Students))
print('\n ')
print('\n  Using dir on students \n ')
print(dir(Students))
print('\n \n \n \n ')
print('\n  Using vars on student1 \n ')
print('\n ')
print(vars(student1))
print('\n  Using dir on student1 \n ')
print('\n ')
print(dir(student1))










# Question 6

'''

Create a class called Date. It should contain data members day, month and year. 
It should also contain functions to set and display date, 
as well as function to initialize date objects. 
Overload the == operator to check if two dates are equal


'''




class Date:
    def __init__(self,day=None,month='',year=None):
        self.Day=day 
        self.Month=month  
        self.Year = year
    def set_date(self,day,month,year):
        self.Day=day 
        self.Month=month  
        self.Year = year
    def display_date(self):
        print('\n Day  :  ', self.Day  )
        print('Month  : ', self.Month)
        print('Year :  ',self.Year)
    def __eq__(self,other):
       if self.Day==other.Day and self.Month==other.Month and self.Year == other.Year:
            print(' and  D4 are equalls .')


    

D1=Date()
D2=Date()
D3=Date()
D4=Date()
a=D1.set_date(2,'Feb',2002)
b=D4.set_date(4,'March',2000)
c=D3.set_date(15,'Dec',2001)
d=D4.set_date(2,'Feb',2002)
D1.display_date()
D2.display_date()
D3.display_date()
D4.display_date()
eq=Date()
if a==d:
    print('a and d are equals')




# Question 7 
'''

Create a class called weather that has a list containing weather parameters. 
Overload the in operator that checks whether an item is present in the list or not.


'''

class Weather:
    def __init__(self,list1=0,Item=0):
        self.list2=list1
        self.item=Item 
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.list2==self.item:
        
            raise StopIteration 
        else:
            return self.item


list1=['Abhi','Kumar','Sandhu','Ridhi','Jaiswal','Kumari']
word=('Abhi')


for word in (list1):
    print('The Item is present in list.... ')
    break


# Question 8
'''

Create a class called complex containing real and imaginary 
parts and then use it to check whether two objects are of the same type, 
whether their attributes are same and whether they are pointing to the same object

'''

class Complex(object):
    def __init__(self,realPart=1,ImgPart=0):
        self.realPart=realPart 
        self.ImgPart=ImgPart  

    def real_img_part(self,realPart,ImgPart):
        self.realPart=realPart 
        self.ImgPart=ImgPart 
    def display_num(self):
        print('\n The Number is   :  ', self.realPart + self.ImgPart )
        return self.realPart+self.ImgPart
D1=Complex()
a=D1.real_img_part(2,4j)
b=D1.real_img_part(67,42j)

D1.display_num()
a=2+4j
if (type(2+4j))==(type(67+42j)):
    print('Type are same of both value.')






# Question 9
'''

Create a class called department with the attributes deptname and deptid. 
Modify the student class defined in Q.No. 3 
such that it contains an object of department class. 
Name the new modified student class as student2.

'''


class department:
    def __init__(self,deptname,deptid,roll_no,Student_name,Branch):
        self.deptname=deptname 
        self.deptid=deptid         
        self.Roll_no=roll_no 
        self.Sname=Student_name  
        self.Branch = Branch
 

    def display_data(self):
        
        print('\n Department Name  :  ', self.deptname  )
        print('Department ID  : ', self.deptid)
        print('\n Name  :  ', self.Roll_no  )
        print('Age  : ', self.Sname)
        print('Salary :  ',self.Branch)
    
    def __del__(self):
        print(f"\n Roll No- {self.deptname} \t Name-  {self.deptid}  details are deleted........")


class Students(department):
        def __init__(self,deptname,deptid,Roll_no,Sname,Branch):
            super().__init__(deptname,deptid,Roll_no,Sname,Branch)

stu1=Students('Engineering',101,1,'Abhishek','CS')
stu2=Students('Engineering',102,2,'Aniket','IT')
stu3=Students('Engineering',102,3,'Ram','ME')
stu4=Students('Engineering',103,4,'Kumar','CE')

print(stu1.deptname,stu1.deptid,stu1.Roll_no,stu1.Sname,stu1.Branch)
print(stu1.deptname,stu2.deptid,stu2.Roll_no,stu2.Sname,stu2.Branch)
print(stu1.deptname,stu3.deptid,stu3.Roll_no,stu3.Sname,stu3.Branch)
print(stu1.deptname,stu4.deptid,stu4.Roll_no,stu4.Sname,stu4.Branch)



# Question 10
'''

Create a class called Person. From this class, inherit another class called student. 
Assume suitable data members and member functions for these two classes. 
In both the classes, define the __str__ function and demonstrate method overriding. 


'''


class Person:
    def __init__(self,name,dob,city):
        self.name=name
        self.dob=dob
        self.city=city 
        
    def __str__(self,name,dob,year):
        super().__init__(name,dob,year)
        self.year=year

class Student(Person):
    fees=10000
    no_of_students=0
    def __init__(self,rollno,name,dob,city):
        super().__init__(name,dob,city)
        self.rollno=rollno
        Student.no_of_students+=1
    def address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} '
        return addres
    def __str__(self,name,dob,city,year):
        super().__init__(name,dob,city)
        self.year=year
    def pay_fees(self,amount):
        return self.fees-amount


stu1=Student('Abhishek',100,1990,'Bareilly')
stu2=Student('Anand',101,1999,'Lucknow')
stu3=Student('Rohit',102,2000,'Dehli')
stu4=Student('Mohit',104,2010,'Chennai')



print(stu1.name,stu1.dob,stu1.city,stu1.rollno)
print(stu2.name,stu2.dob,stu2.city,stu2.rollno)
print(stu3.name,stu3.dob,stu3.city,stu3.rollno)
print(stu4.name,stu4.dob,stu4.city,stu4.rollno)

print(stu1.fees)
print(stu2.fees)
print(stu3.fees)
print(stu4.fees)
print(Student.fees)























