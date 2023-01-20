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

class Developer(Employee):
    raise_amount = 1.3

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emp(self):
        for emp in self.employees:
            print(emp.full_name())


dev_1 = Developer('Jijo', 'James', 25000, 'Python')
dev_2 = Developer('Allen', 'F', 25000, 'Golang')

mgr_1 = Manager('Sajjad', 'S', 35000, [dev_1])

print(mgr_1.email)
mgr_1.print_emp()
mgr_1.add_emp(dev_2)
print('\n')
mgr_1.print_emp()
print('\n')
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()



'''
print(dev_2.pay)
Developer.apply_raise(dev_2)
print(dev_2.pay)


print(dev_2.email)
print(dev_2.prog_lang)
'''

