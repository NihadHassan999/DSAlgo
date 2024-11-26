'''
-> Same approach as Course Schedule I, except that this time we return the course list compared to just bool
'''

from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)  # Dictionary to store adjacency list
        indegree = [0] * numCourses  # Array to track prerequisites count

        # Build graph and indegree array
        for b, a in prerequisites:  # b -> a
            graph[b].append(a)
            indegree[a] += 1

        # Initialize queue with courses having no prerequisites
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        finish, output = 0, []

        # Process courses using BFS (Kahn's Algorithm)
        while q:
            node = q.popleft()
            output.append(node)
            finish += 1

            # Reduce indegree for neighbors and add them to queue if they have no prerequisites
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        # If not all courses are processed, return an empty list (cycle detected)
        if finish != numCourses:
            return []

        return output[::-1]  # Return the reversed topological order

'''
Time complexity : O(V+E)
Space complexity : O(V+E) 
'''