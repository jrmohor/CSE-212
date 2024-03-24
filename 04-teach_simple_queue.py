"""
CSE212 
(c) BYU-Idaho
04-Teach - Problem 1 

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class Simple_Queue:
    """
    Maintain a Queue using a List
    """

    def __init__(self):
        """
        Initialize the empty queue using a Python List.  
        """
        self.queue = []

    def enqueue(self, value):
        """
        Enqueue the value provided into the queue
        """
        self.queue.append(value) # This line need to be fix #Solution:use append, and remove the 0
        #self.queue.insert(0, value)

    def dequeue(self):
        """
        Dequeue the next value and return it
        """
        if len(self.queue) <= 0:
            raise IndexError()
        # Solution 1 - these should be [0] in both lines
        value = self.queue[0] #value = self.queue[1]
        del self.queue[0] #del self.queue[1]
        return value

# Test Cases

# Test 1
# Scenario: Enqueue one value and then Dequeue it.
# Exepcted Result: It should display 100
print("Test 1")
queue = Simple_Queue()
queue.enqueue(100)
value = queue.dequeue()
print(value)
# Defect(s) Found:in the dequeue function should be removing [0] instead of [1]

print("=================")

# Test 2
# Scenario: Enqueue multiple values and then Dequeue all of them
# Exepcted Result: It should display 200, then 300, then 400 in that order
print("Test 2")
queue = Simple_Queue()
queue.enqueue(200)
queue.enqueue(300)
queue.enqueue(400)
value = queue.dequeue()
print(value)
value = queue.dequeue()
print(value)
value = queue.dequeue()
print(value)
# Defect(s) Found: in the enqueue function should use append instead of insert

print("=================")

# Test 3
# Scenario: Dequeue from an empty Queue
# Exepcted Result: An exception should be raised
print("Test 3")
queue = Simple_Queue()
try:
    queue.dequeue()
    print("Oops ... This shouldn't have worked.")
except IndexError:
    print("I got the exception as expected.")
# Defect(s) Found: No error



