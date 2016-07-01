# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(TreeNode):
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        nodeStack = [root];
        depthStack = [1];
        maxDepth = 0;
        while len(nodeStack)>0:
            node = nodeStack.pop();
            depth = depthStack.pop();
            maxDepth = maxDepth if maxDepth > depth else depth
            if node.left != None:
                nodeStack.append(node.left)
                depthStack.append(depth+1)
            if node.right != None:
                nodeStack.append(node.right)
                depthStack.append(depth+1)
        return maxDepth

        