# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: palindrome linked list
#
# Given a singly linked list, determine if it is a palindrome.
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Linked List
# Two Pointers
# 
# Show Similar Problems
# 
#  (E) Palindrome Number
#  (E) Valid Palindrome
#  (E) Reverse Linked List


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utils import *


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        tail = head
        length = 1
        while tail.next:
            length += 1
            tail = tail.next

        mid = head
        for i in range((length + 1) // 2):
            mid = mid.next

        p = mid
        pn = p.next
        p.next = None
        while pn:
            pnn = pn.next
            pn.next = p
            p = pn
            pn = pnn
        # head of reverse: p

        while head and tail:
            if head.val != tail.val:
                return False
            else:
                head = head.next
                tail = tail.next
        return True


def main():
    solver = Solution()
    tests = [
        ((build_linked_list([1, 2, 3, 2, 1]),), True),
        ((build_linked_list([1, 2, 3, 3, 2, 1]),), True),
        ((build_linked_list([1, 2, 3, 4, 2, 1]),), False),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.isPalindrome(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
