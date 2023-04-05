class AdultException(Exception):
    pass

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_minor_age(self):
        if self.age > 18:
            raise AdultException
        else:
            return self.age

    def display(self):
        try:
            print(f"Age : {self.get_minor_age()}")
        except AdultException:
            print("Person is an adult")
        finally:
            print(f"Name : {self.name}\n")
        


Person("Ravi", 17).display()
Person("Sunny",21).display()