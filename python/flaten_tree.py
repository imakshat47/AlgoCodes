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
    while root != None:
        if root.left != None:
            curr = root.left
            while curr.right != None:
                curr = curr.right
            curr.right = root.right
            root.right = root.left
            root.left = None
        root = root.right

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.key, end=' ')
    inorder(root.right)

if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(5)
    root.left.left = newNode(3)
    root.left.right = newNode(4)
    root.right.right = newNode(6)

    flatten(root)

    print("The Inorder traversal after flattening binary tree ", end='')
    inorder(root)
