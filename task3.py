class Stack:
    def __init__(self):
        self.items=[]
    def push(self,k):
        self.items.append(k)
    def pop(self):
        if len(self.items)==0:
            print("Empty stack")
        else:
            return self.items.pop()
    def peek(self):
        if len(self.items)==0:
            print("Stack is empty")
        else:
            return self.items[-1]
    def is_empty(self):
        if len(self.items)==0:
            return True
        else:
            return False
    def size(self):
        return len(self.items)
    def display(self):
        return str(self.items)
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    return reversed_str
y=Stack()
y.push("Ali")
y.push("Ahmad")
print(y.peek())
print(y.pop())
print(y.size())
print(y.display())
print(reverse_string("hello"))





