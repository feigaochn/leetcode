# author: Fei Gao
#
# Remove Nth Node From End Of List
#
# Given a linked list, remove the nth node from the end of list and return its head.
# For example,
# Given linked list: 1->2->3->4->5, and n = 2.
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.

from node.sllist import *


class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        # let ph be 1st, pn be n-th
        ph = head
        pn = head
        i = 1
        while pn.next is not None and i < n:
            pn = pn.next
            i += 1
        # print(i, pn)
        # len < n
        if i < n:
            return head
        # len == n
        if i == n and pn.next is None:
            head = head.next
            return head

        # len > n
        # let pn be (n+1)-st
        pn = pn.next
        # pn be last 1-st
        while pn.next is not None:
            pn = pn.next
            ph = ph.next
        # now ph is the last (n+1)-st
        ph.next = ph.next.next
        return head


def main():
    solver = Solution()
    lst = [1, 2, 3, 4, 5]
    tests = [
        (lst, 2),
        (lst, 4),
        (lst, 5),
        (lst, 6)
    ]
    for test in tests:
        print(test)
        sll = SinglyLinkedList(test[0])
        print(sll)
        print(' ->')
        result = SinglyLinkedList(solver.removeNthFromEnd(sll.head, test[1]))
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
