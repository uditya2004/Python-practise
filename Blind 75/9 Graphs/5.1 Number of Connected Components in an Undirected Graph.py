"""
- This is Same as Count disconnected components using DFS/BFS, 
- But HERE EDGE LIST IS GIVEN , instead of adjacency list.
- So First Task is:- Convert edge list to adjacency list.
- Rest of the logic remains same
"""
class Solution:
    def dfs(self, start: int, adj: list[list[int]], visited: list[bool])->None:
        visited[start] = True

        for child in adj[start]:
            if visited[child] == False:
                self.dfs(child, adj, visited)

    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        
        # converting Edge list to Adj list first
        # 1. Initialize:- for each of the node, create empty list
        adj = [[] for i in range(0, n)]  

        # 2. Appending nodes to appropriate list
        for u,v in edges:
            adj[u].append(v)  # u is connected to v
            adj[v].append(u)  # v is also connected to u
        
        # now continue with normal count connected component logic
        visited = [False]*len(adj)
        count = 0

        for node in range(0, len(adj)):
            if visited[node] == False:
                count +=1
                self.dfs(node, adj, visited)
        return count


obj = Solution()
n = 5 
edges = [[0,1],[1,2],[3,4]]
print(obj.countComponents(n, edges))