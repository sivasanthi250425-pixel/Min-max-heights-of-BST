class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)

    return root


def minimum(root):
    while root.left:
        root = root.left
    return root.data


def maximum(root):
    while root.right:
        root = root.right
    return root.data


def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left),
                   height(root.right))


root = None
keys = list(map(int, input("Enter keys: ").split()))

for key in keys:
    root = insert(root, key)

if root:
    print("Minimum:", minimum(root))
    print("Maximum:", maximum(root))
    print("Height:", height(root))
else:
    print("Tree is empty")