class Employee:
# init is the constructor and self is the default argument passing(the instance created)

    raise_amount = 1.20
    number_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        self.number_of_employees += 1
        print(self.number_of_employees)


    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    

    def apply_raise(self):
        self.pay = int(self.pay) * self.raise_amount

print("Number of Employees Initially : ", Employee.number_of_employees)

emp_1 = Employee('Jijo', 'James', '25000')
emp_2 = Employee('Allen', 'F', '50000')

print("Number of Employees Finally : ", Employee.number_of_employees)


Employee.raise_amount = 1.25
#changing raise_amount using class variable

emp_2.raise_amount = 1.3
#changing raise_amount using instance variable

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


print("\n", emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)