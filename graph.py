# Implementing Graph datastructure in python
from time import time

class Graph(object):
    """This is Graph class"""
    def __init__(self,graph = [],nodes = []):
        """This is a Graph constructor"""
        self.graph = graph
        self.nodes = nodes
       
    
    def add_node(self,V):
        """This method adds the nodes in the graph"""
        if V in self.nodes:
            print("The vertex "+str(V)+" is already present in the graph!")
        
        else:
            self.nodes.append(V)
            for n in self.graph: # Appending 0 for every row
                n.append(0)
            
            temp = []
            for i in range(len(self.nodes)):
                temp.append(0)
            self.graph.append(temp)
            
    
    def print_graph(self):
        """This method prints the adjacency matrix and list"""
        print("The Adjacency List is: "+str(self.nodes))
        print("The Adjacency Matrix is: ")
        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                print(self.graph[i][j],end = "\t")
            print()
        
                
def main():
    """This is main method"""
    try:
        g = Graph()
        vertices = ["A","B","A","C","D","E","F"]
        for i in vertices:
            g.add_node(i)
        g.print_graph()
    except (KeyboardInterrupt,Exception) as e:
        print("An Exception occurred: "+str(e))

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