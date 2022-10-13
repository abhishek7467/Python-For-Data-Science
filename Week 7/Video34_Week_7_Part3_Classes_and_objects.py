# Implement operator overloading on the quality class

class Quality:
    def __init__(self,v=0):
        self._value=v
    def __add__(self,other):
        new_value=self._value+other._value
        return Quality(new_value)
    def __sub__(self,other):
        new_value=self._value- other._value
        return Quality(new_value)

    def __pow__(self,other):
        new_value=self._value**other._value
        return new_value

    # def __Greater__(self,other):
    #     new_value=self._value > other._value
    #     return new_value

    # def __it__(self,other):
    #     new_value=self._value <= other._value
    #     return new_value    
    def __str__(self):
        return str(self._value)

q1=Quality(12)
q2=Quality(10)
q3=Quality()
print(f'q1 = {q1} , q1 = {q2}')

q3=q1+q2 
print(f'The sum is {q3}')

q4=Quality()
q4=q1-q2
print(f'The sunstraction is : {q4}')

q5=Quality()
q5=q1**q2 
print(f'The Power is : {q5}')

# q6=Quality()
# q6=q1 > q2
# print(f'{q1} is greater then {q2}')

# q6=Quality()
# q6=q1 <= q2
# print(f'{q1} is less then {q2}')


# A example to demonstrate Containership


class Department:
    def set_department(self):

        self._id = input('Enter Department ID  :  ')
        self._name = input('Enter Department name :  ')

    def display_department(self):
        print('Department Id : ',self._id)
        print('Department name : ',self._name)

class  Employee3:
    def set_employee(self):
        self._id = input('Enter employee ID :    ')
        self._name =input('Enter EMployee name  :  ')
        self._dept = Department()
        self._dept.set_department()

    def display_employee(self):
        print('Employee ID  :  ',self._id)
        print('Employee Name  :  ',self._name)
        self._dept.display_department()


emp = Employee3()
emp.set_employee()
print('-'*30)
emp.display_employee()


