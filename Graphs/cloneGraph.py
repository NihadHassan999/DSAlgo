'''
Clone Graph
Solved 
Given a node in a connected undirected graph, return a deep copy of the graph.

Each node in the graph contains an integer value and a list of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed).

The input node will always be the first node in the graph and have 1 as the value.

Example 1:

Input: adjList = [[2],[1,3],[2]]

Output: [[2],[1,3],[2]]
Explanation: There are 3 nodes in the graph.
Node 1: val = 1 and neighbors = [2].
Node 2: val = 2 and neighbors = [1, 3].
Node 3: val = 3 and neighbors = [2].

Example 2:

Input: adjList = [[]]

Output: [[]]
Explanation: The graph has one node with no neighbors.

Example 3:

Input: adjList = []

Output: []
Explanation: The graph is empty.

Constraints:

0 <= The number of nodes in the graph <= 100.
1 <= Node.val <= 100
There are no duplicate edges and no self-loops in the graph.
'''

'''
-> cover edge case if input is empty
-> Create hashmap to store cloned adjacent list graph
-> first clone current node and recursively clone neighbours
'''


# # Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # Hash map to store cloned nodes
        cloned_nodes = {}

        # Recursive DFS function
        def dfs(curr_node):
            # If already cloned, return the clone
            if curr_node in cloned_nodes:
                return cloned_nodes[curr_node]

            # Clone the node
            clone = Node(curr_node.val)
            cloned_nodes[curr_node] = clone

            # Recursively clone all neighbors
            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)


'''
Time compplexity : O(V + E)
Space complexity : O(V)
'''
















        