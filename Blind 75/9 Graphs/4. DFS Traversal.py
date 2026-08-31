"""
- TC: O(V+E)
      - dfsRec body       => runs at most once per node        => O(V)
      - inner for loop    => degree(node) per call,
                             summed over all nodes = 2E        => O(E)

- SC: O(V)
        - visited list      => O(V), one boolean per node
        - recursion stack   => O(V) worst case (chain graph 0-1-2-...-V)

"""
class Solution:
    def dfsRec(self, start: int, adj: list[list[int]], visited: list[bool])-> None:
        visited[start] = True
        print(start, end=" ")

        for child in adj[start]:
            if visited[child] == False:
                self.dfsRec(child, adj, visited)


    def dfs(self, adj: list[list[int]], start: int):
        visited = [False]*len(adj)
        self.dfsRec(start, adj, visited)


obj = Solution()
s = 0
adj = [[1,2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4], [2, 3]]  # adjacency representation of graph
obj.dfs(adj, s)