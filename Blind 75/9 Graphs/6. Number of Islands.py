
# TC: O(M*N), where m = rows and n = columns in a grid
# SC: O(M*N), in worst case all cells are 1's for recursive call stack of size M*N
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
    
        row = len(grid)
        column = len(grid[0])
        island = 0

        # In this DFS we are converting the (r,c) land to water and also all the land connected to (r,c) into water => "SINKING THE ISLAND"
        def dfs(r, c):

            # Base case: out of bounds OR found water/"0"
            if r < 0 or r >= row or c < 0 or c >= column or grid[r][c] == "0":
                return
            
            """
            - If reacher here means:- (r,c) is in bound and grid[r][c] == "1" means it's a land. So we do:-
                - Mark as visited by changing 1 to 0 of element grid[r][c]
            """
            grid[r][c] = "0"

            # Explore all 4 directions for land
            dfs(r-1, c)  #up
            dfs(r+1, c)  #down
            dfs(r, c-1)  #left
            dfs(r, c+1)  #right

        # for each [i][j] we check if it's "1", that means we got new island  => then perform dfs/bfs to find adjacent "1" ' s
        for i in range(row):
            for j in range(column):

                if grid[i][j] == "1":
                    island +=1   # new island found
                    dfs(i, j)    # dfs to find adjacent lands (1's) => (i,j) indicates the start node of dfs



obj = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(obj.numIslands(grid))
