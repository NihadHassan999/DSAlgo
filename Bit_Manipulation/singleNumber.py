'''
Single Number
Solved 
You are given a non-empty array of integers nums. Every integer appears twice except for one.

Return the integer that appears only once.

You must implement a solution with O(n)
O(n) runtime complexity and use only O(1)
O(1) extra space.

Example 1:

Input: nums = [3,2,3]

Output: 2
Example 2:

Input: nums = [7,6,6,7,8]

Output: 8
Constraints:

1 <= nums.length <= 10000
-10000 <= nums[i] <= 10000
'''

'''
-> using XOR to find out the number which occurs only once
-> same numbers cancel out each other since x XOR x = 0
'''
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num
        return res
'''
Time complexity : O(n) depends on the length of nums
Space complexity : O(1) no additional data structures are used
'''