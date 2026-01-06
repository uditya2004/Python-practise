
# TC: O(M*N) -> operation done for each cell
# SC: O(M*N) -> recursive stack can be m*n as we are check for each cell in the grid

# Where m is the number of rows and n is the number of columns in the grid.
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        
        row = len(grid)
        column = len(grid[0])
        result = 0

        def dfs(r,c):
            if r < 0 or r >= row or c < 0 or c >= column or grid[r][c] == 0:
                return 0

            # mean we are in range and grid[r][c] = 1, so make count = 1 for this cell
            grid[r][c] = 0
            count = 1

            # explore all 4 direction and update the total land count
            count += dfs(r-1, c)      # Each dfs call eturns the total count of connected land cells from that direction 
            count += dfs(r+1, c)    
            count += dfs(r, c-1)    
            count += dfs(r, c+1)

            return count
                

        for r in range(row):
            for c in range(column):
                
                if grid[r][c] == 1:
                    result = max(result, dfs(r, c))
        return result


obj = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(obj.maxAreaOfIsland(grid))