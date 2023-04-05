"""
Create an iterator for fibonacci series in such a way that each next returns the next element from fibonacci series.
The iterator should stop when it reaches a limit defined in the constructor.
"""

class Fibonnaci():
    def __init__(self,limit):
        self.f1 = 0
        self.f2 = 1
        self.fibo = 0
        self.limit = limit
        self.index = 0


    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < self.limit:
            if self.index == 0:
                print("Fibo:",self.fibo,"\n")

            self.fibo = self.f1 + self.f2
            self.f2 = self.f1
            self.f1 = self.fibo
            print("Fibo:",self.fibo,"\n")
            self.index += 1

        else:
            raise StopIteration

f = iter(Fibonnaci(10))
while True:
    try:
        next(f)
    except StopIteration:
        break
    

