"""
Design your implementation of the doubly linked list.
A node in a doubly linked list should have three attributes: val, next.val and prev.val

Solution:
  - Linked List is a data structure with zero or several elements.
  - The python list is an example of an implementation of a doubly linked list
  -  Use Sentinel nodes for implementation
    - Sentinel nodes are widely used in the trees and linked lists as pseudo-heads, pseudo-tails, etc
    - Sentinels nodes will be used here to simplify insert and delete.
  - It contains size, sentinel head and sentinel tail.
"""

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None



class LinkedList:
    def __init__(self):
        self.size = 0
        # sentinel nodes as pseudo-head and pseudo-tail
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index > self.size:
            return -1

        # choose the fastest way: to move from the head
        # or to move from the tail
        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
        
        return curr.val

    def addAtHead(self, value):
        """
        Add a node of value before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        """
        pred, succ = self.head, self.head.next

        self.size += 1
        to_add = ListNode(value)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def addAtTail(self, value):
        """
        Append a node of value val to the last element of the linked list.
        """
        succ, pred = self.tail, self.tail.prev
        
        self.size += 1
        to_add = ListNode(value)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def addAtIndex(self, index, value):
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return

        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev

        # insertion itself
        self.size += 1
        to_add = ListNode(value)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index > self.size:
            return

        # find predecessor and successor of the node to be deleted
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
        
        # delete pred.next 
        self.size -= 1
        pred.next = succ
        succ.prev = pred

    def __str__(self):
        if not self.size:
            return str(self.head.val)
        
        node = self.head
        linkedlist = ""
        for _ in range(self.size):
            node = node.next
            linkedlist += "{}<-->".format(node.val) 
        return linkedlist


def main():
    linkedList = LinkedList()
    print("Empty Linked list: {}".format(linkedList))
    linkedList.addAtHead(3)
    print("Add 3 at head: {}".format(linkedList))
    linkedList.addAtHead(1)
    print("Add 1 at head: {}".format(linkedList))
    linkedList.addAtTail(4)
    print("Add 4 at tail: {}".format(linkedList))
    linkedList.addAtIndex(1, 2)
    print("Add 2 at index 1: {}".format(linkedList))
    print("Element at position 1 is {}".format(linkedList.get(1)))       
    linkedList.deleteAtIndex(1)
    print("delete index 1 element: {}".format(linkedList))
    print("Element at position 1 is {}".format(linkedList.get(1)))


if __name__ == '__main__':
    main()
