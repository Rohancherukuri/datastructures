# Implementing Binary Search Tree in python
from time import time

class BinarySearchTree(object):
    """ 
        Ex:-
            10
           /  \
          /    \
         5      21
        / \    /  \
       3  7   17  24
    """ 
    """This is Binary Search Tree class"""
    def __init__(self,root_value = None):
        """This is a constructor of BinarySearchTree class"""
        self.leftChild = None
        self.root_value = root_value
        self.rightChild = None
    
    
    def Tree(self,l):
        """This method takes a list of inputs and converts into a BinarySearchTree"""
        for i in l:
            self.insert(i)
        
        return self
    
    
    def insert(self,data):
        """
            This method inserts the elements onto the nodes 
            if exists else creates the nodes and inserts the 
            elements into BinarySearchTree
        """
        if self.root_value is None:
            self.root_value = data
            return 
        # Handling duplicate values
        if self.root_value == data:
            return 
        if self.root_value > data:
            if self.leftChild:
                self.leftChild.insert(data)
            
            else:
                self.leftChild = BinarySearchTree(data)
        
        if self.root_value < data:
            if self.rightChild:
                self.rightChild.insert(data)
            
            else:
                self.rightChild = BinarySearchTree(data)
                
    
    def delete(self,data):
        """This method deletes the given node in BinarySearchTree"""
        if self.root_value is None:
            print("The Tree is empty!")
            return 
        
        if self.root_value > data:
            if self.leftChild:
                self.leftChild = self.leftChild.delete(data)
            
            else:
                print("The given node is not present in the Tree!")
        
        elif self.root_value < data:
            if self.rightChild:
                self.rightChild = self.rightChild.delete(data)
            
            else:
                print("The given node is not present in the Tree!")
        
        else:
            if self.leftChild is None:
                temp = self.rightChild
                self = None
                return temp
            
            if self.rightChild is None:
                temp = self.leftChild
                self = None
                return temp
            
            node = self.rightChild
            while node.leftChild:
                node = node.leftChild
            
            self.root_value = node.root_value
            self.rightChild = self.rightChild.delete(node.root_value)
            
        return self
    
    
    def search(self,key):
        """This method searches for the given key in BinarySearchTree"""
        
        if self.root_value == key:
            print("The key {} is present in the binary search tree!".format(key))
            return 
        
        if key < self.root_value:
            if self.leftChild:
                self.leftChild.search(key)
                
            else:
                print("The key {} is not present in the binary search tree!".format(key))
        
        else:
            if self.rightChild:
                self.rightChild.search(key)
            
            else:
                print("The key {} is not present in the binary search tree!".format(key))
    
    
    def find(self,key):
        """This method returns boolean values if the found key present in the BinarySearchTree"""
        lst = self.inorder()
        if key in lst:
            return True
        
        else:
            return False
        
        
    def preorder(self):
        """This method prints the BinarySearchTree elements in preorder fashion"""
        # root->leftsubtree->rightsubtree
        left_list,right_list = [],[]
        if self is None:
            return
        
        else:
            val = [self.root_value]
            if self.leftChild:
                left_list = self.leftChild.preorder()
            
            if self.rightChild:
                right_list = self.rightChild.preorder()
                
        result = val + left_list + right_list
        #return "Tree({},type = <class 'bst.binarySearchTree'>)".format(result)
        return result
    
    def inorder(self):
        """This method prints the BinarySearchTree elements in inorder fashion"""
        # leftsubtree->root->rightsubtree
        left_list,right_list = [],[]
        if self is None:
            return
        
        else:
            if self.leftChild:
                left_list = self.leftChild.inorder()
            
            val = [self.root_value]
            
            if self.rightChild:
                right_list = self.rightChild.inorder()
        result = left_list + val + right_list
        #return "Tree({},type = <class 'bst.BinarySearchTree'>)".format(result)
        return result
       
    def postorder(self):
        """This method prints the BinarySearchTree elements in postorder fashion"""
        # leftsubtree->rightsubtree->root
        left_list,right_list = [],[]
        if self is None:
            return
        
        else:
            if self.leftChild:
                left_list = self.leftChild.postorder()
                
            
            if self.rightChild:
                right_list = self.rightChild.postorder()
            
            val = [self.root_value]
        
        result = left_list + right_list + val
        #return "Tree({},type = <class 'bst.BinarySearchTree'>)".format(result)
        return result
        
    
    
    def levelorder(self):
        """This method prints the BinarySearchTree elements in levelorder fashion"""
        root = self
        if root is None:
            return []
        queue = [root]
        next_queue = []
        level = []
        result = []
        while queue != []:
            for root in queue:
                level.append(root.root_value)
                if root.leftChild is not None:
                    next_queue.append(root.leftChild)
                
                if root.rightChild is not None:
                    next_queue.append(root.rightChild)
            
            result.append(level)
            level = []
            queue = next_queue
            next_queue = []
        # We return the list of lists of elements arranged by level 
        return result
            
    
    
    def minimum(self):
        """This method finds the minimum element in a BinarySearchTree"""
        curr_node = self
        while curr_node.leftChild:
            curr_node = curr_node.leftChild
        
        print("The minimum node element is: "+str(curr_node.root_value))
    
    def maximum(self):
        """This method finds the maximum element in a BinarySearchTree"""
        curr_node = self
        while curr_node.rightChild:
            curr_node = curr_node.rightChild
        
        print("The maximum node element is: "+str(curr_node.root_value))
    
    def peek(self):
        """This method returns the root element of a BinarySearchTree"""
        print("The root element in the binary search tree is: "+str(self.root_value))
    
    
    def size(self):
        """This method computes the size of a BinarySearchTree"""
        total = 1
        if self.root_value is None:
            return 0
        
        if self.leftChild:
            total += self.leftChild.size()
        
        if self.rightChild:
            total += self.rightChild.size()
        
        return total
    
    def height(self):
        """This method calculates the height of BinarySearchTree"""
        if self.root_value is None:
            return 0
        else:
            h = self.levelorder()
            return len(h) - 1
    
    def balance(self,sorted_list):
        """This method balances the BinarySearchTree"""
        if not sorted_list and self.root_value is None:
            return None
        
        else:
            newNode = self
            start = sorted_list[0]
            end = sorted_list[len(sorted_list) -1]
            mid = start + (end - start) // 2
            newNode = BinarySearchTree(sorted_list[mid])
            newNode.leftChild = BinarySearchTree(sorted_list[:(mid - 1)])
            newNode.rightChild = BinarySearchTree(sorted_list[(mid + 1):])
            return newNode
    
    
    
    def lca(self,n1,n2):
        """This method finds the lowest common ancestor of given two nodes in the BinarySearchTree"""
        if self is None:
            return
        
        if self.root_value > n1 and self.root_value > n2:
            return self.lca(self.leftChild,n1,n2)
        
        if self.root_value < n1 and self.root_value < n2:
            return self.lca(self.rightChild,n1,n2)
        
        return self
    
    def __len__(self):
        """This method returns the length of the BinarySearchTree"""
        s = self.size()
        return s
    def __repr__(self):
        if self.root_value is None:
            return "BinarySearchTree()"
        else:
            lst = self.preorder()
            return f"BinarySearchTree({lst},default = preorder)"      
        
def main():
    """This is a main function"""
    print("-----------------[TREE-MENU]--------------")
    print("1.INSERT")
    print("2.DELETE")
    print("3.SEARCH")
    print("4.PREORDER")
    print("5.INORDER")
    print("6.POSTORDER")
    print("7.LEVELORDER")
    print("8.MINIMUM")
    print("9.MAXIMUM")
    print("10.PEEK")
    print("11.SIZE")
    print("12.HEIGHT")
    print("13.BALANCE")
    print("14.LOWEST COMMON ANCESTOR")
    print("15.EXIT") 
    print("------------------------------------------")
    try:
        bst = BinarySearchTree()
        i = 0
        while i != "15":
            ch = input("Enter your choice: ")
            if ch == "1":
                val = eval(input("Enter the element to be inserted into the Tree: "))
                bst.insert(val)
            
            elif ch == "2":
                val = eval(input("Enter the element to be deleted from the Tree: "))
                bst.delete(val)
            
            elif ch == "3":
                key = eval(input("Enter the key to be searched: "))
                bst.search(key)
            
            elif ch == "4":
                print("This is Preorder traversal!")
                s = bst.preorder()
                print(s)
                
                
            elif ch == "5":
                print("This is Inorder traversal!")
                s = bst.inorder()
                print(s)
            
            elif ch == "6":
                print("This is Postorder traversal!")
                s = bst.postorder()
                print(s)
            
            elif ch == "7":
                print("This is Levelorder traversal!")
                ll = bst.levelorder()
                print(ll)
            
            elif ch == "8":
                bst.minimum()
            
            elif ch == "9":
                bst.maximum()
            
            
            elif ch == "10":
                bst.peek()
            
            elif ch == "11":
                s = bst.size()
                print("The size of the Tree is: "+str(s))
            
            elif ch == "12":
                h = bst.height()
                print("The height of the Tree is: "+str(h))
            
            elif ch == "13":
                sorted_arr = bst.inorder()
                b = bst.balance(sorted_arr)
                balancedTree = b.preorder()
                print("The balanced Tree is: "+str(balancedTree))
            
            
            elif ch == "14":
                node1 = eval(input("Enter node1 value: "))
                node2 = eval(input("Enter node2 value: "))
                tree = bst.lca(node1,node2)
                print("The Lowest Common Ancestor for {} and {} is: {}".format(node1,node2,tree.root_value))
              
            elif ch == "15":
                print("Exitting from the BST program!")
                break
            
            else:
                print("Invalid Choice!")
                print("Please enter again!")
            i = i + 1
    
    except (KeyboardInterrupt,Exception) as e:
        print("There was an error in Tree operatons: "+str(e))

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
