'''
84. Largest Rectangle in Histogram
Hard
Topics
Companies
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''


'''
-> initialise maxArea and stack (index, height) pair
-> iterate index and height 
-> if stack is not empty and curr element h < stack top element h, 
    then pop element from stack
-> calculate max area of popped index and height and set new index
-> iterate through remaining indexes and heights in stack to find again maxArea
'''

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = []
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
            
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

'''
Time Complexity : O(n)
Space Complexity : O(n)
'''
