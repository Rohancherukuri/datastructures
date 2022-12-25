# Finding the lowest common ancestor between two nodes in BinarySearchTree
from bst import BinarySearchTree
from time import time

def lowestCommonAncestor(root,n1,n2):
    """This method finds the lowest common ancestor of given two nodes in the tree"""
    if root is None:
        return
    
    if root.root_value > n1 and root.root_value > n2:
        return lowestCommonAncestor(root.leftChild,n1,n2)
    
    if root.root_value < n1 and root.root_value < n2:
        return lowestCommonAncestor(root.rightChild,n1,n2)
    
    return root
    
def main():
    """This is main method"""
    tree = BinarySearchTree()
    t = tree.Tree([10,5,3,7,21,24,17])
    print("The BinarySearchTree is: "+t)
    node1 = eval(input("Enter node1 value: "))
    node2 = eval(input("Enter node2 value: "))
    ans = lowestCommonAncestor(tree,node1,node2)
    print("The lowest common ancestor of {} and {} is: {}".format(node1,node2,ans.root_value))
    key = eval(input("Enter the key element: "))
    print(tree.find(key))

if __name__ == "__main__":
    try:
        t1 = time()
        main()
        t2 = time()
    
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        t3 = t2 - t1
        print("[Finished in: "+str(round(t3,3))+" sec]")
