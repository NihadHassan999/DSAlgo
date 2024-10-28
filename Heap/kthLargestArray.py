'''
Kth Largest Element in an Array
Solved 
Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.

By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

Follow-up: Can you solve it without sorting?

Example 1:

Input: nums = [2,3,1,5,4], k = 2

Output: 4
Example 2:

Input: nums = [2,3,1,1,5,5,4], k = 3

Output: 4
Constraints:

1 <= k <= nums.length <= 10000
-1000 <= nums[i] <= 1000
'''

'''
-> Quick Select
-> k becomes len(nums) - k so that kth largest no becomes kth smallest index
-> using binary search, start with while loop l and r pointers and get pivot
-> define paritition function using quickselect
'''

# # Quick Select
# # Time complexity: O(n) in average, O(n^2) in worst case
# class Solution:

#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         k = len(nums) - k
#         left, right = 0, len(nums) - 1

#         while left < right:
#             pivot = self.partition(nums, left, right)

#             if pivot < k:
#                 left = pivot + 1
#             elif pivot > k:
#                 right = pivot - 1
#             else:
#                 break

#         return nums[k]

#     def partition(self, nums: List[int], left: int, right: int) -> int:
#         pivot, fill = nums[right], left

#         for i in range(left, right):
#             if nums[i] <= pivot:
#                 nums[fill], nums[i] = nums[i], nums[fill]
#                 fill += 1

#         nums[fill], nums[right] = nums[right], nums[fill]

#         return fill

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

'''
Time complexity : O(n) , worse cast scenario O(n^2)
Space complexity : O(1)
'''








