#!/usr/bin/env python
# coding: utf-8


"""
Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
"""

from utils import ListNode, build_linked_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if root is None:
            return [None for _ in range(k)]
        length = 0
        p = root
        while p is not None:
            length += 1
            p = p.next

        average, rem = divmod(length, k)
        list_lens = [average + 1] * rem + [average] * (k - rem)

        heads = []
        p = root
        pre = None
        for l in list_lens:
            if pre:
                pre.next = None
            heads.append(p)
            while l:
                l -= 1
                if p.next:
                    pre = p
                    p = p.next
                else:
                    pre = p
                    p = None
        return heads


if __name__ == '__main__':
    sol = Solution().splitListToParts
    print(sol(build_linked_list([1, 2, 3]), 5))
    print(sol(build_linked_list([1, 2, 3]), 3))
    print(sol(build_linked_list([1, 2, 3]), 2))
    print(sol(build_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3))
