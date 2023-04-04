"""
Create a sample class named Employee with two attributes id and name
employee :
    id
    name
object initializes id and name dynamically for every Employee object created.
emp = Employee(1, "coder")
Use del property to first delete id attribute and then the entire object

"""

class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def display(self):
        print(f'{emp1.id} , {emp1.name}')

if __name__ == '__main__':
    emp1  = Employee(1,"coder")
    emp1.display()
    del emp1.id
    print(emp1.name)
    del emp1
    print(f'id :{emp1.id} \nname:{emp1.name}')
    
    