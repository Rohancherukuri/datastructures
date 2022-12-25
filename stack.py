# Implementing stack in python
from time import time

class Stack(object):
    """
        Ex:-
            |70|
            |60|
            |50|
            |40|
            |30|
            |20|
            |10|
            ----
    """
    """This is Stack class"""
    def __init__(self,length):
        """This is a constructor of Stack class"""
        self.top = -1
        self.stack  = []
        self.length = length
        
    def push(self,val):
        """This method pushes the elements into the Stack"""
        if self.top  == self.length - 1:
            print("Stack is full!")
        else:
                self.stack.append(val)
                self.top = self.top + 1
                
    def pop(self):
        """This method pops the elements into the Stack"""
        if self.top == -1 or None:
            print("Stack is empty!")
        else:
            print("The popped element from stack is: "+str(self.stack.pop()))
            self.top = self.top - 1
            
    def peek(self):
        """This method shows the topmost element in the Stack"""
        peek = self.top
        print("The peek element in stack is: "+str(self.stack[peek]))
        
    def size(self):
        """This method shows the size of the Stack"""
        print("The size of the Stack is: "+str(len(self.stack)))
        
    def display(self):
        """This method displays the elements of the Stack"""
        print("Stack(",end = "")
        for i in reversed(self.stack):
            print(i,end = " ")
        print(",type = <class 'stack.Stack'>)")
        
    def find(self,key):
        """This method finds the elements in the Stack"""
        for i in self.stack:
            if i == key:
                print("The key "+str(key)+" is found!")
                break
        else:
            print("The key "+str(key)+" is not found!")

def main():
        """This is main method"""
        print("-----------------[STACK-MENU]--------------")
        print("1.PUSH")
        print("2.POP")
        print("3.PEEK")
        print("4.SIZE")
        print("5.DISPLAY")
        print("6.FIND")
        print("7.EXIT") 
        print("-------------------------------------------")
        try:
            size  = int(input("Enter the size of the stack: "))
            s = Stack(size)
            i = 0
            while i != "7": 
                c = input("Enter your choice: ")
                if c == "1":
                    val = eval(input("Enter  the element to be pushed into Stack: "))
                    s.push(val)
                elif c == "2":
                    s.pop()
                elif c == "3":
                    s.peek()
                elif c == "4":
                    s.size()
                elif c == "5":
                    s.display()
                elif c == "6":
                    key = eval(input("Enter the key element to be searched: "))
                    s.find(key)
                elif c == "7":
                    print("Exitting from the Stack program!")
                    break
                else:
                    print("Invalid Choice!")
                    print("Please enter again!")
                i = i + 1
                
                
        except (KeyboardInterrupt,Exception) as e:
            print("There is some error in your code"+str(e))
        
if __name__ == "__main__":
    try:
        t1 = time()
        main()
    
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
    
    
    finally:
        t2 = time() - t1
        print("[Finished in: "+str(round(t2,3))+" sec]")