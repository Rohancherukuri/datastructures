# Using merge sort to sort a linked list of numbers in python
import random
from list_structure import SinglyLinkedList


def merge(l1: SinglyLinkedList, l2: SinglyLinkedList):
    """
        This function is used for merging two 
        sub linked lists and sort accordingly
    """
    temp = None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.data <= l2.data:
        temp = l1
        temp.next = merge(l1.next,l2)
    else:
        temp = l2
        temp.next = merge(l1,l2.next)
    return temp
    

def merge_sort(head: SinglyLinkedList):
    """This function sorts recursively on both halves of linked list"""
    if head is None or head.next is None:
        return head
    else:
        l1,l2 = divideLists(head)
        l1 = merge_sort(l1)
        l2 = merge_sort(l2)
        head = merge(l1,l2)
        return head

def divideLists(head: SinglyLinkedList):
    """
        This function divides the linked list 
        and returns the head and middle node
    """
    slow = head
    fast = head
    if fast:
        fast = fast.next
    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next
    mid = slow.next
    slow.next = None
    return head,mid

def main():
    """This is a main function"""
    try:
        l1 = SinglyLinkedList()
        l1.build(dict.fromkeys([random.randint(1,11) for _ in range(10)]))
        print("The LinkedList before sorting is:",l1)
        l1.head = merge_sort(l1.head)
        print("The linked list after sorting is:",l1)
    except Exception as e:
        print("Error occured: "+str(e))
        
if __name__ == "__main__":
    main()

    
