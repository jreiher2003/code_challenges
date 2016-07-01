class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def bst_checker(root):

    # start at the root, with an arbitrarily low lower bound
    # and an arbitrarily high upper bound
    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    # depth-first traversal
    while len(node_and_bounds_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        # if this node is invalid, we return false right away
        if (node.value < lower_bound) or (node.value > upper_bound):
            return False

        if node.left:
            # this node must be less than the current node
            node_and_bounds_stack.append((node.left, lower_bound, node.value))
        if node.right:
            # this node must be greater than the current node
            node_and_bounds_stack.append((node.right, node.value, upper_bound))

    # if none of the nodes were invalid, return true
    # (at this point we have checked all nodes)
    return True



