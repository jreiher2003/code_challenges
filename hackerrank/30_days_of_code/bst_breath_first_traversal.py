import sys

class Node:
    def __init__(self,data,right=None,left=None):
        self.right=right
        self.left=left
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        """this is right"""
        result, bf = [], [root]
        while bf:
            trav = [] 
            for n in bf:
                result += [n.data]
                
                if n.left:
                    trav += [n.left]
                if n.right:
                    trav += [n.right]
            bf = trav
        print " ".join([str(x) for x in result])
#not right
# t = Node(3, Node(2, Node(5)), Node(1, Node(4), Node(7)))

tree = Solution() 
tree.levelOrder(t)



