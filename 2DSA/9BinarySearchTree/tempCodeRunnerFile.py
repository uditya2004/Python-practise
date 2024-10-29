def Insert(root, key):
    if root is None:
        return Node(key)
    elif root.data == key:
        return root
    elif root.data > key:
        root.left = Insert(root.left, key)
    else:
        root.right = Insert(root.right, key)
    return root

def getHeight(root):
    if root is None:
        return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))

def printTree(root):
    def fillMatrix(matrix, node, row, col, width):
        if not node:
            return

        matrix[row][col] = str(node.data)
        
        if node.left:
            matrix[row+1][col-width//4] = '/'
            fillMatrix(matrix, node.left, row+2, col-width//2, width//2)
        
        if node.right:
            matrix[row+1][col+width//4] = '\\'
            fillMatrix(matrix, node.right, row+2, col+width//2, width//2)

    height = getHeight(root) * 2 - 1
    width = 2 ** getHeight(root) * 2 - 1
    matrix = [[' ' for _ in range(width)] for _ in range(height)]

    fillMatrix(matrix, root, 0, width // 2, width)

    # Remove trailing spaces from each row
    for i, row in enumerate(matrix):
        last_non_space = max(idx for idx, char in enumerate(row) if char != ' ')
        matrix[i] = row[:last_non_space + 1]

    # Print the matrix
    for row in matrix:
        print(''.join(row))