"""
BFS ON A DISCONNECTED GRAPH

CONNECTED     => every node reachable from any single start node
DISCONNECTED  => graph splits into separate "islands" (connected components)
                 no edge crosses between components

PROBLEM: plain BFS from start=0 only covers 0's component.
         The queue only receives NEIGHBOURS of discovered nodes,
         so it can never "jump" to another island. Nodes 4,5,6 stay unvisited.

FIX (2 changes vs normal BFS):
  1. Move "visited" OUT of bfs() -> pass it in, so state persists across calls.
  2. Outer loop over every node: if not visited -> start a fresh BFS there.

=> Each bfs() call covers exactly ONE component.
=> Number of bfs() calls = number of connected components.

TC: O(V + E)  |  SC: O(V)   (outer loop is O(V), visited check is O(1),
                             no node is ever enqueued twice)
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
            print(node, end=" ")

            for u in adj[node]:
                if visited[u] == False:
                    q.append(u)
                    visited[u] = True
    
    
    def bfsDisconnected(self, adj: list[list[int]])-> None:
        """
        ALGO
        - We traverse each index of "adj" list (i.e node value)
        - For each node:
            - we check => if it's not visited, then => we call BFS with "start" node as this node
        
        - We share the same "visited" list for each BFS function call.
        - On each BFS function call:
            - It marks the elements visited in each call
        """
        
        visited = [False] * len(adj)
        
        # loop tries every node as a potential start
        for node in range(len(adj)):    
            if visited[node] == False:
                self.bfs(node, adj, visited)

obj = Solution()
adj = [[1,2], [0,3], [0,3], [1,2], [5,6], [4,6], [4,5]]  # adjacency representation of graph
obj.bfsDisconnected(adj)

"""
STRUCTURE

Node	Neighbours	Component
0	       1, 2	      A
1	       0, 3	      A
2	       0, 3	      A
3	       1, 2	      A

4	       5, 6	      B
5	       4, 6	      B
6	       4, 5	      B

"""

"""
DRY RUN (adj at bottom, 2 components)

  node=0  not visited -> bfs(0) prints "0 1 2 3"   visited=[T,T,T,T,F,F,F]
  
  node=1,2,3          -> already True, skipped
  
  node=4  not visited -> bfs(4) prints "4 5 6"     visited=[T,T,T,T,T,T,T]
  
  node=5,6            -> already True, skipped
  
OUTPUT: 0 1 2 3 4 5 6
"""