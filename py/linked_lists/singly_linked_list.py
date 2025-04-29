"""
Design your implementation of the singly linked list.
A node in a singly linked list should have two attributes: val and next.val

Solution:
  - Linked List is a data structure with zero or several elements.
  -  Use Sentinel nodes for implementation
    - Sentinel nodes are widely used in the trees and linked lists as pseudo-heads, pseudo-tails, etc
    - Sentinels nodes will be used here to simplify insert and delete.
  - Note: Sentinel node in singly linked list is used as a pseudo-head and is always present. 
"""

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = ListNode(0)  # sentinel node as pseudo-head
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        return curr.value

    def addAtIndex(self, index, value):
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return

        self.size += 1

        # find predecessor of the node to be added
        pred = self.head
        for _ in range(index):
            pred = pred.next

        # node to be added
        to_add = ListNode(value)
        # insertion itself
        to_add.next = pred.next
        pred.next = to_add

    def addAtHead(self, value):
        """
        Add a node of value before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, value)

    def addAtTail(self, value):
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, value)

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index > self.size:
            return

        self.size -= 1

        # find predecessor of the node to be deleted
        pred = self.head
        for _ in range(index):
            pred = pred.next

        # delete pred.next 
        pred.next = pred.next.next
    
    def __str__(self):
        if not self.size:
            return str(self.head.value)
        
        node = self.head
        linkedlist = ""
        for _ in range(self.size):
            node = node.next
            linkedlist += "{}-->".format(node.value) 
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
