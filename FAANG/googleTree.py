# https://www.youtube.com/watch?v=-tNMxwWSN_M

class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



#          1
#        /  \
#       2    3
#      / \  / \
#     4  5 6  7
#    / \
#   8  9


# Task 1: Return the sum of the node depths of the tree
# A node depth is it's distance from the root node

def nodeDepthSum(root):
    nodeDepthSum.answer = 0
    def dfsHelper(root, depth):
        nodeDepthSum.answer += depth
        if root.right:
            dfsHelper(root.right, depth + 1)
        if root.left:
            dfsHelper(root.left, depth + 1)
    dfsHelper(root, 0)
    return nodeDepthSum.answer

# Task 2: Return the sum of the node depths for all of the subtrees in the tree

def subTreeNodeDepthSum(root):
    def dfsHelper(root):
        result = [1, 0]  # Number of nodes, sum of depths
        if root.right:
            rResult = dfsHelper(root.right)
            result[0] += rResult[0]
            result[1] += rResult[0] + rResult[1]
        if root.left:
            lResult = dfsHelper(root.left)
            result[0] += lResult[0]
            result[1] += lResult[0] + lResult[1]
        return result
    return dfsHelper(root)[1]


def main():
    # This tree represents the above tree for reference and testing
    example = Node(1, Node(2, Node(4, Node(8), Node(9)), Node(5)), Node(3, Node(6), Node(7)))
    print("\nSum of node depths: {}\n".format(nodeDepthSum(example)))


if __name__ == "__main__":
    main()