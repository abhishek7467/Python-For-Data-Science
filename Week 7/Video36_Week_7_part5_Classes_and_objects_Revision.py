


# OOP Concepts


# What is class? 
''' Class is like a template or blueprint. We use it to build objects. Class it itself does'nt occupyany memory . when an object
ia initiaited memmory is allocated '''


# What does a class contain?
''' A contain methods and attributes. Methods are equvelent to functions, Attributes are like variables  '''
'''All the variables you create in python are object. 
When you wrie name='apple', you cerate an objrct(variable) belonging to the class string. 
All the functions can do on strings like rstrip, lstrip, split etc are the methods in the class string'''


from email.headerregistry import Address


name='apple'
print(type(name))
li=[]
print(type(li))

# let us create a list, tuple, dictionary
l=[] #l is an object belonging to class list
t=()# t is an object belonging to classtuple
d={} # d is an object belonging to class dictionary
print(type(l))
print(type(t))
print(type(d))


# Let us see what all the methods or function that you can see in a given class. We have created 4 variables  till now

# name which is string. I which is a list, t which is a tuple , d which is a list. 
print(dir(name))#to see the methods associated with class strings

namel =" This is Skill-Lync "
print(namel)
namel.strip( ' ')
na=namel.isdigit()
print(na)

print(dir(l))# to see methods associated with thw class list. 
#kindly note the pressence of apped wich allow you to edit the list
# strings don't have it

print(dir(t))# to see methods associated with thw class tuple
print(dir(d))# to see methods associated with thw class dictionary


## now let us add soemthing to the list.  
#we call the object and the method you want to perform


l=[]
print(l)
print(50*'*')
l.append(1)
l.append(2)
print(l)# you can see that class list has a method called apped
# Which allowed you to change the list.  


print(name)

print('*'*50)
# name.append(name) #AttributeError: 'str' object has no attribute 'append'
print(name)## you can see that class string has a method called apped
# Which allowed you to change the string.  
''' Note the error "str " object has no attribute "append" '''

#Let us create a class now

class Student:
    pass
stu1=Student()
stu2=Student()
stu3=Student()
stu4=Student()

print(stu1)
print(stu2)
print(stu3)
print(stu4)

# Let us complicate our Student class

class Student1:
    pass
stu1=Student()
stu2=Student()
stu3=Student()
stu4=Student()
q=Student1()
# creating  an instance variable
stu1.name='Abhi'
stu1.rollno=100
stu1.dob=1990
stu2.name='Ridhi'
stu2.rollno=181
stu2.dob=1999
stu3.name='kumar'
stu3.rollno=672
stu3.dob=2000
stu4.name='sandhya'
stu4.rollno=871
stu4.dob=2001
print('*'*100)
print(stu1.name,stu1.rollno,stu1.dob)
print(stu2.name,stu2.rollno,stu2.dob)
print(stu3.name,stu3.rollno,stu3.dob)
print(stu4.name,stu4.rollno,stu4.dob)



# This is extrememly painful if there are 100 Students. So use init Method. 
# This is also called  a constructor in kanguages like JAVA

class Students:
    def __init__(self,name,rollno,dob,city):
        self.name=name
        self.rollno =rollno
        self.dob=dob
        self.city=city 

stu1=Students('Abhishek',100,1990,'Bareilly')
stu2=Students('Anand',101,1999,'Lucknow')
stu3=Students('Rohit',102,2000,'Dehli')
stu4=Students('Mohit',104,2010,'Chennai')

print(stu1.name,stu1.rollno,stu1.dob,stu1.city)
print(stu2.name,stu2.rollno,stu2.dob,stu2.city)
print(stu3.name,stu3.rollno,stu3.dob,stu3.city)
print(stu4.name,stu4.rollno,stu4.dob,stu4.city)


# Creating Another Method

class Students1:
    def __init__(self,name,rollno,dob,city):
        self.name=name
        self.rollno =rollno
        self.dob=dob
        self.city=city 
    def address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} '
        return addres


stu1=Students1('Abhishek',100,1990,'Bareilly')
stu2=Students1('Anand',101,1999,'Lucknow')
stu3=Students1('Rohit',102,2000,'Dehli')
stu4=Students1('Mohit',104,2010,'Chennai')


print(stu1.name,stu1.rollno,stu1.dob,stu1.city)
print(stu2.name,stu2.rollno,stu2.dob,stu2.city)
print(stu3.name,stu3.rollno,stu3.dob,stu3.city)
print(stu4.name,stu4.rollno,stu4.dob,stu4.city)

print('*'*50)
print(stu1.address())
print(stu2.address())
print(stu3.address())
print(stu4.address())

## Let us create another method to find age
#to do this we import the date module and get the current year from that

 
from datetime import date 
class Students2:
    def __init__(self,name,rollno,dob,city):
        self.name=name
        self.rollno =rollno
        self.dob=dob
        self.city=city 
    def address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} '
        return addres
    
    def age(self):
        return date.today().year-self.dob


stu1=Students2('Abhishek',100,1990,'Bareilly')
stu2=Students2('Anand',101,1999,'Lucknow')
stu3=Students2('Rohit',102,2000,'Dehli')
stu4=Students2('Mohit',104,2010,'Chennai')

print("\t AGE")
print('*'*50)
print(stu1.age())
print(stu2.age())
print(stu3.age())
print(stu4.age())
print('*'*50)

print('*'*50)
print(stu1.address())
print(stu2.rollno)








# Instance the variables, creating object specific attributes like say fees for student1 ect..
 
from datetime import date 
class Students2:
    def __init__(self,name,rollno,dob,city):
        self.name=name
        self.rollno =rollno
        self.dob=dob
        self.city=city 
    def address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} '
        return addres
    
    def age(self):
        return date.today().year-self.dob

stu1=Students2('Abhishek',100,1990,'Bareilly')
stu2=Students2('Anand',101,1999,'Lucknow')
stu3=Students2('Rohit',102,2000,'Dehli')
stu4=Students2('Mohit',104,2010,'Chennai')



stu1.fees=1300000
stu2.fees=1300000
stu3.fees=1300000
print(stu1.fees)
print(stu2.fees)
print(stu3.fees)
# print(stu4.fees) #This will throw an error , because no attributes for stu4
#AttributeError: 'Students2' object has no attribute 'fees'


## To create commmon fees for all studenrs we create the class variable outside  the class 

 
from datetime import date 
class Students3:
    def __init__(self,name,rollno,dob,city):
        self.name=name
        self.rollno =rollno
        self.dob=dob
        self.city=city 
    def address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} '
        return addres
    
    def age(self):
        return date.today().year-self.dob

stu1=Students3('Abhishek',100,1990,'Bareilly')
stu2=Students3('Anand',101,1999,'Lucknow')
stu3=Students3('Rohit',102,2000,'Dehli')
stu4=Students3('Mohit',104,2010,'Chennai')

Students3.fees=150000 #  Comman Class Variables

print(stu1.fees)
print(stu2.fees)
print(stu3.fees)
print(stu4.fees)


#Now let us creae the class variable inside the class only

 
from datetime import date 

class Students3:
    fees=10000 # class variables inside the class
    def __init__(self,name,rollno,dob,city):
        self.name=name
        self.rollno =rollno
        self.dob=dob
        self.city=city 
    def address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} '
        return addres
    
    def age(self):
        return date.today().year-self.dob

stu1=Students3('Abhishek',100,1990,'Bareilly')
stu2=Students3('Anand',101,1999,'Lucknow')
stu3=Students3('Rohit',102,2000,'Dehli')
stu4=Students3('Mohit',104,2010,'Chennai')


print(stu1.fees)
print(stu2.fees)
print(stu3.fees)
print(stu4.fees)


# All the fees of students are 10000. now we can change one particular students fees alone by using the object directly. 
print('*'*50)
print('# All the fees of students are 10000. now we can change one particular students fees alone by using the object directly.')
stu1.fees=120000
print(stu1.fees)
print(stu2.fees)
print(stu3.fees)
print(stu4.fees)

