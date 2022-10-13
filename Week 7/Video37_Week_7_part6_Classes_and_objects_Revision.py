from datetime import date

from numpy import roll 
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

print(stu1.__dict__)# here we have used an instance variable as fees=12000 is created
print(stu2.__dict__)# here no specific attributes for students is created
print(stu2.fees)# just prints the fees attributes of the entire class


# Let us create a method when different amount is paid by different student, here we need to create
# instance variables because student pay different amount. 


class Students4:
    fees=10000 # class variables inside the class
    def __init__(self,name,rollno,dob,city):
        self.name=name
        self.rollno =rollno
        self.dob=dob
        self.city=city 
    def address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} '
        return addres
    
    def pay_fees(self,amount):
        return self.fees-amount

stu1=Students4('Abhishek',100,1990,'Bareilly')
stu2=Students4('Anand',101,1999,'Lucknow')
stu3=Students4('Rohit',102,2000,'Dehli')
stu4=Students4('Mohit',104,2010,'Chennai')

print(stu1.pay_fees(5000))
print(stu2.pay_fees(5000))
print(stu3.pay_fees(3000))
print(stu4.pay_fees(2000))

print('*'*50)
stu1.fees=30000
print(stu1.pay_fees(5000))
print(stu2.pay_fees(5000))
print(stu3.pay_fees(3000))
print(stu4.pay_fees(2000))




# No of students in the class, Here we want to find all the students in the class. so we have to create
# a class variable and not instance or object variable 
 
class Students5:
    fees=10000 # class variables inside the class
    no_of_students=0
    def __init__(self,name,rollno,dob,city):
        self.name=name
        self.rollno =rollno
        self.dob=dob
        self.city=city 
        Students5.no_of_students=Students5.no_of_students+1
    def address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} '
        return addres
    
    def pay_fees(self,amount):
        return self.fees-amount

stu1=Students5('Abhishek',100,1990,'Bareilly')
stu2=Students5('Anand',101,1999,'Lucknow')
stu3=Students5('Rohit',102,2000,'Dehli')
stu4=Students5('Mohit',104,2010,'Chennai')

print('Total Number of students is  : ',Students5.no_of_students)
print('*'*50)
print(stu1.pay_fees(5000))
print(stu2.pay_fees(5000))
print(stu3.pay_fees(3000))
print(stu4.pay_fees(2000))




''' Let us learn about the inheritence of OOOPs'''
#Inheritence meance getting or importing atrributes from another class

class Students6:
    fees=10000 # class variables inside the class
    no_of_students=0
    def __init__(self,name,rollno,dob,city):
        self.name=name
        self.rollno =rollno
        self.dob=dob
        self.city=city 
        Students6.no_of_students+=1
    def address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} '
        return addres
    
    def pay_fees(self,amount):
        return self.fees-amount
class DADS(Students6):
    pass # all the function from students inherited byDADS

stu1=DADS('Abhishek',100,1990,'Bareilly')
stu2=DADS('Anand',101,1999,'Lucknow')
stu3=DADS('Rohit',102,2000,'Dehli')
stu4=DADS('Mohit',104,2010,'Chennai')

print(stu1.name,stu1.rollno,stu1.dob,stu1.city)
print(stu2.name,stu2.rollno,stu2.dob,stu2.city)
print(stu3.name,stu3.rollno,stu3.dob,stu3.city)
print(stu4.name,stu4.rollno,stu4.dob,stu4.city)

print('Total Number of students is  : ',Students6.no_of_students)
print('*'*50)
print(stu1.pay_fees(5000))
print(stu2.pay_fees(5000))
print(stu3.pay_fees(3000))
print(stu4.pay_fees(2000))


print(dir(DADS))# inherit everything from students6

print(DADS.__mro__)#It has searched in DADS and want to STUDENTS
# It is called resolution order. 


# Method ovverriding Let us modify the fees of DADS student alone


class Student7:
    fees=10000 # class variables inside the class
    no_of_students=0
    def __init__(self,name,rollno,dob,city):
        self.name=name
        self.rollno =rollno
        self.dob=dob
        self.city=city 
        Student7.no_of_students+=1
    def address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} '
        return addres
    
    def pay_fees(self,amount):
        return self.fees-amount
class DADS(Student7):
    fees=175000 # fees for DADS alone changed now
stu1=Student7('Abhishek',100,1990,'Bareilly')
stu2=Student7('Anand',101,1999,'Lucknow')
stu3=DADS('Rohit',102,2000,'Dehli')
stu4=DADS('Mohit',104,2010,'Chennai')

print(stu1.name,stu1.rollno,stu1.dob,stu1.city)
print(stu2.name,stu2.rollno,stu2.dob,stu2.city)
print(stu3.name,stu3.rollno,stu3.dob,stu3.city)
print(stu4.name,stu4.rollno,stu4.dob,stu4.city)

print('Total Number of students is  : ',Student7.no_of_students)
print('*'*50)
print(stu1.pay_fees(5000))
print(stu2.pay_fees(5000))
print(stu3.pay_fees(3000))
print(stu4.pay_fees(2000))

# We overriding the variable now we can overriding the method also. ie, we can change the function also. 



class Student8:
    fees=10000 # class variables inside the class
    no_of_students=0
    def __init__(self,name,rollno,dob,city):
        self.name=name
        self.rollno =rollno
        self.dob=dob
        self.city=city 
        Student8.no_of_students+=1
    def address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} '
        return addres
    
    def pay_fees(self,amount):
        return self.fees-amount
class DADS(Student8):
    fees=175000 # fees for DADS alone changed now
    def __init__(self,name,rollno,dob,city,year):
        self.name=name
        self.rollno =rollno
        self.dob=dob
        self.city=city 
        self.year=year 
        Student8.no_of_students+=1
    def address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} ,\n Year : {self.year}'
        return addres




stu1=DADS('Abhishek',100,1990,'Bareilly',2018)
stu2=DADS('Anand',101,1999,'Lucknow',2009)
stu3=DADS('Rohit',102,2000,'Dehli',2010)
stu4=DADS('Mohit',104,2010,'Chennai',2020)
print(stu1.year)
print(stu2.year)
print(stu3.year)
print(stu4.year)

print(stu1.name,stu1.rollno,stu1.dob,stu1.city,stu1.year)
print(stu2.name,stu2.rollno,stu2.dob,stu2.city,stu1.year)
print(stu3.name,stu3.rollno,stu3.dob,stu3.city,stu1.year)
print(stu4.name,stu4.rollno,stu4.dob,stu4.city,stu1.year)


print('Total Number of students is  : ',Student8.no_of_students)
print('*'*50)
print(stu1.pay_fees(5000))
print(stu2.pay_fees(5000))
print(stu3.pay_fees(3000))
print(stu4.pay_fees(2000))



#Literally we have used the same code again . extremely bad practice


class Student9:
    fees=10000 # class variables inside the class
    no_of_students=0
    def __init__(self,name,rollno,dob,city):
        self.name=name
        self.rollno =rollno
        self.dob=dob
        self.city=city 
        Student9.no_of_students+=1
    def address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} '
        return addres
    
    def pay_fees(self,amount):
        return self.fees-amount
class DADS(Student9):
    fees=175000 # fees for DADS alone changed now
    def __init__(self,name,rollno,dob,city,year):
        super().__init__(name,rollno,dob,city)
        self.year=year




stu1=DADS('Abhishek',100,1990,'Bareilly',2018)
stu2=DADS('Anand',101,1999,'Lucknow',2009)
stu3=DADS('Rohit',102,2000,'Dehli',2010)
stu4=DADS('Mohit',104,2010,'Chennai',2020)
print(stu1.year,stu1.name)
print(stu2.year)
print(stu3.year)
print(stu4.year)

print(stu1.name,stu1.rollno,stu1.dob,stu1.city,stu1.year)
print(stu2.name,stu2.rollno,stu2.dob,stu2.city,stu1.year)
print(stu3.name,stu3.rollno,stu3.dob,stu3.city,stu1.year)
print(stu4.name,stu4.rollno,stu4.dob,stu4.city,stu1.year)


print('Total Number of students is  : ',Student9.no_of_students)
print('*'*50)
print(stu1.pay_fees(5000))
print(stu2.pay_fees(5000))
print(stu3.pay_fees(3000))
print(stu4.pay_fees(2000))

## We saw a single inheritence, Let us create another create a class, now we have multi level inheritence. 


class Person:
    # fees=10000 # class variables inside the class
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




stu1=DADS('Abhishek',100,1990,'Bareilly',2018)
stu2=DADS('Anand',101,1999,'Lucknow',2009)
stu3=DADS('Rohit',102,2000,'Dehli',2010)
stu4=DADS('Mohit',104,2010,'Chennai',2020)
print(stu1.year,stu1.name,stu1.rollno)
print(stu2.year)
print(stu3.year)
print(stu4.year)




## Let us create hierarchial inheritence 


class Person1:
    # fees=10000 # class variables inside the class
    def __init__(self,name,dob,city):
        self.name=name
        self.dob=dob
        self.city=city 
        
class Student11(Person1):
    fees=10000
    no_of_students=0
    def __init__(self,rollno,name,dob,city):
        super().__init__(name,dob,city)
        self.rollno=rollno
        Student11.no_of_students+=1
    def address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} '
        return addres
    
    def pay_fees(self,amount):
        return self.fees-amount


class DADS(Student11):
    fees=5000 # fees for DADS alone changed now
    def __init__(self,name,rollno,dob,city,year):
        super().__init__(name,rollno,dob,city)
        self.year=year
class Teacher(Person1):
    pass



stu1=DADS('Abhishek',100,1990,'Bareilly',2018)
stu2=DADS('Anand',101,1999,'Lucknow',2009)
stu3=DADS('Rohit',102,2000,'Dehli',2010)
stu4=DADS('Mohit',104,2010,'Chennai',2020)
t1=Teacher('Riddhi',105,'India')
print(stu1.year,stu1.name,stu1.rollno)
print(stu2.year)
print(stu3.year)
print(stu4.year)
print(t1.name,t1.city,t1.dob)


'''
Person1

Students        Teacher

DADS

'''

## Let us create hierarchial inheritence 


class Person1:
    # fees=10000 # class variables inside the class
    def __init__(self,name,dob,city):
        self.name=name
        self.dob=dob
        self.city=city 
        
class Student12(Person1):
    fees=10000
    no_of_students=0
    def __init__(self,rollno,name,dob,city):
        super().__init__(name,dob,city)
        self.rollno=rollno
        Student12.no_of_students+=1
    def address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} '
        return addres
    
    def pay_fees(self,amount):
        return self.fees-amount


class DADS(Student12):
    fees=5000 # fees for DADS alone changed now
    def __init__(self,name,rollno,dob,city,year):
        super().__init__(name,rollno,dob,city)
        self.year=year
class Teacher1(Person1):
    def __init__(self, name, dob,rollno, city,stu=[]):
        super().__init__(name, rollno,dob,city)
        self.Student12=stu
    def show_students(self):
        for i in self.Student12:
            print(i.name)


stu1=DADS('Abhishek',100,1990,'Bareilly',2018)
stu2=DADS('Anand',101,1999,'Lucknow',2009)
stu3=DADS('Rohit',102,2000,'Dehli',2010)
stu4=DADS('Mohit',104,2010,'Chennai',2020)
t1=Teacher1('Riddhi',105,'India',[stu1,stu2])
print(stu1.year,stu1.name,stu1.rollno)
print(stu2.year)
print(stu3.year)
print(stu4.year)
print(t1.name,t1.city,t1.dob)


''' Encapsulation and abstraction '''


''' Data hiding + abstraction = Encapsulation. Example : 3 people using account ina book. 
A must know only A's details. Similary B must know B's account details and similary with C. 
We have to make sure that B,C do not know about A and vice versa. In our daily life by using
user name and password we are able to access our data. So we need an authetication process to allow access. 
Without the authentication the data is still available but it needs to be hidden. Absraction is the process
of hiding process from the users. For instance we withdrow money from ATM card. 
On the outside st the user interface we 1. swipe the card, 2  enter the money needed . 3 with draw the cash . But
with in the ATM the moment we insert the card and enter the pin, and enter the money needed , 
the ATM machine searches for available balace and checks if money can be given or not . 
These process are not visible to us . This is callled abstraction . So internal details are hidden. '''


# Public data



class Person1:
    # fees=10000 # class variables inside the class
    def __init__(self,name,dob,city):
        self.name=name
        self.dob=dob
        self.city=city 
        
class Student12(Person1):
    fees=10000
    no_of_students=0
    def __init__(self,rollno,name,dob,city):
        super().__init__(name,dob,city)
        self.rollno=rollno
        Student12.no_of_students+=1
    def address(self):
        addres=f' \n Name : {self.name} ,\n Roll no: {self.rollno},\n DOb : {self.dob}, \n City : {self.city} '
        return addres
    
    def pay_fees(self,amount):
        return self.fees-amount


class DADS(Student12):
    fees=5000 # fees for DADS alone changed now
    def __init__(self,name,rollno,dob,city,year):
        super().__init__(name,rollno,dob,city)
        self.year=year
class Teacher1(Person1):
    def __init__(self, name, dob,rollno, city,stu=[]):
        super().__init__(name, rollno,dob,city)
        self.Student12=stu
    def show_students(self):
        for i in self.Student12:
            print(i.name)


stu1=DADS('Abhishek',100,1990,'Bareilly',2018)
stu2=DADS('Anand',101,1999,'Lucknow',2009)
stu3=DADS('Rohit',102,2000,'Dehli',2010)
stu4=DADS('Mohit',104,2010,'Chennai',2020)
t1=Teacher1('Riddhi',105,'India',[stu1,stu2])
print(stu1.year,stu1.name,stu1.rollno)














































