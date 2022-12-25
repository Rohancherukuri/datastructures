# Constructing a binary tree  in python
from time import time

class BinaryTree(object):
    """This is a BinaryTree class"""
    def __init__(self,root_value = None):
        """This is the constructor of the BinaryTree class"""
        self.root_value = root_value
        self.leftChild = None
        self.rightChild = None
    
    def insert(self,data):
        """This method inserts the elements into the BinaryTree"""
        if self.root_value is None:
            self.root_value = data
            return
        
        else:
            """The BinaryTree us under construction"""
            pass
            
        


def main():
    """This is main method"""
    tree = BinaryTree(10)
    print(tree.data)

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