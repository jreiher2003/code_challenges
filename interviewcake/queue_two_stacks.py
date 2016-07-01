# Implement a queue with 2 stacks. 
# Your queue should have an enqueue 
# and a dequeue function and it 
# should be "first in first out" 
# (FIFO).
class Stacks(object):
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

q = Stacks()
for i in range(10):
    print q.enqueue(i)

print "\n"

for i in xrange(10):
    print q.dequeue()