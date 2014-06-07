# author: Fei Gao
#
# Add Two Numbers
#
# You are given two linked lists representing two non-negative
# numbers. The digits are stored in reverse order and each of
# their nodes contain a single digit. Add the two numbers and
# return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

from node.sllist import ListNode, SinglyLinkedList


class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        h1 = l1
        h2 = l2
        h = ListNode(0)
        p = h
        carry = 0
        while h1 and h2:
            p.next = ListNode(h1.val + h2.val + carry)
            p = p.next
            carry = p.val // 10
            p.val %= 10
            h1 = h1.next
            h2 = h2.next
        h3 = h1 if h1 else h2
        while h3:
            p.next = ListNode(h3.val + carry)
            p = p.next
            carry = p.val // 10
            p.val %= 10
            h3 = h3.next
        while carry != 0:
            p.next = ListNode(carry)
            p = p.next
            carry = p.val // 10
            p.val %= 10
        return h.next


def main():
    solver = Solution()
    tests = [[[2, 4, 3], [5, 6, 4]],
             [[1], [9] * 3]]
    for test in tests:
        l1 = SinglyLinkedList(test[0])
        print(l1)
        l2 = SinglyLinkedList(test[1])
        print(l2)
        print(' ->')
        result = SinglyLinkedList(solver.addTwoNumbers(l1.head, l2.head))
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
