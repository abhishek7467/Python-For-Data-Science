''' Thre are two ways to inialize an object:
1- get_data()/set_data()
2- __init__() '''





# demonstrate init abd del functions in Employee class
class Employee:
    '''An Epmloyee class to create and manipulate Employee objects'''
    def __init__(self,n='',a=0,s=0.0):
        self._name=n
        self._age=a
        self._salary=s
        


    def set_data(self,n,a,s):
        self._name=n  
        self._age=a 
        self._salary = s

    def deisplay_data(self):

        print('\n Name  :  ', self._name  )
        print('Age  : ', self._age)
        print('Salary :  ',self._salary)

    # def __del__(self):
    #     print('Deleting the Object is : ', str(self))

# Create Objects of EMployee class
e1=Employee()
e1.set_data('Abhishek',21,218998)
e1.deisplay_data()

e2=Employee()
e2.deisplay_data()


e3=Employee()
e3.set_data('Kumar',20,893789)
e3.deisplay_data()

e1.set_data('Ridhi',23,8736834)
e1.deisplay_data()




# Demostrate class variable 

class Employee1:     
    instace_count=0
    def __init__(self,n=' ',a=0,s=0.0):
        Employee1.increment_instance_count()
        self._name=n
        self._age=a
        self._salary=s

    def set_data(self,n,a,s):
        self._name=n  
        self._age=a 
        self._salary = s

    def deisplay_data(self):

        print('\n Name  :  ', self._name  )
        print('Age  : ', self._age)
        print('Salary :  ',self._salary)


    @classmethod
    def increment_instance_count(cls):
        cls.instace_count+=1 

e1=Employee1()
e2=Employee1('Abhishek',21,23423)
print('Number of Emloyee objects created so far : ',Employee1.instace_count)

e3=Employee1('Suresh',23,13000)
print('Number of Emloyee objects created so far : ',Employee1.instace_count)



# vars and dir function
'''
vers()-->Dictionary
dir()-->List
'''
print('\n ')

print(vars(Employee))
print('\n ')

print(vars(Employee1))

print('\n ')
print(dir(Employee))
print('\n ')
print(dir(Employee1))









