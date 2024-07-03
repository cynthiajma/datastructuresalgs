from typing import Optional


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

    def insert(self, node: Optional['TreeNode'], key: int) -> Optional["TreeNode"]:
        # Tree is empty
        if node is None:
            return TreeNode(key)
        # Tree is not empty:
        if key < node.val:
            node.left = self.insert(node.left, key)
        elif key > node.val:
            node.right = self.insert(node.right, key)
        return node # return the unchanged node pointer


    def search_in_bst(self, root: Optional['TreeNode'], search_value: int) -> Optional["TreeNode"]:
        # insert the node as the root if no root exists, or if the node ALREADY exists.
        if root is None or root.val == search_value:
            return root
        if root.val < search_value:
            return self.search_in_bst(root.right, search_value)
        else:
            return self.search_in_bst(root.left, search_value)


    def inorder_traversal(self, root: Optional['TreeNode']) -> None:
        if root.left:
            self.inorder_traversal(root.left)
        if root is not None:
            print(root.val)
        if root.right:
            self.inorder_traversal(root.right)


    def invert(self, node: Optional['TreeNode']) -> None:
        # recursive traversal, and swap the right and left subtrees for each node.
        if not node:
            return
        else:
            node.left, node.right = node.right, node.left
            self.invert(node.left)
            self.invert(node.right)


if __name__ == '__main__':
    root = None
    tree = TreeNode()
    root = tree.insert(root, 50)
    tree.insert(root, 30)
    tree.insert(root, 20)
    tree.insert(root, 40)
    tree.insert(root, 70)
    tree.insert(root, 60)
    tree.insert(root, 80)

    key = 2
    # if tree.search_in_bst(root, key) is None:
    #     print("key", key, "not found\nPrinting list...")
    #     tree.inorder_traversal(root)
    # else:
    #     print("key found", key)

    # test inversion
    print("original:")
    tree.inorder_traversal(root)
    tree.invert(root)
    print("inverted:")
    print(tree.inorder_traversal(root))











