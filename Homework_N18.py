# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# def print_leaf_nodes(node):
#     if node is None:
#         return
#     if node.left is None and node.right is None:
#         print(node.value, end=' ')
#     else:
#         print_leaf_nodes(node.left)
#         print_leaf_nodes(node.right)
#
#
# def count_nodes(node):
#     if node is None:
#         return 0
#     return 1 + count_nodes(node.left) + count_nodes(node.right)
#
#
# def count_edges(root):
#     total_nodes = count_nodes(root)
#     return total_nodes - 1 if total_nodes > 0 else 0
