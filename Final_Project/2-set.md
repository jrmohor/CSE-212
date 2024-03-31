# Understanding Sets

## Introduction
Sets are a fundamental data structure in computer science used to store unique elements. They allow you to store and manipulate collections of items, ensuring that each item appears only once. Sets offer efficient methods for common set operations like intersection, union, and difference.

## Hashing and Sets
Sets are often implemented using hash tables, which enable fast access and retrieval of elements. Hashing is a technique where an element's value is converted into a unique hash code, which is then used as an index to store the element in a data structure like an array or a hash table. This allows for efficient lookup and insertion operations.

## Applications with Sets
Sets have various applications across different domains:
- Removing duplicates from a collection of elements
- Checking for membership (whether an element is present in a set)
- Performing set operations like union, intersection, and difference
- Filtering unique elements from a dataset
- Implementing algorithms such as graph algorithms, where sets can represent vertices or edges

### See this examples

![Set](https://media.geeksforgeeks.org/wp-content/uploads/20230504134511/insert.png)

![Set1](https://media.geeksforgeeks.org/wp-content/uploads/20230302134205/11-(1).png)

![Set2](https://media.geeksforgeeks.org/wp-content/uploads/20230504134511/insert.png)


## Sets in Python
In Python, sets are implemented using the `set` data type. Sets in Python are unordered collections of unique elements. They can be created using curly braces `{}` or the `set()` constructor. Python sets support various operations like adding elements, removing elements, checking for membership, and performing set operations.

## Example code using Set in Python
```python
# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Adding elements to a set
set1.add(6)

# Removing elements from a set
set2.remove(8)

# Checking for membership
print(2 in set1)  # Output: True

# Set operations
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6, 7}
print(set1.intersection(set2))  # Output: {4, 5, 6}
```

### Union:
```python
# The union of two sets A and B contains all the elements that are either in A or in B, or in both.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union_set = A.union(B)
print("Union of A and B:", union_set)
```
### Intersection:
```python
# The intersection of two sets A and B contains all the elements that are common to both A and B.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

intersection_set = A.intersection(B)
print("Intersection of A and B:", intersection_set)
```
### Difference:
```python
# The difference between two sets A and B, denoted as A - B, contains all the elements that are in A but not in B.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

difference_set = A - B
print("Difference of A and B:", difference_set)
```


## Now let's get to work and apply what we've learned:

Now that we understand the basics of set, let's move on to solving a problem using set.

### Problem Statement