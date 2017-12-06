# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: swap nodes in pairs
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# Your algorithm should use only constant space. You may not modify the values
# in the list, only nodes itself can be changed.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Linked List
# 
# Show Similar Problems
# 
#  (H) Reverse Nodes in k-Group


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        # swap first two
        header = ListNode(0)
        header.next = head
        p1 = header
        while p1.next and p1.next.next:
            p2 = p1.next
            p3 = p2.next
            p2.next = p3.next
            p3.next = p2
            p1.next = p3
            p1 = p2

        return header.next


def main():
    solver = Solution()
    tests = [
        (('param',), 'result'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.swapPairs(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
