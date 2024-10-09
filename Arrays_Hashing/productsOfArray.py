'''
Products of Array Discluding Self
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O
(
n
)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20
'''

'''
1) create result
2) create separate loops for prefix and postfix
3) prefix enters first res value, then the present input value is multiplied with prefix
4) postfix enters last res value, then the present input value is multiplied with postfix
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix # multiply prefix to res index
            prefix *= nums[i] # update prefix with current num index

        postfix = 1
        for i in range(len(nums) - 1, -1,-1): # iterate in reverse order  
            res[i] *= postfix # multiply prefix to res index
            postfix *= nums[i] # update prefix with current num index

        return res

'''
Time Complexity : O(n) 
Space Complexity : O(1) -> no data structures are being used apart from 'res',
                           which is not considered as extra space as mentioned in the question
'''