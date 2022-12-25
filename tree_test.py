# This is to find the kth largest and smallest elements in the Binary Search Tree
from bst import  BinarySearchTree
from time import time

def kthSmallest(k,lst):
    """This method computes the 'k' smallest element in BinarySearchTree"""
    if k <= 0:
        return "List index out of bounds"
    return lst[k-1]

def kthLargest(k,lst):
    """This method computes the 'k' largest element in BinarySearchTree"""
    if k <= 0:
        return "List index out of bounds"
    return lst[-k]

def main():
    """This is main method"""
    tree = BinarySearchTree()
    lt = [10,5,15,2,7,13]
    k = int(input("Enter the 'k' value: "))
    for i in lt:
        tree.insert(i)
    lst = tree.inorder()
    s = kthSmallest(k,lst)
    print("The 'k'th smallest element in a bst is:  "+str(s))
    l = kthLargest(k,lst)
    print("The 'k'th largest element in bst is: "+str(l))


if __name__ == "__main__":
    try:
        t1 = time()
        main()
    
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        t2 = time() - t1
        print("[Finished in: "+str(round(t2,3))+" sec]")       