"""
ALGO
- Traverse each node in the adjacency list.
- For every node, check whether it is visited.
- If the node is not visited:
    - Start BFS/DFS from that node.
    - Increase the connected component count by 1.
- BFS/DFS visits and marks all nodes visited = True , from the starting node.
- Nodes still unvisited after that belong to another disconnected component.

NOTE:- We share the same "visited" list for each BFS function call. So it remain persistent across the BFS function calls
"""

"""
- TC: O(V+E)
- SC: O(V)
      - visited list      => O(V), one boolean per node
      - queue             => O(V) worst case (star graph: all neighbours queued at once)
      - count             => O(1)
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

        count = 0
        for node in range(len(adj)):    
            if visited[node] == False:
                count +=1
                self.bfs(node, adj, visited)
        return count

obj = Solution()
adj = [[1,2], [0,3], [0,3], [1,2], [5,6], [4,6], [4,5]]  # adjacency representation of graph
print(obj.countConnectedComp(adj))