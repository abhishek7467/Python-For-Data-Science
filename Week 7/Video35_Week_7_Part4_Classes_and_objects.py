'''                   Class Inheriteance         '''


# Parent class
class Person():
    def __init__(self,n,a):
        self._name=n
        self._age=a
    def birthday(self):
        print('Happy Birthday , you were : ',self._age)
        self._age +=1
        print('Now your age is  : ',self._age)

    def __str__(self):
        return self._name + ' is  ' +  str(self._age)  + ' Years old .'

    
    # Chold  Class / sub class / Derived class

class Employee(Person):
    def __init__(self,n,a,i):
        super().__init__(n,a)# invoking the init method of the super classs
        self._id =i
    
    def calculate_pay(self,hours_worked):
        rate_of_pay= 7.5
        if self._age >=21:
            rate_of_pay +=2.50
        return hours_worked * rate_of_pay

print(' A Person only object  ')
p=Person('Abhishek ', 24)
print('The person  object p is :', p)

print('*' * 50)

print('An Employee object')
e=Employee('Abhi',30,707707)
e.birthday()
print(e, 'Pay of employee for 40 hours is  :  ',e.calculate_pay(40))
print('*' * 50)




# Inherit from Employee class
class SalsePerson(Employee):
    def __init__(self, n, a, i,r,s):
        super().__init__(n,a,i) 
        self._region=r
        self._sales=s 

    def bonus(self):
        return self._sales*0.5
    def __str__(self): # AN Overring MEthod
        return self._name + ' is  ' +  str(self._age)  + ' Years old , ID is : ' + str (self._id) + 'region is ' + str(self._region)


print('Sales Person object ')
s=SalsePerson('Ramesh',24,34532,'UK',12000)
s.birthday()
print(s,' Pay of this object for 40 hrs is  ', s.calculate_pay(40))
print('Bonus is  : ', s.bonus())








