class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next  

    def insert(self,head,data): 
        if not head:
            self.head = self.tail = Node(data)
        else:
            self.tail.next = self.tail = Node(data)
        return self.head


mylist = Solution()

node0 = Node(2)
node1 = Node(3)
node2 = Node(4)
node3 = Node(1)



