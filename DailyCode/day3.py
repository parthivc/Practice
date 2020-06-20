# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

empty = '-1'


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deserializeHelper(s):
    if not s or s[0] == empty:
        return None
    root = Node(s.pop(0))
    root.left = deserializeHelper(s)
    root.right = deserializeHelper(s)
    return root


def deserialize(s):
    return deserializeHelper(s.split())


def serialize(root):
    if root is None:
        return empty
    node = root.val
    node += ' ' + serialize(root.left)
    node += ' ' + serialize(root.right)
    return node


# Preorder is used to copy the tree (which is being used here)
# Postorder is used to delete the tree
# Inorder is used to give tree nodes in a non-decreasing order


def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    # deepcode ignore AttributeLoadOnNone: Hardcoding initial value
    print(deserialize(serialize(node)).left.left.val == 'left.left')


if __name__ == "__main__":
    main()
