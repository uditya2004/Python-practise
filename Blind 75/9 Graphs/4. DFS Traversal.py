
# TC: O(V+E), where V is number of vertex and E is number of edges
class Solution:
    def dfsRec(self, start: int, adj: list[list[int]], visited: list[bool])-> None:
        visited[start] = True
        print(start, end=" ")

        for u in adj[start]:
            if visited[u] == False:
                self.dfsRec(u, adj, visited)



    def dfs(self, adj: list[list[int]], start: int):
        visited = [False]*len(adj)
        self.dfsRec(start, adj, visited)


obj = Solution()
s = 0
adj = [[1,2], [0, 3, 4], [0, 3], [1, 2, 4], [1, 3]]  # adjacency representation of graph
obj.dfs(adj, s)