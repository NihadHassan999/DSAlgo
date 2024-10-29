'''
Task Scheduling
Solved 
You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

Return the minimum number of CPU cycles required to complete all tasks.

Example 1:

Input: tasks = ["X","X","Y","Y"], n = 2

Output: 5
Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

Example 2:

Input: tasks = ["A","A","A","B","C"], n = 3

Output: 9
Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.

Constraints:

1 <= tasks.length <= 1000
0 <= n <= 100
'''

'''
-> Frequency Counting
-> maxHeap to track frequent tasks
-> time and queue simulation
-> execution loop
-> edge case for empty heap
'''
import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

        
'''
Time complexity : O(TlogT)
Space complexity : O(T)
'''