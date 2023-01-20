
class Employee:
# init is the constructor and self is the default argument passing(the instance created)

    raise_amount = 1.20
    number_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        #self.number_of_employees += 1
        #print(self.number_of_employees)


    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    

    def apply_raise(self):
        self.pay = int(self.pay) * self.raise_amount
    

    @classmethod # convert a fn to a class method
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_sting(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)
    
    @staticmethod # one doesn't require a default argument
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6 :
            return False
        return True

emp_1 = Employee('Jijo', 'James', '25000')
emp_2 = Employee('Allen', 'F', '50000')


emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_sting(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2023, 1, 22)
print('\n', Employee.is_workday(my_date))