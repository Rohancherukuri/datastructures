# This is a test function optimized in python using numba
from time import time
from numba import jit

@jit(nopython = True)
def test():
    l = []
    for x in range(10):
        for y in range(1000):
            for z in range(10000):
                if (z + y + x) / 10 == x:
                    l.append(x)
        print(x)
    return l
if __name__ == "__main__":
    try:
        start = time()
        t = test()
    
    except Exception as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        end = time() - start
        print("Finished in: {} sec".format(end))
        