'''
Longest Consecutive Sequence
Solved 
Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
'''

# create hashset and initialiase result(longest)
# iterate, if left neighbour not present, it starts a new sequence = 1
# if next neighbour (current + length) is present, increment legnth
# finall find longest by max and return it 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
            
'''
Time Complexity : O(n)
Space Complexity : O(n)
'''

# Example Usage
solution = Solution()
nums = [100, 4, 200, 1, 3, 2]
result = solution.longestConsecutive(nums)
print(f"The longest consecutive sequence length is: {result}")