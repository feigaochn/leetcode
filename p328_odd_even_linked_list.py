# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: odd even linked list
#
# Given a singly linked list, group all odd nodes together followed by the
# even nodes. Please note here we are talking about the node number and not
# the value in the nodes.
# You should try to do it in place. The program should run in O(1) space
# complexity and O(nodes) time complexity.
# 
# Example:
# Given 1->2->3->4->5->NULL,
# return 1->3->5->2->4->NULL.
# 
# Note:
# The relative order inside both the even and odd groups should remain as it
# was in the input.
# The first node is considered odd, the second node even and so on ...
# 
# Credits:Special thanks to @DjangoUnchained for adding this problem and
# creating all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Linked List


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        h = head
        o = oh = head
        e = eh = head.next
        while True:
            if e.next is not None:
                o.next = e.next
                o = o.next
            else:
                o.next = eh
                break
            if o.next is not None:
                e.next = o.next
                e = e.next
            else:
                o.next = eh
                e.next = None
                break
        return head

from node.sllist import SinglyLinkedList

def main():
    solver = Solution()
    h = SinglyLinkedList([1])
    tests = [
        ((h.head,), None),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params[0]))
        print('Expect: ' + str(expect))

        result = solver.oddEvenList(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
