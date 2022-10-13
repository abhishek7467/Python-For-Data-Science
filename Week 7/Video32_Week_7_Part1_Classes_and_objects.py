# An example EMployee class to demostrate the class and objects

class Employee:
    def set_data(self,n,a,s):
        self._name=n  
        self._age=a 
        self._salary = s

    def deisplay_data(self):

        print('\n Name  :  ', self._name  )
        print('Age  : ', self._age)
        print('Salary :  ',self._salary)


# Create Objects of EMployee class
e1=Employee()
e1.set_data('Abhishek',21,218998)
e2=Employee()
e2.set_data('Kumar',20,893789)
e1.deisplay_data()
e2.deisplay_data()

e1.set_data('Ridhi',23,8736834)
e1.deisplay_data()






































