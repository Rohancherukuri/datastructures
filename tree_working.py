from bst import BinarySearchTree

b = BinarySearchTree()
b_tree = b.Tree([10,4,5,21,13,17,1,2,-3])
print(b_tree)
print(len(b_tree))
print(b_tree.inorder())