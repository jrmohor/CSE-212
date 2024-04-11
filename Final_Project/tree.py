
###Complete the Code here!

def is_valid_bst(root):
    def is_valid(node, min_val, max_val):
        if not node:
            return True
        if not min_val < node.value < max_val:
            return False
        return is_valid(node.left, min_val, node.value) and is_valid(node.right, node.value, max_val)
    
    return is_valid(root, float('-inf'), float('inf'))

# Usage:
# Assuming bst is the root of our BST from the previous example
print(is_valid_bst(bst.root))  # Output: True
