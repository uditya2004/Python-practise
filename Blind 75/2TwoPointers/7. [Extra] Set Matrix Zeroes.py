# METHOD 1:- Brute force
# As at the worst case when all elements are zero k = m*n
# TC: O(m*n)
# SC: O(m*n)
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        col = len(matrix[0])

        # Phase 1:- Detect all the locations of zero's   . TC: O(m × n)
        zeros = []   # SC: O(K)
        for r in range(rows):
            for c in range(col):
                if matrix[r][c] == 0:
                    zeros.append([r,c])
        

        # Phase 2:- Modify
        # For each element in "zeros", make the rows and colmns of that coorinate zero    . TC: O(K*(m+n))
        for r,c in zeros:

            # make entire row as zero.  TC: O(n)
            for y in range(col):
                matrix[r][y] = 0
            
            # make entire column as zero.   TC: O(m)
            for x in range(rows):
                matrix[x][c] = 0
        

obj = Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
obj.setZeroes(matrix)

print(matrix)

#==================================================

# METHOD 2:- Better solution => USE OF SET to reduce space complexity
"""
- In previous solution, If there are 5 zeros in row 0, you store row 0 five times.
- With Sets => stores unique rows/cols
"""
# TC: O(m*n)
# SC: O(m+n)
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        col = len(matrix[0])

        # Phase 1:- Detect all the locations of zero's   . TC: O(m × n)
        zero_rows = set()   # SC: O(m)
        zero_cols = set()   # SC: O(n)
        for r in range(rows):
            for c in range(col):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)
        

        # Phase 2:- Modify.    TC: O(m*n)
        for r in range(rows):
            for c in range(col):
                if r in zero_rows or c in zero_cols:  # Lookup
                    matrix[r][c] = 0
        

obj = Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
obj.setZeroes(matrix)

print(matrix)

#==================================================

# METHOD 3:- use the first row and first column of the matrix as markers/flags.
"""
- Check if first row has any zero → store in first_row_zero

- Check if first column has any zero → store in first_col_zero

- Loop i from 1 to m-1, j from 1 to n-1:
    - If matrix[i][j] == 0 → set matrix[i][0] = 0 and matrix[0][j] = 0

- Loop i from 1 to m-1, j from 1 to n-1:
    - If matrix[i][0] == 0 OR matrix[0][j] == 0 → set matrix[i][j] = 0

- If first_col_zero → set entire column 0 to 0

- If first_row_zero → set entire row 0 to 0
"""
# TC: O(m*n)
# SC: O(1)
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        # Flags to note if 1st row or column contains a zero element or not.
        first_row_zero = False
        first_col_zero = False
        
        # 1. checking if 1st row contains zero  . TC: O(n)
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_zero = True

        # 2. checking if 1st col contains zero  . TC: O(m)
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_zero = True
        
        #3. Looping through inner matrix and marking zeroes in 1st row and column as MARKER   . TC: O(mn)
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # 4. Marking inner matrix elements as zeros based on MARKER    . TC: O(mn)
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # 5. Making 1st row as zero if first_row_zero = True   . TC: O(n)
        if first_row_zero == True:
            for c in range(cols):
                matrix[0][c] = 0

        # 6. Making 1st column as zero if first_col_zero = True  . . TC: O(m)
        if first_col_zero == True:
            for r in range(rows):
                matrix[r][0] = 0

obj = Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
obj.setZeroes(matrix)

print(matrix)
