# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: intersection of two linked lists
#
# Write a program to find the node at which the intersection of two singly
# linked lists begins.
# For example, the following two linked lists:
# 
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# 
# begin to intersect at node c1.
# Notes:
# 
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function
# returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# 
# Credits:Special thanks to @stellari for adding this problem and creating all
# test cases.
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

from utils import *


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        def reverse(head):
            p = head
            if not p or not p.next:
                return p
            pn = p.next
            p.next = None
            while pn:
                pnn = pn.next
                pn.next = p
                p = pn
                pn = pnn
            return p

        def len(head):
            """length of linked list
            """
            p = head
            n = 0
            while p is not None:
                n += 1
                p = p.next
            return n

        tailA = headA
        while tailA and tailA.next:
            tailA = tailA.next
        tailB = headB
        while tailB and tailB.next:
            tailB = tailB.next
        if tailA != tailB:
            return None

        lenA = len(headA)
        lenB = len(headB)
        tail = reverse(headA)
        lenBA = len(headB)
        reverse(tail)

        idx = (lenB - lenA + (lenBA - 1)) // 2
        p = headB
        for _ in range(idx):
            p = p.next
        return p


def main():
    solver = Solution()
    tests = [
        (('param',), 'result'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.__init__(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
