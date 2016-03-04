# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: merge two sorted lists
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Linked List
# 
# Show Similar Problems
# 
#  (H) Merge k Sorted Lists
#  (E) Merge Sorted Array
#  (M) Sort List
#  (M) Shortest Word Distance II


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(None)
        p = head
        p1 = l1
        p2 = l2

        while True:
            if p1 is None:
                p.next = p2
                break
            elif p2 is None:
                p.next = p1
                break
            else:
                if p1.val < p2.val:
                    p.next = p1
                    p1 = p1.next
                    p = p.next
                else:
                    p.next = p2
                    p2 = p2.next
                    p = p.next
        return head.next


def main():
    solver = Solution()
    tests = [
        (('param',), 'result'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.mergeTwoLists(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
