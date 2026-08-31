"""
SAME AS LEVEL ORDER TRAVERSAL IN TREE (extra thing we do here is keep track of visited nodes, so we don't repeat nodes)

WAY OF PRINTING
- Print Root:
    - Then print all the Nodes connected to Root, then there connected nodes etc.

NOTE: Each node is printed only once
"""

from collections import deque

"""
- TC: O(V+E), where V is number of vertex and E is number of edges
              - In Outer while loop => each vertex enqued atmost once  => O(V)
              - In Inner for loop => runs degree(node) times, summed over all nodes => O(2E) = O(E)

- SC: O(V)
    - visited list => O(V), one boolean per node
    - queue        => O(V) worst case (star graph: all neighbours queued at once)
"""
class Solution:
    def bfs(self, start: int, adj: list[list[int]]) -> None:

        # "visited" list to keep track of which node we visited (means appended into queue), so we prevent repeating the same node twice.
        visited = [False]*(len(adj))   # initializing each node as not visited (False) initially i.e [False, False, False, False, False]
        
        q = deque()             # queue containing node values (which are represented as => index of "adj" list)
        q.append(start)         # intially pushed the "start" node to the queue 
        visited[start] = True   # marking the initial "start" node as Visited as it is enqueued into the queue

        """
        - Popleft from queue -> print it -> for each child check:
            - If child is not visited  => add it to the queue  and mark it as visited.
        """
        while q:   # TC: O(V)
            node = q.popleft()  # contains node value (index of "adj" list)
            print(node, end=" ")

            for child in adj[node]:
                if visited[child] == False:
                    q.append(child)
                    visited[child] = True


obj = Solution()
s = 0
"""
=> This is an adjacency list: a list of lists where the index is the node, and the inner list holds all neighbours of that node.

0 is connected to 1 and 2
1 is connected to 0, 2, 3
2 is connected to 0, 1, 3, 4
3 is connected to 1, 2, 4
4 is connected to 2 and 3

=> So len(adj) == 5 → the graph has 5 nodes labelled 0..4
"""
adj = [[1,2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4], [2, 3]]  # adjacency representation of graph
obj.bfs(s, adj)