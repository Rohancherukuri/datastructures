# Checking if a given number is a perfect square or not
from time import time

def isPerfectSquare(x):
    """This method checks if the given number is perfect square or not"""
    if x < 0:
        return False 
    if int(x) != x:
        return False
    i = 0
    while i <= x:
        if i*i == x:
            return True
        i += 1
    else:
        return False

def isPerfectSquareOptimized(x):
    """This is the optimized function which computes un O(log(n)) time"""
    if x < 0:
        return False 
    if int(x) != x:
        return False
    
    low ,high = 0, x
    while low <= high:
        mid = (low + high) // 2 # integer division in python
        
        if mid*mid == x:
            return True
        
        elif mid*mid > x:
            high = mid - 1
        
        else:
            low = mid + 1
    return False



def main():
    """This is main method"""
    num = eval(input("Enter a number: "))
    ans = isPerfectSquareOptimized(num)
    if ans is True:
        if num is float:
            num = int(num)
        print("The number {} is a perfect square!".format(num))
    
    else:
        print("The number {} is not a perfect square!".format(num))


if __name__ == "__main__":
    try:
        t1 = time()
        main()
        t2 = time()
    
    except Exception as e:
        print("Sorry there was an error in your code:  "+str(e))
    
    finally:
        t3 = t2 - t1
        print("[Finished in: "+str(round(t3,3))+" sec]")  