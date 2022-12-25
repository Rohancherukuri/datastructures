# Implementing Min Heap and Max Heap

class MinHeap(object):
    def __init__(self,root_val):
        self.leftchild = None
        self.root_val = root_val
        self.rightchild = None
    
    
    def push(self,val):
        pass
    
    def pop(self,val):
        pass
    
    def heapify(self,iterable):
        if len(iterable) == 0:
            return 
        else:
            pass
    
    def peek(self):
        return self.root_val
    
    def size(self):
        total = 1
        if self.root_val is None:
            return 0
        if self.leftchild:
            total += self.leftchild.size()
        if self.rightchild:
            total += self.rightchild.size()
        return total
    
    def __repr__(self):
        if self is None:
            return "MinHeap()"
        else:
            return f"MinHeap({None})"