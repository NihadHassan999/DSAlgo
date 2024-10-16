# Index

Basic syntax usage guide for top data structures (1-8), plus other important stuff.

[1. Arrays and Hashing](#1-arrays-and-hashing)<br>
[2. Two Pointers](#2-two-pointers)<br>
[3. Sliding Window](#3-sliding-window)<br>
[4. Stack](#4-stack)<br>
[5. Binary Search](#5-binary-search)<br>
[6. Linked List](#6-linked-list)<br>
[7. Trees](#7-trees)<br>
[8. Graphs](#8-graphs)<br>
[9. String Iteration methods](#9-string-iteration-methods)<br>
[10. Count characters in string - 2 methods](#10-count-characters-in-string---2-methods)

______________________
______________________
# 1. Arrays and Hashing
______________________
______________________
**Usage Syntax:**
```python
# Creating an array
arr = [1, 2, 3, 4, 5]

# Creating a hash table (dictionary in Python)
hash_table = {'a': 1, 'b': 2, 'c': 3}
```

**Operations Syntax:**
```python
# Access
element = arr[2]  # O(1)
value = hash_table['b']  # O(1)

# Insertion
arr.append(6)  # O(1) on average
hash_table['d'] = 4  # O(1)

# Deletion
arr.remove(3)  # O(n) in worst case
del hash_table['c']  # O(1)
```

**Traversal Syntax:**
```python
# Iteration over an array
for num in arr:  # O(n)
    print(num)

# Iteration over a hash table
for key, value in hash_table.items():  # O(n)
    print(key, value)

# Recursion over an array
def traverse_array(arr, index=0):
    if index == len(arr):  # Base case: end of array
        return
    print(arr[index])  # Process the current element
    traverse_array(arr, index + 1)  # Recursive call for the next element

arr = [1, 2, 3, 4, 5]
traverse_array(arr)  # Output will be 1 2 3 4 5
```

**Time and Space Complexity:**
- **Time Complexity:** 
  - Access: O(1)
  - Search: O(n) for arrays, O(1) for hash tables
  - Insertion: O(1) (average for arrays), O(1) for hash tables
  - Deletion: O(n) for arrays, O(1) for hash tables
- **Space Complexity:** O(n) for arrays and hash tables

______________________
______________________
# 2. Two Pointers
______________________
______________________

**Usage Syntax:**
```python
# Two pointers approach in an array
arr = [1, 2, 3, 4, 5]
left, right = 0, len(arr) - 1
```

**Operations Syntax:**
```python
while left < right:
    # Some condition involving arr[left] and arr[right]
    left += 1
    right -= 1
```

**Traversal Syntax:**
```python
# Iterate with two pointers
for i in range(len(arr)):
    # Use i as a single pointer
```

**Time and Space Complexity:**
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

______________________
______________________
# 3. Sliding Window
______________________
______________________

**Usage Syntax:**
```python
# Sliding window for a fixed size
arr = [1, 2, 3, 4, 5]
window_size = 3
```

**Operations Syntax:**
```python
# Calculate sum of first window
window_sum = sum(arr[:window_size])

# Slide the window
for i in range(window_size, len(arr)):
    window_sum += arr[i] - arr[i - window_size]
```

**Traversal Syntax:**
```python
# While sliding the window
for start in range(len(arr) - window_size + 1):
    current_window = arr[start:start + window_size]
```

**Time and Space Complexity:**
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) for fixed-size windows, O(k) for variable-size (where k is the size of the current window)

- So in general for any <b>substring s1</b> in a <b>given string s2</b>, the total number of windows for the same would be <b>len(s2) - len(s1) + 1</b>

______________________
______________________
# 4. Stack
______________________
______________________

**Usage Syntax:**
```python
# Using a list as a stack
stack = []
```

**Operations Syntax:**
```python
# Push
stack.append(1)  # O(1)

# Pop
top = stack.pop()  # O(1)

# Peek
top = stack[-1]  # O(1)
```

**Traversal Syntax:**
```python
# Iterate over stack
for item in stack:  # O(n)
    print(item)
```

**Time and Space Complexity:**
- **Time Complexity:** O(1) for push, pop, and peek
- **Space Complexity:** O(n)

______________________
______________________
# 5. Binary Search
______________________
______________________

**Usage Syntax:**
```python
# Binary search implementation
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
```

**Operations Syntax:**
```python
while left <= right:
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1
```

**Traversal Syntax:**
```python
# Not applicable as binary search is not a traversal
```

**Time and Space Complexity:**
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1) for iterative; O(log n) for recursive (due to call stack)

______________________
______________________
# 6. Linked List
______________________
______________________

**Usage Syntax:**
```python
# Node definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List definition
class LinkedList:
    def __init__(self):
        self.head = None
```

**Operations Syntax:**
```python
# Insertion
def insert(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node  # O(1)

# Deletion
def delete(head, key):
    if head is None:
        return head
    if head.data == key:
        return head.next
    current = head
    while current.next:
        if current.next.data == key:
            current.next = current.next.next
            return head
        current = current.next  # O(n)
```

**Traversal Syntax:**
```python
# Iteration over a linked list
current = head
while current:
    print(current.data)
    current = current.next  # O(n)
```

**Time and Space Complexity:**
- **Time Complexity:** 
  - Access: O(n)
  - Insertion: O(1) (at head), O(n) (at other positions)
  - Deletion: O(n)
- **Space Complexity:** O(n)

______________________
______________________
# 7. Trees
______________________
______________________

**Usage Syntax:**
```python
# Node definition
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
```

**Operations Syntax:**
```python
# Insertion in BST
def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root  # O(h) where h is height of tree

# Deletion in BST
def delete_node(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # Node with two children
        min_larger_node = root.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        root.val = min_larger_node.val
        root.right = delete_node(root.right, min_larger_node.val)
    return root  # O(h)
```

**Traversal Syntax:**
```python
# Pre-order traversal (recursive)
def pre_order(root):
    if root:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)  # O(n)

# In-order traversal (iterative)
def in_order(root):
    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.val)
        current = current.right  # O(n)
```

**Time and Space Complexity:**
- **Time Complexity:** 
  - Insertion: O(h)
  - Deletion: O(h)
  - Traversal: O(n)
- **Space Complexity:** O(h) for recursive traversal, O(n) for non-recursive

______________________
______________________
# 8. Graphs
______________________
______________________

**Usage Syntax:**
```python
# Using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```

**Operations Syntax:**
```python
# Adding an edge
def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)  # O(1)

# Removing an edge
def remove_edge(graph, u, v):
    graph[u].remove(v)
    graph[v].remove(u)  # O(n) in worst case
```

**Traversal Syntax:**
```python
# Depth-First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited  # O(V + E)

# Breadth-First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    return

 visited  # O(V + E)
```

**Time and Space Complexity:**
- **Time Complexity:** 
  - Adding edge: O(1)
  - Removing edge: O(n) in the worst case
  - Traversal: O(V + E) where V is vertices and E is edges
- **Space Complexity:** O(V)

______________________
______________________
# 9. String Iteration methods
______________________
______________________

- **for r in range(len(s)):** When you need indices to manipulate the string (e.g., sliding window, two-pointer technique).
- **for r in s:** When you only care about characters, not their positions.
- **for i, r in enumerate(s):** When you need both index and character in the loop.
- **for r, c in zip(range(len(s)), s):** Similar to enumerate(), but useful when pairing with another sequence.
- **for r in reversed(range(len(s))):** When you need to iterate backward by index.
- **for r in reversed(s):** When you want to iterate backward over the characters.
- **for r in range(len(s) - 1, -1, -1):** When you need a custom reverse loop with full control over steps and boundaries.
- **List comprehension with enumerate():** When you want a compact and readable way to collect results into a list.


______________________
______________________
# 10. Count characters in string - 2 methods
______________________
______________________

## Using List
```python
def count_characters_list(s):
    count = [0] * 26  # List for 26 letters
    for char in s:
        count[ord(char) - ord('a')] += 1
    return count
```
## Using Hashmap
```python
def count_characters_hashmap(s):
    count = {}
    for char in s:
        count[char] = 1 + count.get(char, 0)
    return count
```
