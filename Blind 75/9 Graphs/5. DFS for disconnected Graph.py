
"""
- TC: O(V+E)
      - wrapper for loop  => O(V), each check is O(1)
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

    def dfs(self, adj: list[list[int]]):
        visited = [False] * len(adj)

        for node in range(0, len(adj)):
            if visited[node] == False:
                self.dfsRec(node, adj, visited)

obj = Solution()
adj = [[1,2], [0,2], [0, 1], [4], [3]]  # adjacency representation of graph
obj.dfs(adj)