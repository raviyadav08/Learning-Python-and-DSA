
class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.email = fname +'.'+ lname +'@gmail.com'
        self.pay = pay
        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.fname} {self.lname}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, fname, lname, pay, employee = None):
        super().__init__(fname, lname, pay)
        self.employee = employee

        if employee is None:
            employee = []
        else:
            self.employee = employee
    
    def add_emps(self,emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_emps(self,emp):
        if emp in self.employee:
            self.employee.remove(emp)
    
    def print_emps(self):
        print(f'Employees Under {man1.fname}') 
        for emp in self.employee:
            print('-->',emp.fullname())



emp1 = Employee('Shobha','Yadav',49000)
dev2 = Employee('Rahul','Yadav',50000)
emp3 = Employee('Pooja','Yadav',45000)

dev1 = Developer('Ravi','Yadav',15000,'Python')

man1 = Manager('Akash','Shrivastava',20000,[dev1])
man1.add_emps(dev2)
man1.remove_emps(dev1)

print(man1.fullname)
man1.print_emps()


# print(dev1.email)
# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)



# print(emp1.pay)
# emp1.raise_amount = 1.05
# emp1.apply_raise()
# print(emp1.pay)

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# print(emp3.raise_amount)

