# Implementing Python Doubly Linked List
from time import time
from typing import Union, List


class SinglyLinkedList(object):
    """This is SinglyLinkedList Class"""
    class Node(object):
        """This is Node Class"""
        def __init__(self,data: Union[int, float, str]=None):
            """This is Node Class Constructor"""
            self.data = data
            self.next = None
    
    def __init__(self):
        """This is SinglyLinkedList constructor"""
        self.head = None
        self.tail = None
        self.count = 0
    
    def is_empty(self):
        """
            This method checks and returns True if 
            SinglyLinkedList is empty and False otherwise
        """
        if self.head is None:
            return True
        else:
            return False
    def build(self, iterable: List[Union[int, float, str]]):
        """This method converts the data structure given into a SinglyLinkedList"""
        if len(iterable) == 0:
            return 
        else:
            for i in iterable:
                self.append(i)
            return self
    
    def append(self, val: Union[int, float, str]):
        """This method appends the elements at the end of SinglyLinkedList"""
        new_node = SinglyLinkedList.Node(val)
        if self.is_empty():
            self.head = new_node
            self.tail = self.head
        
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.count += 1
    
    def insert(self, val: Union[int, float, str] ,pos: int):
        """This method inserts the elements at a given position in SinglelyLinkedList"""
        if pos > self.count + 1 or pos < 1:
            raise ValueError(f"Index out of range: {pos}, size {self.count}")
        
        else:
            if pos == 1:
                new_node = SinglyLinkedList.Node(val)
                new_node.next = self.head
                self.head = new_node	
                self.count += 1
            
            elif pos == self.count + 1:
                self.append(val)
            
            else:
                temp = self.head
                for _ in range(2,pos):
                    temp = temp.next
                
                new_node = SinglyLinkedList.Node(val)
                new_node.next = temp.next
                temp.next = new_node
                self.count += 1
    
    
    def delete(self, val: Union[int, float, str]):
        """This method deletes the value from Doubly LinkedList"""
        if self.is_empty():
            print("The linked list is empty!")
            return
        elif self.head.data == val:
            x = self.head.data
            self.head = self.head.next
            self.count -= 1
            return x
        else:
            temp = self.head
            while temp.next is not None:
                if temp.data == val:
                    break
                prev = temp
                temp = temp.next
            if temp is None:
                print("The element is not found in the linked list!")
            else:
                x = temp.data
                prev.next = temp.next
                temp = None
                self.count -= 1
                return x
    
    def clear(self):
        """This method clears the whole SinglyLinkedList"""
        if self.is_empty():
            print("The SinglyLinkedList is empty!")
        else:
            for i in self:
                self.delete(i)
            return self
    
    def search(self, key: Union[int, float, str]):
        """
            This method returns True if key is found and 
            returns False if not found in DoublyLinkedList
        """
        if self.is_empty():
            return None
        else:
            temp = self.head
            while temp is not None:
                if temp.data == key:
                    return True
                temp = temp.next
            else:
                return False
    
    def min(self):
        """This method computes the minimum element present in SinglyLinkedList"""
        if self.is_empty():
            print("The SinglyLinkedList is empty!")
        else:
            min = self.head.data
            temp = self.head
            while temp is not None:
                if min > temp.data:
                    min = temp.data
                temp = temp.next
            return min
    
    def max(self):
        """This method computes the maximum element present in SinglyLinkedList"""
        if self.is_empty():
            print("The SinglyLinkedList is empty!")
        else:
            max = self.head.data
            temp = self.head
            while temp is not None:
                if max < temp.data:
                    max = temp.data
                temp = temp.next
            return max
    
    def sum(self):
        """This method computes the sum of the SinglyLinkedList"""
        if self.is_empty():
            print("The SinglyLinkedList is empty!")
        else:
            sum = 0
            temp = self.head
            while temp is not None:
                sum += temp.data
                temp = temp.next
            return sum
    
    def display(self):
        """This method displays the linked list elements in forward direction"""
        if self.is_empty():
            print("SinglelyLinkedList is empty!")
        else:
            temp = self.head
            while temp is not None:
                print(str(temp.data)+"-->",end = " ")
                temp = temp.next
            print("None")
    
    def size(self):
        """
            This method returns the number of elements 
            present in the SinglyLinkedList
        """
        return self.count
    
    def get_HeadNode(self):
        """This method returns the head of the SinglyLinkedList"""
        return self.head
    
    def get_TailNode(self):
        """This method returns the tail of the SinglyLinkedList"""
        return self.tail
    
    def __len__(self):
        """This method returns the length of the SinglelyLinkedList"""
        if self.is_empty():
            return 0
        else:
            return self.count
    
    def __iter__(self):
        """This special method is used for iterating the SinglelyLinkedList"""
        curr_node = self.head
        while curr_node is not None:
            yield curr_node.data
            curr_node = curr_node.next
    
    def __repr__(self):
        """This representation method of SinglelyLinkedLlist class"""
        if self.is_empty():
            return "SinglyLinkedList()"
        else:
            string  = f"SinglyLinkedList({self.head.data}"
            start = self.head.next
            while start is not None:
                string += f"-->{start.data}"
                start = start.next
            return string + ")"
        


class DoublyLinkedList(object):
    """This is DoublyLinkedList Class"""
    class Node(object):
        """This is Node Class"""
        def __init__(self,data: Union[int, float, str]=None):
            """This is Node Class Constructor"""
            self.prev = None
            self.data = data
            self.next = None
        
    def __init__(self):
        """This is DoublyLinkedList constructor"""
        self.head = None
        self.tail = None
        self.count = 0
    
    def is_empty(self):
        """
            This method checks and returns True if 
            DoublyLinkedList is empty and False otherwise
        """
        if self.head is None:
            return True
        else:
            return False
    
    def append(self, val: Union[int, float, str]):
        """This method appends the elements at the end of DoublyLinkedList"""
        new_node = DoublyLinkedList.Node(val)
        if self.is_empty():
            self.head = new_node
            self.tail = self.head
        
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.count += 1
    
    def insert(self, val: Union[int, float, str], pos: int):
        """This method inserts the elements at a given position in DoublyLinkedList"""
        if pos < 1 or pos > self.count + 1:
            raise ValueError(f"Index out of range: {pos}, size {self.count}")
        
        elif pos == 1:
            new_node = DoublyLinkedList.Node(val)
            self.head.prev = new_node
            self.head = new_node
            self.count += 1
        
        elif pos == self.count + 1:
            self.append(val)
        
        else:
            temp = self.head
            for _ in range(2,pos):
                temp = temp.next
            new_node = DoublyLinkedList.Node(val)
            new_node.next = temp.next
            temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp
            self.count += 1
        
        
    def delete(self, val: Union[int, float, str]):
        """This method removes the value from Doubly LinkedList"""
        if self.is_empty():
            print("The DoublyLinkedList is empty!")
        elif self.head.data == val:
            x = self.head.data
            self.head = self.head.next
            self.count -= 1
            return x
        
        elif self.tail.data == val:
            x = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
            self.count -= 1
            return x
        
        else:
            temp = self.head.next
            while temp is not None:
                if temp.data == val:
                    break
                temp = temp.next
            if temp is None:
                print("The element is not found in the DoublyLinkedList!")
            else:
                x = temp.data
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                self.count -= 1
                return x
    
    def clear(self):
        """This method clears the whole DoublyLinkedList"""
        if self.is_empty():
            return self
        else:
            for i in self:
                self.delete(i)
            return self
            
    def display(self):
        """This method displays the linked list elements in forward direction"""
        if self.is_empty():
            return None
        
        else:
            temp = self.head
            while temp is not None:
                print(str(temp.data)+"-->",end = " ")
                temp = temp.next
            print("None")
    
    def reverse(self):
        """This method displays the linked list elements in backward direction"""
        if self.is_empty():
            return None
        else:
            temp = self.tail
            while temp is not None:
                print(str(temp.data)+"-->",end = "")
                temp = temp.prev
            print("None")
    
    def search(self, key: Union[int ,float, str]):
        """
            This method returns True if key is found and 
            returns False if not found in DoublyLinkedList
        """
        if self.is_empty():
            return None
        else:
            temp = self.head
            while temp is not None:
                if temp.data == key:
                    return True
                temp = temp.next
            else:
                return False
    
    def size(self):
        """This method returns the size of the DoublyLinkedList"""
        return self.count
    
    def build(self, iterable: List[Union[int, float, str]]):
        """This method converts the data structure given into a DoublyLinkedList"""
        if len(iterable) == 0:
            return self
        
        else:
            for i in iterable:
                self.append(i)
            return self
    
    def min(self):
        """This method computes the minimum element present in DoublyLinkedList"""
        if self.is_empty():
            print("The DoublyLinkedList is empty!")
        else:
            min = self.head.data
            temp = self.head
            while temp is not None:
                if min > temp.data:
                    min = temp.data
                temp = temp.next
            return min
    
    def max(self):
        """This method computes the maximum element present in DoublyLinkedList"""
        if self.is_empty():
            print("The DoublyLinkedList is empty!")
        else:
            max = self.head.data
            temp = self.head
            while temp is not None:
                if max < temp.data:
                    max = temp.data
                temp = temp.next
            return max

    def sum(self):
        """This method computes the sum of the SinglyLinkedList"""
        if self.is_empty():
            print("The DoublyLinkedList is empty!")
        else:
            sum = 0
            temp = self.head
            while temp is not None:
                sum += temp.data
                temp = temp.next
            return sum
    
    def get_HeadNode(self):
        """This method returns the head of the DoublyLinkedList"""
        return self.head
    
    def get_TailNode(self):
        """This method returns the tail of the DoublyLinkedList"""
        return self.tail
    
    def __len__(self):
        """This method returns the length of the DoublyLinkedList"""
        return self.size()
    
    def __iter__(self):
        """This special method is used for iterating the DoublyLinkedList"""
        curr_node = self.head
        while curr_node is not None:
            yield curr_node.data
            curr_node = curr_node.next
        
    
    def __repr__(self):
        """This representation method of DoublyLinkedLlist class"""
        if self.head is None:
            return "DoublyLinkedList()"
        else:
            string = f"DoublyLinkedList({self.head.data}"      
            start = self.head.next
            while start is not None:
                string += f"-->{start.data}"
                start = start.next
            return string + ")"


class CircularSinglyLinkedList(object):
    """This is CircularSinglyLinkedList class"""
    class Node(object):
        """This is Node class"""
        def __init__(self, data: Union[int, float, str]=None):
            """This is Node Class Constructor"""
            self.data = data
            self.next = None
        
    def __init__(self):
        """This is CircularSinglyLinkedList Class Constructor"""
        self.head = None
        self.tail = None
        self.count = 0
    
    def build(self, iterable: List[Union[int, float, str]]):
        """This method converts the data structure given into a CircularSinglyLinkedList"""
        pass




def main():
    """This is a main function"""
    dl = SinglyLinkedList()
    lst = [10,20,30,40,50]
    dl.build(lst)
    print(dl)
    print("The length is:",len(dl))
    dl.insert(60,2)
    print(dl)
    print("The length is:",len(dl))
    dl.clear()
    print(dl)
    print("The length is:",len(dl))
     
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
        
