'''
Subsets
Solved 
Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [7]

Output: [[],[7]]
Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''

'''
-> create res and subset list
-> create dfs function inside existing subsets function
-> base case : return solution if index exceeds len(nums)
-> add one : dfs, subtract one : dfs
-> now outside function, dfs(0)
-> return res
'''
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

'''
Time Complexity :   O(2^n)
Space Complexity : O(n * 2^n)
'''