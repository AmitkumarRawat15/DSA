# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)


def reverse_string(s):
    stack = Stack()
    for i in s:
        stack.push(i)

    revrstr = ""
    while not stack.is_empty():
        revrstr += stack.pop()

    print(revrstr)

reverse_string("We will conquere COVID-19")