class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
        p = Node(data)        
        if head==None:
            head=p
        elif head.next==None:
            head.next=p
        else:
            start=head
            while(start.next!=None):
                 start=start.next
            start.next=p
        return head 
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next  
    def removeDuplicates(self,head):
        current = head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        return head


mylist= Solution()
T=6
head=None
for i in range(T):
    head=mylist.insert(head,i)   
head=mylist.removeDuplicates(head)
mylist.display(head);