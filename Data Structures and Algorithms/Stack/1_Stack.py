from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return print(self.container[-1])
    
    def is_Empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    def reverse(self,input):
        list = ""
        count = 0
        for char in input:
            self.container.append(char)
            count += 1
        
        for i in range(count):
            list += self.container.pop()
        return print(list)
    
        
    
if __name__ == "__main__":
    s = Stack()
    
    input_string = "We will conquere COVID-19"
    s.reverse(input_string)

    # s.push(10)
    # s.push(20)
    # s.push(30)
    # print(s.is_Empty())
    # print(s.size())
    # print(s.pop())
    # print(s.pop())
    # print(s.pop())
    # print(s.is_Empty())
