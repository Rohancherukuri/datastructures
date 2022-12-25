class Queue:
    """
        Ex:-
            |10|
            |20|
            |30|
            |40|
            |50|
            |60|
            |70|
    """
    """This is Queue class"""
    def __init__(self,length):
        """This is a constructor of Queue class"""
        self.frontmost = -1
        self.rearmost = -1
        self.queue = []
        self.length = length
    
    def is_empty(self):
        """This method checks wheather the Queue is empty or not"""
        if self.frontmost == -1 or self.frontmost > self.rearmost:
            return True
        else:
            return False
    
    def is_full(self):
        """This method checks wheather the Queue is full or not"""
        if self.rearmost == self.length -1:
            return True
        else:
            return False
        
    def enqueue(self,val):
        """This method enqeueus the elements into the Queue"""
        if self.is_full():
            print("The Queue is full!")
        else:
            if self.frontmost  == -1:
                self.frontmost = 0
            self.queue.append(val)
            self.rearmost = self.rearmost + 1
            
    def dequeue(self):
        """This method dequeues the elements into the Queue"""
        if self.is_empty():
            print("Queue is empty!")
        else:
            d_val = self.queue.pop(0)
            self.frontmost = self.frontmost + 1
            return d_val
            
    def front(self):
        """This method shows the front most element in the Queue"""
        f = self.frontmost
        return self.queue[f]
        
    def rear(self):
        """This method shows the rear most element in the Queue"""
        r = self.rearmost
        return self.queue[r]
        
    def size(self):
        """This method shows the size of the Queue"""
        return len(self.queue)
        
    def find(self,key):
        """This method finds the elements in the Queue"""
        for i in range(len(self.queue)):
            if key == self.queue[i]:
               return i
        else:
            print("The key "+str(key)+" is not found!")
    
    def __len__(self):
        """This is magic method which gives the length of the Queue"""
        return len(self.queue)
    
    def __repr__(self):
        """This is magic method which gives  the string repr of the Queue"""
        return "Queue()"
    
def main():
    size = int(input("Enter the queue size: "))
    q = Queue(size)
    for i in range(1,size+1):
        q.enqueue(i)
    print(q)
    key = eval(input("Enter key value: "))
if __name__ == "__main__":
    try:    
        main()
    except Exception as e:
        print(e)