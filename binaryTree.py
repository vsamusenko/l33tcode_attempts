class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


def to_tuple(root):
    if isinstance(root, TreeNode):
        if root.left is None and root.right is None:
            tuplerep = root.key
        else:
            tuplemid = root.key
            tupleleft = to_tuple(root.left)
            tupleright = to_tuple(root.right)
            tuplerep = (tupleleft, tuplemid, tupleright)

    if root is None:
        tuplerep = None

    return tuplerep


def traverse_in_order(node):
    if node is None:
        return []
    return(traverse_in_order(node.left) +
           [node.key] +
           traverse_in_order(node.right))


def tree_height(node):
    print(node)
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


def min_Depth(node):
    print(node)
    if node is None:
        return 0
    return 1 + min(min_Depth(node.left), min_Depth(node.right))


def diameter(node):
    print(node)
    if node is None:
        return 0
    return 1 + min(min_Depth(node.left), min_Depth(node.right))





def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)




tree2 = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))

print(to_tuple(tree2))

print(traverse_in_order(tree2))

print(min_Depth(tree2))