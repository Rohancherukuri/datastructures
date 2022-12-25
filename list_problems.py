from list_structure import DoublyLinkedList
from time import time

def middle_node(d_list):
    if d_list.is_empty():
        return None
    else:
        slow_pt = fast_pt = d_list.head
        while fast_pt is not None and fast_pt.next is not None:
            slow_pt = slow_pt.next
            fast_pt = fast_pt.next.next
        middle_node = d_list.get_nodeIndex(slow_pt.data)
        return middle_node
    
def nth_node(d_list,n):
    temp = d_list.tail
    for i in range(1,n):
        temp = temp.prev
    val = d_list.remove(temp.data)
    return val

def main():
    dl = DoublyLinkedList()
    mylist = dl.DL_list([21,12,-5,13,56,0,4,76])
    print(mylist)
    output1 = middle_node(mylist)
    print("The middle node index is: "+str(output1))
    n = int(input("Enter nth_node: "))
    output2 = nth_node(mylist,n)
    print("The nth node deleted from end of the list is: "+str(output2))
    print(mylist)
    
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