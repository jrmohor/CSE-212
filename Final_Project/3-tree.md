# Tutorial: Understanding Tree Data Structure

## Introduction
A tree is a hierarchical data structure that consists of nodes connected by edges. It is widely used in computer science for organizing and representing hierarchical relationships between elements. Trees have various applications, including in file systems, databases, and network routing algorithms.

## Binary Trees
A binary tree is a type of tree in which each node has at most two children, referred to as the left child and the right child. The topmost node of a binary tree is called the root node. Binary trees can be used to implement more advanced data structures like binary search trees (BSTs).

![tree](https://www.tutorialspoint.com/data_structures_algorithms/images/binary_tree.jpg)

![dif_trees](https://miro.medium.com/v2/resize:fit:16000/1*CMGFtehu01ZEBgzHG71sMg.png)


## Inserting into a Binary Search Tree (BST)
A binary search tree (BST) is a type of binary tree in which the nodes are arranged in a specific order that allows for efficient search, insertion, and deletion operations. In a BST, for each node:

* All nodes in the left subtree have values less than the node's value.
* All nodes in the right subtree have values greater than the node's value.

To insert a new node into a BST, we start from the root and compare the new node's value with the current node. If the new node's value is less than the current node's value, we go to the left subtree; if it's greater, we go to the right subtree. We repeat this process recursively until we find an appropriate spot to insert the new node.

![bts](https://static.javatpoint.com/ds/images/binary-search-tree12.png)


## BST in Python
In Python, binary search trees can be implemented using classes to represent nodes and methods for insertion, deletion, and traversal. Below is a simple implementation of a BST in Python:

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        else:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)
```
### Let's demonstrate how to use the BST class:
```python
bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
```
### After inserting these values, the binary search tree would look like this:
```   
    10
   /  \
  5    15
 / \
3   7
```

## Now let's get to work and apply what we've learned:

Now that you have a basic understanding of binary search trees, here's a problem for you to solve: 

### Problem:

Given a binary search tree, write a function to determine if it is a valid BST.
#### Example usage:
```
bst = TreeNode(10)
bst.left = TreeNode(5)
bst.right = TreeNode(15)
bst.left.left = TreeNode(3)
bst.left.right = TreeNode(7)
```

- [tree file](tree.py)

After trying, if you get stuck here is the solution to the example problem

- [solution](solution.py)

### Now it's your turn to do it!

#### Here's an example problem involving a binary search tree (BST):

Problem: Find the Inorder Successor in a BST
Given a binary search tree (BST) and a value target, write a function to find the inorder successor of the node containing target in the BST. If the target node has a right subtree, then the inorder successor is the leftmost node in the right subtree. Otherwise, it's the nearest ancestor whose left child is also an ancestor of the target node.

For example, consider the following BST:
```
        20
       /  \
      9    25
     / \     \
    5   12    30
       /  \
      11   14
```
Write a function find_inorder_successor(root, target) that takes the root of the BST and the target value as input and returns the value of the inorder successor. If no such successor exists (e.g., the target is the largest value in the tree), return None.

- [practice file](practice_tree.py)

## Summary

This concludes our tutorial on the tree data structure, focusing on binary trees and binary search trees. Trees are fundamental in computer science and understanding them is crucial for developing efficient algorithms and solving various problems.