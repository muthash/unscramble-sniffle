"""
Given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Solution:
    - Initialize current node to dummy head of the returning list.
    - Initialize carry to 0.
    - Initialize p and q to head of l1 and l2 respectively.
    - Loop through lists l1 and l2 until you reach both ends.
        - Set x to node p's value. If p has reached the end of l1, set to 0.
        - Set y to node q's value. If q has reached the end of l2, set to 0.
        - Set sum = x + y + carrysum
        - Update carry = sum/10
        - Create a new node with the digit value of (sum mod 10) and set it to current node's next, then advance current node to next
        - Advance both p and q.
    - Check if carry = 1, if so append a new node with digit 1 to the returning list.
    - Return dummy head's next node.
"""

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def add_two_numbers(l1, l2):
    dummy = ListNode(-1)
    cur = dummy
    carry = 0

    while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

        carry, res = divmod(val1 + val2 + carry, 10)
        cur.next = ListNode(res)
        cur = cur.next
    if carry:
        cur.next = ListNode(carry)
    return dummy.next


def main():
    l1 = ListNode(1)
    l1.next = ListNode(5)
    l2 = ListNode(8)
    l2.next = ListNode(9)

    cur = add_two_numbers(l1, l2)
    list_sum = ""
    while cur:
        list_sum += (str(cur.val) + "-->")
        cur = cur.next
    print("The Sum is: {}".format(list_sum))


if __name__ == '__main__':
    main()
