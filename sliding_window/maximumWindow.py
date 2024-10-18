'''
239. Sliding Window Maximum
Solved
Hard
Topics
Companies
Hint
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []  # Initialize the list to store the maximums of each sliding window
        q = deque()  # Deque to store the indices of elements in 'nums' for the sliding window
        l = r = 0    # Left and right pointers for the sliding window

        # Loop until the right pointer reaches the end of the nums list
        while r < len(nums):
            # Maintain the deque by removing indices of elements that are smaller than the current element
            while q and nums[q[-1]] < nums[r]:
                q.pop()  # Pop indices from the back of the deque

            q.append(r)  # Add the current index to the deque

            # If the left pointer has moved past the index of the maximum in the deque,
            # it means this index is no longer valid for the current window
            if l > q[0]:
                q.popleft()  # Remove the front index from the deque

            # Check if we have a complete window of size k
            if (r + 1) >= k:
                output.append(nums[q[0]])  # Append the maximum for the current window
                l += 1  # Move the left pointer to slide the window
            r += 1  # Move the right pointer to expand the window

        return output  # Return the list of maximums for each sliding window
    
'''
Time Complexity : O(n)
Space Complexity : O(n)
'''