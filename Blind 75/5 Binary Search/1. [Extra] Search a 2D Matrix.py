
# Method 1 Better solution
"""
Let:-
    n -> rows
    m -> columns

1. First perform binary search to determine which row may contain target element
2. Once the rows is found, perform binary search in that row to find the target element
"""
# TC: O(logn + logm)
def searchMatrix(matrix, target: int) -> bool:
    low = 0
    high = len(matrix) - 1

    # Performing binary search to determn row.
    while low <= high :
        mid = (low + high) // 2
        
        left  = 0
        right = len(matrix[mid]) - 1

        if target == matrix[mid][left] or target == matrix[mid][right]:
            return True
        
        elif target > matrix[mid][left] and target < matrix[mid][right]:
            # target present in this array (do binary search here)
            while left <= right:
                innerMid = (left + right) // 2

                if matrix[mid][innerMid]  == target:
                    return True
                
                elif target < matrix[mid][innerMid]:
                    right = innerMid - 1

                else:
                    left = innerMid + 1
            return False


        elif target < matrix[mid][left]:
            #present in previous array
            high = mid - 1

        else:
            #present in next array
            low = mid + 1
    
    return False

matrix = [
        [1,3,5,7],
        [10,11,16,20],
        [23,30,34,60]
    ]
target = 23

print(searchMatrix(matrix, target))


#======================================
# Method 2 Best solution

# TC: O(log(m x n))
# SC: O(1)

"""
1. Imagine 2D array as 1D array and simply perform binary search on this 1D array which take logn time complexity
    - To find the mid element coordinate, we devise a formula which can give us the 2D coordinate from a 1D index
        - Row of mid elemnent -> mid // column
        - Column of mid element -> mid % Column
"""
def searchMatrix(matrix, target: int) -> bool:
    Row = len(matrix)
    Column = len(matrix[0])
    
    low = 0
    """
    - if we flatten the matrix, there will be m x n elements in the 1D array.
    - So the last element index in this new 1D array will be m*n - 1
    """
    high = (Row * Column) - 1      

    while low <= high:
        mid = (low + high) // 2    # mid index of flattened 2D array
        
        # Convert mid to 2D:
        # calculating the 2D coordinate of the mid element in 2D array like (Row, Column)
        midRow = mid // Column
        midColumn = mid % Column

        mid_value_2D = matrix[midRow][midColumn]

        # now apply typical binary search logic
        if mid_value_2D == target:
            return True
        
        elif mid_value_2D < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False

matrix = [
        [1,3,5,7],
        [10,11,16,20],
        [23,30,34,60]
    ]
target = 22

print(searchMatrix(matrix, target))