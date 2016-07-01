class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

def is_palindrome(l):
    head = l
    prev = None
    while l.next:
        l.prev = prev
        prev = l
        l = l.next
    tail = l
    tail.prev = prev
    while head is not tail and head.data == tail.data:
        head = head.next
        tail = tail.prev
    if head is tail:
        return True
    elif head.data == tail.data:
        return True
    else:
        return False
    
n=Node(1)
n.next=Node(2)
n.next=Node(1)
print is_palindrome(n)
n.next=Node(5)
print is_palindrome(n)
m=Node(5)
m.next=n
print is_palindrome(m)
    