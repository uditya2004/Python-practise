"""
SAME AS LEVEL ORDER TRAVERSAL IN TREE (extra thing we do here is keep track of visited nodes, so we don't repeat nodes)

WAY OF PRINTING
- Print Root:
    - Then print all the Nodes connected to Root, then there connected nodes etc.

NOTE: Each node is printed only once
"""

from collections import deque

class Solution:
    def bfs(self, start: int, adj: list[list[int]], visited: list[bool]) -> None:
        
        # initialize queue by adding start element to queue and mark it as visited
        q = deque()
        q.append(start)
        visited[start] = True

        while q:
            node = q.popleft()

            for u in adj[node]:
                if visited[u] == False:
                    q.append(u)
                    visited[u] = True
    
    
    def countConnectedComp(self, adj: list[list[int]])-> int:
        visited = [False] * len(adj)
        
        """
        - We traverse each index of "adj" list (i.e node value)
        - For each node:
            - we check => if it's not visited, then => we call BFS with "start" node as this node
        
        - We share the same "visited" list for each BFS function call.
        - On each BFS function call:
            - It marks the elements visited in each call
        """

        count = 0
        for node in range(len(adj)):    
            if visited[node] == False:
                count +=1
                self.bfs(node, adj, visited)
        return count

obj = Solution()
adj = [[1,2], [0,3], [0,3], [1,2], [5,6], [4,6], [4,5]]  # adjacency representation of graph
print(obj.countConnectedComp(adj))