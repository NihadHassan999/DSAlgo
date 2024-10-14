'''
You are given an integer array heights where heights[i] represents the height of the 
i
t
h
i 
th
  bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:

Input: height = [1,7,2,5,4,7,3,6]

Output: 36
Example 2:

Input: height = [2,2,2]

Output: 4
Constraints:

2 <= height.length <= 1000
0 <= height[i] <= 1000
'''

'''
-> use two pointers at ends of list to get max area
-> compute max area
-> if height of left or right pointer lower, increment or decrement accordingly
'''

class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res
    
'''
Time complexity : O(n) (nested loop brute force would have taken o(n2))
Space complexity : O(1) (two pointers taking no space, and res variable doesnt count)
'''