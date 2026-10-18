def count_leaves(root):
    # Base case: empty tree
    if root is None:
        return 0

    # A leaf has no left or right child
    if root.left is None and root.right is None:
        return 1

    # count leaves in both subtrees
    return count_leaves(root.left) + count_leaves(root.right)
