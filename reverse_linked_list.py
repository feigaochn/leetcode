# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: reverse linked list
#
# Reverse a singly linked list.
# click to show more hints.
# Hint:
# A linked list can be reversed either iteratively or recursively.
# Could you implement both?
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Linked List
# 
# Show Similar Problems
# 
#  (M) Reverse Linked List II
#  (M) Binary Tree Upside Down
#  (E) Palindrome Linked List


# Definition for singly-linked list.
from node.sllist import ListNode


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        first = last = head
        while last.next: last = last.next

        def helper(h, t):
            if h.next == t:
                t.next = h
                h.next = None
                return h, t
            else:
                h2, t = helper(h.next, t)
                h.next = None
                h2.next = h
                return h, t

        first, last = helper(first, last)
        first.next = None
        return last


def main():
    solver = Solution()
    l = ListNode([0, 1, 2])

    tests = [
        ((l,), l.to_list()),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.reverseList(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
