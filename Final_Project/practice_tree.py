class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

### Write the solution code here.###

# Example usage:
bst = TreeNode(20)
bst.left = TreeNode(9)
bst.right = TreeNode(25)
bst.left.left = TreeNode(5)
bst.left.right = TreeNode(12)
bst.left.right.left = TreeNode(11)
bst.left.right.right = TreeNode(14)
bst.right.right = TreeNode(30)

target = 9
print(f"Inorder successor of {target}: {find_inorder_successor(bst, target)}")

target = 14
print(f"Inorder successor of {target}: {find_inorder_successor(bst, target)}")

target = 30
print(f"Inorder successor of {target}: {find_inorder_successor(bst, target)}")
