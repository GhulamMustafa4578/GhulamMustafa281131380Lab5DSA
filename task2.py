#Part2
class Queue():
    def __init__(self):
        self.ist=[]
    def enqueue(self,k):
        self.ist.append(k)
    def dequeue(self):
        if len(self.ist)==0:
            return False
        else:
            return self.ist.pop(0)
    def is_empty(self):
        return len(self.ist)==0
    def size(self):
        return len(self.ist)
    def display(self):
        return str(self.ist)
x=Queue()
x.enqueue("Asas")
x.enqueue("Lia")
print(x.dequeue())
print(x.is_empty())
print(x.size())
print(x.display())



a=Queue()
a.enqueue("Goti")
a.enqueue("Boti")
print(a.dequeue())
print(a.is_empty())
print(a.size())
print(a.display())