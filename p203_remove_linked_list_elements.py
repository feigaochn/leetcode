# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: remove linked list elements
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6,  val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Linked List
# 
# Show Similar Problems
# 
#  (E) Remove Element
#  (E) Delete Node in a Linked List


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utils import *

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        if head is None:
            return head
        p = head
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return head


def main():
    solver = Solution()
    tests = [
        ((build_linked_list([6, 1,2,6,3,6]), 6), build_linked_list([1,2,3])),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.removeElements(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
