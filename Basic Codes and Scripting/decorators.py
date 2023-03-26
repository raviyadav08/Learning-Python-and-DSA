class Employee:

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        # self.email = fname +'.'+ lname + '@email.com'
        self.pay = pay
    
    @property
    def email(self):
        return f'{self.fname}.{self.lname}@email.com'

    @property
    def fullname(self):
        return f'{self.fname} {self.lname}'


    @fullname.setter
    def fullname(self,name):
        fname , lname = name.split(' ')
        self.fname = fname
        self.lname = lname
    
    
    @fullname.deleter
    def fullname(self):
        print('Deleting Employee Records')
        self.fname = None
        self.lname = None
        self.pay = None

    def __repr__(self):
        return f'Employee({self.fullname},{self.pay})'
    
    def __str__(self) -> str:
        return f'{self.fullname},{self.pay}'
        

emp1 = Employee('Jack','Sparrow',10000)
emp1.fullname = 'Deus ExMachina'

print(emp1.fname)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname

print(emp1.fname)


# print(emp1.__repr__())
# print(emp1.__str__())