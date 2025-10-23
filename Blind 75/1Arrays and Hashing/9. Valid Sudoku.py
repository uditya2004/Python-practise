import collections

"""
Concept:-
- Let:
    - rows -> contain all elements in the current element's row
    - cols -> contain all elements in the current element's column
    - squares -> contain all the elements in the 3x3 square where current element belong.

- Every element in the board has the index is like [row][column]

    - For check if the element is in row -> we use rows[row] 
    - For check if the element is in row -> we use cols[col]
    - For check if the element is in square -> we use square[(row//3, col//3)]

- For every element we check following to ensure sudoku is valid:
    - Element is not a duplicate in its row
    - Element is not a duplicate in its column
    - Element is not a duplicate in its 3x3 square
"""

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = collections.defaultdict(set)     # key: column_number, value: set of all values in that column
        rows = collections.defaultdict(set)     # key: row_number, value: set of all values in that row
        squares = collections.defaultdict(set)  # key = (r//3, c//3) , value: all elements in that square

        #Iterating over the entire 9x9 board
        for r in range(9):      # as board has 9 rows
            for c in range(9):  # as board has 9 columns

                #if the current element is "." , do nothing , move to next element in the board
                if board[r][c] == ".":
                    continue
                
                # Checking if current element is duplicate
                # If it is a duplicate then the sudoku board is invalid
                if (board[r][c] in rows[r] or   # For rows, if the current element is already present in its row, then current element is a duplicate
                    board[r][c] in cols[c] or   # For column, if the current element is already present in its column, then current element is a duplicate
                    board[r][c] in squares[(r//3, c//3)]):   # For 3x3 square, if the current element is already present in its square, then current element is a duplicate
                    
                    return False
                
                # If current element is not a duplicate, we add current element in all 3 hash maps
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        
        # While iterating the board, if we never detected a duplicate, then the board is value, thus return True
        return True





board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
obj = Solution()
print(obj.isValidSudoku(board))