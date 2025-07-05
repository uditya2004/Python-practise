class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Inorder traversal
def Inorder(root):
    if root != None:
        Inorder(root.left)
        print(root.data)
        Inorder(root.right)


# create a tree
root = Node(10)
root.left = Node(20)
root.right = Node(30)

root.left.left = Node(40)

Inorder(root)