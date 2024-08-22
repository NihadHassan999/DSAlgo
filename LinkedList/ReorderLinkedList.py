'''

Reorder Linked List
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:

Input: head = [2,4,6,8]

Output: [2,8,4,6]
Example 2:

Input: head = [2,4,6,8,10]

Output: [2,10,4,8,6]

'''

#Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        def find_middle(node):
            fast = slow = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverselist(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node 
            return prev

        def mergelist(l1,l2):
            while l2:
                next1 = l1.next
                next2 = l2.next
                l1.next = l2
                l2.next = next1
                l1 = next1
                l2 = next2
        if not head or not head.next:
            return 
        
        middle = find_middle(head)
        second_half = middle.next
        middle.next = None

        second_half = reverselist(second_half)
        mergelist(head, second_half)
