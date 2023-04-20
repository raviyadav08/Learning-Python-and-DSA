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
    
def match_dict(ch1,ch2):
    dict = {
    ')':'(',
    '}':'{',
    ']':'['
    }
    return dict[ch1] == ch2
    
def is_balanced(input):
    s = Stack()
    for char in input:
        if char == '(' or char == '{' or char == "[":
            s.push(char)
        if char == ')' or char == "}" or char == ']':
            if s.size() == 0:
                return False
            if not match_dict(char,s.pop()):
                return False
    return s.size() == 0
            
    
if __name__ == "__main__":
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))