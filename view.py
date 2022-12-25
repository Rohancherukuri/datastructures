# Printing  the left and right views of a Binary Search Tree
from bst import BinarySearchTree
from time import time

def left_view(root,levels):
    """This method returns the left view of the BinarySearchTree"""
    left_list = []
    if root is None:
        return "The Tree is empty!"
    else:
        for i in levels:
            left_list.append(i[0])
        return left_list

def right_view(root,levels):
    """This method returns the right view of the BinarySearchTree"""
    right_list = []
    if root is None:
        return "The Tree is empty!"
    
    else:
        for i in levels:
            right_list.append(i[len(i) - 1])
        return right_list


def main():
    """This is main method"""
    root = BinarySearchTree()
    lst = [10,5,3,7,6,9,4,1,21,17,24,15,19,22,27]
    for i in lst:
        root.insert(i)
    levels = root.levelorder(root)
    l = left_view(root,levels)
    r = right_view(root,levels)
    print("The left most view of BST is: "+str(l))
    print("The right most view of BST is: "+str(r))
    

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
