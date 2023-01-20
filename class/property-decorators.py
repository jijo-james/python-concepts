class Employee:

    raise_amount = 1.20
    number_of_employees = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        print('Deleted..')
        self.first = None
        self.last = None
    

emp_1 = Employee('Jijo', 'James')
emp_2 = Employee('Allen', 'F')

emp_1.full_name = 'Adharsh Shaji'

print(emp_1.first)
print(emp_1.email)
print(emp_1.full_name)

del emp_1.full_name