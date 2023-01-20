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
        return '{} {}'.format(self.first, self.last)
    

    def apply_raise(self):
        self.pay = int(self.pay) * self.raise_amount
    
    def __repr__(self) -> str:
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
    
    def __str__(self) -> str:
        return '{} - {}'.format(self.full_name(), self.email)



emp_1 = Employee('Jijo', 'James', 25000)
emp_2 = Employee('Allen', 'F', 25000)

print(emp_1.__repr__())
print(emp_1.__str__())