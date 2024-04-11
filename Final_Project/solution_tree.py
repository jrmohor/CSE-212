class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_valid_bst(root):
    def is_valid(node, min_val, max_val):
        if not node:
            return True
        if not min_val < node.value < max_val:
            return False
        return is_valid(node.left, min_val, node.value) and is_valid(node.right, node.value, max_val)
    
    return is_valid(root, float('-inf'), float('inf'))

# Example usage:
bst = TreeNode(10)
bst.left = TreeNode(5)
bst.right = TreeNode(15)
bst.left.left = TreeNode(3)
bst.left.right = TreeNode(7)

print(is_valid_bst(bst))  # Output: True
