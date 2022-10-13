 #Public data


from numpy import sometrue


class Person:
    fees=10000 # class variables inside the class
    def __init__(self,name,dob,city):
        self.name=name
        self.dob=dob
        self.city=city 
        
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
    
    def pay_fees(self,amount):
        return self.fees-amount


class DADS(Student):
    fees=5000 # fees for DADS alone changed now
    def __init__(self,name,rollno,dob,city,year):
        super().__init__(name,rollno,dob,city)
        self.year=year
class Teacher(Person):
    def __init__(self,name,dob,city,studentss=[]):
        super().__init__(name,dob,city)
        self.studentss=studentss

    def show_studentss(self):
        for i in self.studentss:
            print(i.name)


stu1=DADS('Abhishek',100,1990,'Bareilly',2018)
stu2=DADS('Anand',101,1999,'Lucknow',2009)
stu3=DADS('Rohit',102,2000,'Dehli',2010)
stu4=DADS('Mohit',104,2010,'Chennai',2020)
t1=Teacher('Ridhi',1999,'Paris',[stu1,stu2,stu3])


print(stu1.year,stu1.name)
print(stu2.year,stu2.name,stu2.dob,stu2.city,stu2.rollno)
print(stu3.year)
print(stu4.year)
print(t1.show_studentss())

print(stu1.fees)
print(Student.fees)
# I could access the data which was inside the class. This is public data. 


## privatising using-
 

class Person:
    # __fees=10000
    def __init__(self,name,dob,city):
        self.name=name
        self.dob=dob
        self.city=city 
        
class Student(Person):
    __fees=10000
    no_of_students=0
    def __init__(self,rollno,name,dob,city):
        super().__init__(name,dob,city)
        self.rollno=rollno
        Student.no_of_students+=1
    def address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} '
        return addres
    
    def pay_fees(self,amount):
        return self.fees-amount


class DADS(Student):
    fees=5000 # fees for DADS alone changed now
    def __init__(self,name,rollno,dob,city,year):
        super().__init__(name,rollno,dob,city)
        self.year=year
class Teacher(Person):
    def __init__(self,name,dob,city,studentss=[]):
        super().__init__(name,dob,city)
        self.studentss=studentss

    def show_studentss(self):
        for i in self.studentss:
            print(i.name)


stu1=DADS('Abhishek',100,1990,'Bareilly',2018)
stu2=DADS('Anand',101,1999,'Lucknow',2009)
stu3=DADS('Rohit',102,2000,'Dehli',2010)
stu4=DADS('Mohit',104,2010,'Chennai',2020)
t1=Teacher('Ridhi',1999,'Paris',[stu1,stu2,stu3])


print(stu1.year,stu1.name)
print(stu2.year,stu2.name,stu2.dob,stu2.city,stu2.rollno)
print(stu3.year)
print(stu4.year)
print(t1.show_studentss())

print(stu1.fees)

# print(stu1.__fees) #AttributeError: 'DADS' object has no attribute '__fees' 
print(stu1.address())







# Privtising methods using __ (adress and pay_fees)
# Now the methods are privatised




class Person:
    # __fees=10000
    def __init__(self,name,dob,city):
        self.name=name
        self.dob=dob
        self.city=city 
        
class Student(Person):
    __fees=10000
    no_of_students=0
    def __init__(self,rollno,name,dob,city):
        super().__init__(name,dob,city)
        self.rollno=rollno
        Student.no_of_students+=1
    def __address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} '
        return addres
    
    def __pay_fees(self,amount):
        return self.fees-amount


class DADS(Student):
    fees=5000 # fees for DADS alone changed now
    def __init__(self,name,rollno,dob,city,year):
        super().__init__(name,rollno,dob,city)
        self.year=year
class Teacher(Person):
    def __init__(self,name,dob,city,studentss=[]):
        super().__init__(name,dob,city)
        self.studentss=studentss

    def show_studentss(self):
        for i in self.studentss:
            print(i.name)


stu1=DADS('Abhishek',100,1990,'Bareilly',2018)
stu2=DADS('Anand',101,1999,'Lucknow',2009)
stu3=DADS('Rohit',102,2000,'Dehli',2010)
stu4=DADS('Mohit',104,2010,'Chennai',2020)
t1=Teacher('Ridhi',1999,'Paris',[stu1,stu2,stu3])


print(stu1.year,stu1.name)
print(stu2.year,stu2.name,stu2.dob,stu2.city,stu2.rollno)
print(stu3.year)
print(stu4.year)
print(t1.show_studentss())
print(stu1.fees)

# print(stu1.__address)
# print(stu1.__pay_fees)


print(t1.show_studentss())


# we can also privatise the individual attributes. 
# for instance if we want to change year of a student 1 in DADs to 2022 , we just give the object.attribute= 
print(stu2.year)
print('*'*50)

# changing the attributes
stu2.year=2022
print(stu2.year)
# Since it is not privates I could  change, now lwt us make it private. 



class Person:
    # __fees=10000
    def __init__(self,name,dob,city):
        self.name=name
        self.dob=dob
        self.city=city 
        
class Student(Person):
    fees=10000
    no_of_students=0
    def __init__(self,rollno,name,dob,city):
        super().__init__(name,dob,city)
        self.rollno=rollno
        Student.no_of_students+=1
    def __address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} '
        return addres
    
    def __pay_fees(self,amount):
        return self.fees-amount


class DADS(Student):
    fees=5000 # fees for DADS alone changed now
    def __init__(self,name,rollno,dob,city,year):
        super().__init__(name,rollno,dob,city)
        self.__year=year
class Teacher(Person):
    def __init__(self,name,dob,city,studentss=[]):
        super().__init__(name,dob,city)
        self.studentss=studentss

    def show_studentss(self):
        for i in self.studentss:
            print(i.name)


stu1=DADS('Abhishek',100,1990,'Bareilly',2018)
stu2=DADS('Anand',101,1999,'Lucknow',2009)
stu3=DADS('Rohit',102,2000,'Dehli',2010)
stu4=DADS('Mohit',104,2010,'Chennai',2020)
t1=Teacher('Ridhi',1999,'Paris',[stu1,stu2,stu3])


print(stu1.year,stu1.name)
print(stu2.year,stu2.name,stu2.dob,stu2.city,stu2.rollno)
print(stu3.year)
print(stu4.year)
print(t1.show_studentss())
print(stu1.fees)




''' However this is not an efficient method, because we can still access the data'''

# Delibrately made entire the content in the class has private


class Person:
    # __fees=10000
    def __init__(self,name,dob,city):
        self.name=name
        self.dob=dob
        self.city=city 
        
class Student(Person):
    __fees=10000
    no_of_students=0
    def __init__(self,rollno,name,dob,city):
        super().__init__(name,dob,city)
        self.rollno=rollno
        Student.no_of_students+=1
    def address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} '
        return addres
    
    def __pay_fees(self,amount):
        return self.fees-amount


class DADS(Student):
    fees=5000 # fees for DADS alone changed now
    def __init__(self,name,rollno,dob,city,year):
        super().__init__(name,rollno,dob,city)
        self.year=year
class Teacher(Person):
    def __init__(self,name,dob,city,studentss=[]):
        super().__init__(name,dob,city)
        self.studentss=studentss

    def __show_studentss(self):
        for i in self.studentss:
            print(i.name)

class Teacher2(Teacher):
    pass
stu1=DADS('Abhishek',100,1990,'Bareilly',2018)
stu2=DADS('Anand',101,1999,'Lucknow',2009)
stu3=DADS('Rohit',102,2000,'Dehli',2010)
stu4=DADS('Mohit',104,2010,'Chennai',2020)
t1=Teacher('Ridhi',1999,'Paris',[stu1,stu2,stu3])
t2=Teacher2('Ridhi',1900,'Aaris',[stu1,stu2,stu3])

# print(t1.show_studentss()) # AttributeError: 'Teacher' object has no attribute 'show_studentss'

print(t2._Teacher__show_studentss()) # When I accesss the data using the class name, I can change the value
print(t1._Teacher2__show_studentss()) # When I accesss the data using the class name, I can change the value
print(t1._Person__address())

print(t1.show_studentss()) # When I accesss the data using the class name, I can change the value
print(t2.show_studentss()) # When I accesss the data using the class name, I can change the value
print(t1._Person__address())









class Person:
    # __fees=10000
    def __init__(self,name,dob,city):
        self.name=name
        self.dob=dob
        self.city=city 
        
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
    
    def pay_fees(self,amount):
        return self.fees-amount


class DADS(Student):
    fees=5000 # fees for DADS alone changed now
    def __init__(self,name,rollno,dob,city,year):
        super().__init__(name,rollno,dob,city)
        self.year=year
    
    def __str__(self,name,dob,city,year):
        super().__init__(name,dob,city)
        self.year=year
class Teacher(Person):
    def __init__(self,name,dob,city,studentss=[]):
        super().__init__(name,dob,city)
        self.studentss=studentss
    def show_stu(self):
        for i in self.studentss:
            print(i.name)

stu1=DADS('Abhishek',100,1990,'Bareilly',2018)
stu2=DADS('Anand',101,1999,'Lucknow',2009)
stu3=DADS('Rohit',102,2000,'Dehli',2010)
stu4=DADS('Mohit',104,2010,'Chennai',2020)
t1=Teacher('Ridhi',1999,'Paris',[stu1,stu2,stu3])

# you van even change the values of any attribute you want. Suppose you want to change the name Anad to say Abhijeet. 

stu1.year=1990
print(stu1.year)# It is printing has 1990 but the original value has not changed. 

print(stu1) # The change is not in dtatabase





'''   Operator overloading  '''

c=10+20
print(c)

s=int.__add__(10,20)
print(s)

x='10'+'20'
print(x)

y=str.__add__('10','20')
print(y)


class SomTotals:
    def __init__(self,a):
         self.a=a
         print(self.a)

obj1=SomTotals(10)
obj2=SomTotals(20)
print(obj1.a+obj2.a)


# print(obj1+obj2)      #TypeError: unsupported operand type(s) for +: 'SomTotals' and 'SomTotals'      


class SomTotals:
    def __init__(self,a):
         self.a=a
         print(self.a)

    def __add__(self,other):
        return self.a+other.a
obj1=SomTotals(10)
obj2=SomTotals(20)
print(obj1.a+obj2.a)


class students():
    def __init__(self,m1,m2):
        self.ml=m1
        self.m2=m2

    def __add__(self, temp):
        m1=self.m1+temp.m1-self.m2**2
        m2=self.m2*temp.m2
        s3=students(m1,m2)
        return s3

s1=students(30,40)
s2=students(50,20)
s3=s1+s2
print(s3.m1,s3.m2)





'''Polymorphism through inheritence'''

class versionl:
    def button1(self):
        print('red')

class versionl2(versionl):
    def button2(self):
        print('yelow')

class version3(versionl2):
    def button3(self):
        print('green')

a=version3()
print(a.button1())
print(a.button2())
print(a.button3())






class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y 
    def adder(self):
        return self.x+self.y

    def sub(self):
        return self.x-self.y 

T=A(2,2)
print(T.adder())
print(T.sub())
