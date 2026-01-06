

class Solution:
    def dfsRec(self, start: int, adj: list[list[int]], visited: list[bool])-> None:
        visited[start] = True
        print(start, end=" ")

        for u in adj[start]:
            if visited[u] == False:
                self.dfsRec(u, adj, visited)

    def dfs(self, adj: list[list[int]]):
        visited = [False] * len(adj)

        for node in range(0, len(adj)):
            if visited[node] == False:
                self.dfsRec(node, adj, visited)

obj = Solution()
adj = [[1,2], [0,2], [0, 1], [4], [3]]  # adjacency representation of graph
obj.dfs(adj)