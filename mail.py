class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def get_max_value(tree: TreeNode):
    if tree is None:
        return None

    current = tree

    while current.right is not None:
        current = current.right

    return current.value


def get_min_value(tree: TreeNode):
    if tree is None:
        return None

    current = tree
    while current.left is not None:
        current = current.left

    return current.value


def get_sum_of_all_values(tree: TreeNode) -> int:
    if tree is None:
        return 0

    return sum([tree.value, get_sum_of_all_values(tree.left), get_sum_of_all_values(tree.right)])


treeNode = TreeNode(9)
treeNode.left = TreeNode(1)
treeNode.right = TreeNode(70)
treeNode.right.left = TreeNode(30)
treeNode.right.right = TreeNode(100)
treeNode.right.right.left = TreeNode(99)

print(f"Max value: {get_max_value(treeNode)}")
print(f"Min value: {get_min_value(treeNode)}")
print(f"Sum : {get_sum_of_all_values(treeNode)}")
