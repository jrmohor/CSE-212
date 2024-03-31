# Understanding Stacks

### What is a Stack?

A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed. Think of a stack as a collection of items stacked one on top of another, similar to a stack of plates.

### Stack Function:

In data structure the "function stack" refers to the stack of function calls made during the execution of a program. Each time a function is called, its parameters, local variables, and the return address are pushed onto the stack. When the function completes execution, its stack frame is popped off the stack, and control returns to the caller. Understanding the function stack is essential for understanding program execution flow and debugging.

### Operations on a Stack:

1. **Push:** Adds an item to the top of the stack.
2. **Pop:** Removes and returns the top item from the stack.
3. **Peek (or Top):** Returns the top item from the stack without removing it.
4. **isEmpty:** Checks if the stack is empty.
5. **Size:** Returns the number of items in the stack.

![Stack](https://static-assets.codecademy.com/ugc_articles/create_a_stack_in_python/stack.png)

### Implementation of a Stack in Python:

Python provides several ways to implement stacks. One common approach is to use a list, where elements can be added or removed from the end of the list. However, Python also provides a module called collections that offers a specialized data structure called deque, which can efficiently implement a stack.

Here's how you can use deque to create a stack in Python:

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())  # Output: 3
print(stack.pop())   # Output: 3
print(stack.size())  # Output: 2

```

Let's see another example of using a stack to reverse a string:

```python
def reverse_string(input_string):
    stack = deque()
    reversed_string = ''
    for char in input_string:
        stack.append(char)
    while stack:
        reversed_string += stack.pop()
    return reversed_string

input_str = "Hello, World!"
print(reverse_string(input_str))  # Outputs: "!dlroW ,olleH"

```

## Let's do it

Now that we understand the basics of stacks, let's move on to solving a problem using stacks.

### Problem Statement

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

**Example:**

Input: "()[]{}"
Output: True

Input: "([)]"
Output: False

### Let's implement this, using the Python file below,

- [stack file](stack.py)

Now, it's your turn to solve this problem! Try to implement the solution on your own. Once you're done, you can check the solution using the provided link.

- [solution file](solution.py)

### Now it's your turn to do it!

Now that we have reviewed an example, it's time for you to try solving a problem on your own! Below you have the file to apply what you learned in this tutorial

- [practice file](practice_stack.py)

### Statement Problem: Next Greater Element

Given an array, find the Next Greater Element (NGE) for every element. The Next Greater Element for an element x is the first greater element on the right side of x in the array. If there is no greater element on the right side, then the output should be -1.

**Example:**

Input: [4, 5, 2, 10, 8]

Output: [5, 10, 10, -1, -1]





