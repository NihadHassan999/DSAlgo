'''

You are given the root of a binary tree root. Invert the binary tree and return its root.

Example 1:



Input: root = [1,2,3,4,5,6,7]

Output: [1,3,2,7,6,5,4]
Example 2:[]



Input: root = [3,2,1]

Output: [3,1,2]
Example 3:

Input: root = []

Output: []

'''

# Treenode Definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        # Base case, stops the recursion if root is empty
        if root is None:
            return None
        
        # Swap the left and right children of root
        root.left, root.right = root.right, root.left

        # Perform recursion on left child of root
        self.invertTree(root.left)

        # Perform recursion on right child of root
        self.invertTree(root.right)

        return root
    
'''
Time complexity : O(n)  because each node is visited once at least
Space complexity : O(h) where h is height of tree, for recursion

for more deeper trees, iteration using queue is preferred in order to prevent stack overflow (limit of 1000 trees recursion)


'''