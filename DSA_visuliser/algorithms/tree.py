from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree_level_order(values):
    if not values or values[0] == "None":
        return None

    root = Node(int(values[0]))
    q = deque([root])
    i = 1
    n = len(values)

    while q and i < n:
        node = q.popleft()

        # Left child
        if i < n and values[i] != "None":
            node.left = Node(int(values[i]))
            q.append(node.left)
        i += 1

        # Right child
        if i < n and i < n and values[i] != "None":
            node.right = Node(int(values[i]))
            q.append(node.right)
        i += 1

    return root

def bfs(root):
    res=[]
    if not root: return res
    q = deque([root])
    while q:
        n = q.popleft()
        res.append(n.val)
        if n.left: q.append(n.left)
        if n.right: q.append(n.right)
    return res

def inorder(root, res):
    if not root: return
    inorder(root.left, res)
    res.append(root.val)
    inorder(root.right, res)

def preorder(root, res):
    if not root: return
    res.append(root.val)
    preorder(root.left, res)
    preorder(root.right, res)

def postorder(root, res):
    if not root: return
    postorder(root.left, res)
    postorder(root.right, res)
    res.append(root.val)
