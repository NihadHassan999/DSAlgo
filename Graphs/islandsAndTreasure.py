'''
Islands and Treasure
Solved 
You are given a 
m
×
n
m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
Example 2:

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}
'''

'''
-> use bfs with set and queue to keep visited count and process elements 
-> set rows, cols, set and queue
-> def addCell, use this to eliminate OOB, visited and walls out
-> after edge case elimination, add to set and queue
-> iterate through all elements and add to visited and append
-> do the bfs by popping from the queue, assigning dist and going in 4 directions
'''

from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()

        # checking OOB conditions
        def addCell(r, c):
            if (min(r, c) < 0 or c == COLS or r == ROWS or grid[r][c] == -1 or (r, c) in visit):
                return 
            visit.add((r, c))
            q.append([r, c])

        
        # iterate and get all gates appended to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append([r, c])
        
        # initialise dist and assign to neighbours
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1

'''
Time Complexity : O(m * n)
Space Complexity : O(m * n)
'''