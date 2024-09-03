class QueueWithStacks:
    def __init__(self):
        self.stack_in = []  
        self.stack_out = []  

    def enqueue(self, x):
        self.stack_in.append(x)  

    def dequeue(self):
        if not self.stack_out:  
            while self.stack_in:  
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop() if self.stack_out else None  

q = QueueWithStacks()
q.enqueue(5)
q.enqueue(6)
print(q.dequeue())  
print(q.dequeue())  
