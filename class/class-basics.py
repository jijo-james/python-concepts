# class name is the only thing in python follows camel styling all others use _ naming format
class Employee:
# init is the constructor and self is the default argument passing(the instance created)
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


    def full_name(self):
        return '{} {}'.format(self.first,self.last)


emp_1 = Employee('Jijo', 'James', '25000')
emp_2 = Employee('Allen', 'F', '50000')
print(emp_1.email)
print(emp_1.full_name())
print(emp_2.email)
print(emp_2.full_name())