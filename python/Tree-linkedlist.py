class Node:
    def __init__(self):
        self.key = 0
        self.left = None
        self.right = None

def newNode(key):
    node = Node()
    node.key = key
    node.left = node.right = None
    return node

def flatten(root):
    if root is None or (root.left is None and root.right is None):
        return
    
    if root.left is not None:
        flatten(root.left)
        tmpRight = root.right
        root.right = root.left
        root.left = None

        t = root.right
        while t.right is not None:
            t = t.right

        t.right = tmpRight

    flatten(root.right)

def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    print(root.key, end=' ')
    inorder(root.right)

if __name__=='__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(5)
    root.left.left = newNode(3)
    root.left.right = newNode(4)
    root.right.right = newNode(6)

    flatten(root)

    print("The Inorder traversal after flattening binary tree ", end='')
    inorder(root)
