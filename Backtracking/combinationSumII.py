'''
40. Combination Sum II
Solved
Medium
Topics
Companies
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''

'''
-> same approach of skipping duplicates by sorting and then comparing adjacent 
    elements to skip in while loop
-> create empty res and sort candidates
-> create dfs, success base case, i == len(candidates) return base case
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur[::])
                return
            if total > target or i == len(candidates):
                return
            # append
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            # pop
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res 

'''
Time Complexity : O(n * 2^n)
Space Complexity : O(n)
'''