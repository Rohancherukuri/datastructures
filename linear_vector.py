from time import time
class Vector2D(object):
    """This is a Vector2D Class"""
    import math
    #defaults are set at 0.0 for x and y
    def __init__(self, x = None, y = None):
        """This is Vector2D constructor"""
        self.x = x
        self.y = y

    #allows us to return a string for print
    def __str__(self):
        return "Vector2D({},{})".format(self.x,self.y)

    # from_points generates a vector between 2 pairs of (x,y) coordinates
    @classmethod
    def from_points(cls, P1, P2):
        return cls(P2[0] - P1[0], P2[1] - P1[1])

    #calculate magnitude(distance of the line from points a to points b
    def get_magnitude(self):
        return math.sqrt(self.x**2+self.y**2)

    #normalizes the vector (divides it by a magnitude and finds the direction)
    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude

    #adds two vectors and returns the results(a new line from start of line ab to end of line bc)
    def __add__(self, rhs):
        return Vector2D(self.x +rhs.x, self.y+rhs.y)

    #subtracts two vectors
    def __sub__(self, rhs):
        return Vector2D(self.x - rhs.x, self.y-rhs.y)

    #negates or returns a vector back in the opposite direction
    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    #multiply the vector (scales its size) multiplying by negative reverses the direction
    def __mul__(self, scalar):
        return Vector2D(self.x*scalar, self.y*scalar)

    #divides the vector (scales its size down)
    def __div__(self, scalar):
        return Vector2D(self.x/scalar, self.y/scalar)
    
    def __len__(self):
        return len(self.values)
            

    #iterator 
    def __iter__(self):
        return self.values.__iter__()
    
    def __getitem__(self, key):
        return self.values[key]
    
    def __repr__(self):
        return "Vector2D({},{})".format(self.x,self.y) 


    #turns a list into a tuple
    def values(self):
        return (self.x,self.y)
    
    def make_tuple(self,data):
        return tuple(data)
    
    def make_vector(self,t):
        self.x = t[0]
        self.y = t[1]
        return Vector2D(self.x,self.y)
    
    def reverse(self):
        self.x,self.y = self.y,self.x
        return Vector2D(self.x,self.y)

def main():
    """This is a main function"""
    num1 = int(input("Enter first number1: "))
    num2 = int(input("Enter second number2: "))
    v = Vector2D(num1,num2)
    print(v)
    print(len(v))
    
    

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
        