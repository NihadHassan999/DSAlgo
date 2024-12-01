'''
Graph Valid Tree
Solved 
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output:
true
Example 2:

Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

Output:
false
Note:

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
'''

'''
-> BFS, tree should have all components with edges and no cycles
-> To validate if a given graph is a valid tree, we need two conditions:
   1. The graph should be connected, meaning all nodes are reachable from any starting point.
   2. The graph should not contain any cycles.
   3. The number of edges should be exactly n - 1, where n is the number of nodes.

-> Approach:
   - Use BFS to traverse the graph and keep track of visited nodes.
   - Ensure there are no cycles by checking if we revisit any node that is not the immediate parent.
   - After traversal, check if all nodes are visited to ensure the graph is connected.
'''

from collections import defaultdict, deque
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        q = deque([(0, -1)])  # (current node, parent node)
        visit.add(0)
        
        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, node))
        
        return len(visit) == n

'''
Time Complexity : O(V + E)
- Each node and edge is visited at most once during the BFS traversal.

Space Complexity : O(V + E)
- The adjacency list representation takes O(V + E) space.
- The queue can contain up to O(V) nodes in the worst case.
'''
