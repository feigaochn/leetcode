# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: delete node in a linked list
#
# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
# 
# Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Linked List
# 
# Show Similar Problems
# 
#  (E) Remove Linked List Elements


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        head = self
        s = []
        while head is not None:
            s.append(head.val)
            head = head.next
        return str(s)

    @classmethod
    def build(cls, values):
        nodes = [ListNode(v) for v in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

def main():
    solver = Solution()
    node = ListNode.build([0, 1])

    print('-' * 5 + 'TEST' + '-' * 5)
    print('Input:  ' + str(node))
    print('Expect: ' + str([1]))

    solver.deleteNode(node)
    print('Result: ' + str(node))
    pass


if __name__ == '__main__':
    main()
    pass
