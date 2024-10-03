'''

Duplicate Integer
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

'''

# Create a hashset 
# direct iterate over nums
# if element not in hashset, return true

'''

cant use stack because stack is o(n) whereas set is o(1)
and also stack does index based iteration, whereas set does direct iteration

for i in range(len(nums)):
    n = nums[i]
    if n in hashset:
        return True
    hashset.add(n)

'''

class Solution():
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


''''

Time Complexity : O(n)
Space Complexity : O(n)

'''
