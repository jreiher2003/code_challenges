class Node:
    def __init__(self,data):
        self.right=self.left=None
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

    def getHeight(self, root):
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 0 
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

myTree = Solution()
root = None 
for i in range(5):
    data = i 
    root = myTree.insert(root, data)
    height = myTree.getHeight(root)
print height