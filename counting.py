# Implementing a custom Counter object
import numpy as np
import random
import time

class Counter:
    """This is Counter class"""
    def __init__(self,iterable):
        """This is Counter class constructor"""
        self.c = iterable
    
    def frequency(self):
        """This method notes the frequency of elements prersent in the iterable"""
        self.container = {}
        for i in self.c:
            if i not in self.container:
                self.container[i] = 0
            self.container[i] += 1
        
        self.container = {k:v for k,v in sorted(self.container.items(),key = lambda kv:kv[1],reverse = True)}
        return
    
    def top_most(self,top):
        """This method returns the top most elements present in the dictionary"""
        return dict(list(self.container.items())[:top])
    
    def __repr__(self):
        """This method is speacial method"""
        return f"Counter({self.container})"


def main():
    """This is a main function"""
    size = int(input("Enter the size of the array: "))
    A = np.array([random.SystemRandom().randint(1,11) for _ in range(size)])
    print("The array is:",A)
    c = Counter(A)
    c.frequency()
    print(c)
    top = int(input("Enter the most top number: "))
    print("Th top most elements with highest frequency present in the array are:",c.top_most(top))
    
if __name__ == "__main__":
    try:
        t1 = time.perf_counter()
        main()
        t2 = time.perf_counter()
        
    except (KeyboardInterrupt,Exception) as e:
        print("Error occured: "+str(e))
    
    finally:
        t3 = t2 - t1
        print("[Finished in: "+str(round(t3,3))+" sec]")