def preorderTraversal(self, node):
    if node is not None:
        print(node.data, end=' ')
        self.preorderTraversal(node.left)
        self.preorderTraversal(node.right)
        print("Preorder traversal:", end=' ')
        bst.preorderTraversal(bst.root)
print()