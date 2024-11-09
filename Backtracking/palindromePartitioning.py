'''
131. Palindrome Partitioning
Solved
Medium
Topics
Companies
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''

'''
we are using dfs backtracking to use a palidrome helper function to check
for palindrome, using append and pop to add possible palindrome variations 
to our final result. We are using slicing to append.

-> create empty res and part
-> base case to stop everything in case dfs reached end of list,
    append to res and return
-> if pali is true, then append backtrack and pop backtrack
-> return res
-> create isPali function
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    res.append(part.copy())
                return
            
            if self.isPali(s, j, i):
                part.append(s[j : i + 1])
                dfs(i + 1, i + 1)
                part.pop()
            
            dfs(j, i + 1)
        
        dfs(0, 0)
        return res
        
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
        
'''
Time complexity : O(n x 2^n)
Space complexity : O(n x 2^n)
'''