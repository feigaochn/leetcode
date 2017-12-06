#!/usr/local/bin/python3
# Definition for singly-linked list.

from node.sllist import ListNode


class Solution:
    # @param head, a ListNode
    # @return a ListNode

    def deleteDuplicates(self, head):
        if head is None:
            return None
        self.myhead = ListNode(head.val)
        self.cur = self.myhead
        p = head.next
        while p is not None:
            if p.val != self.cur.val:
                self.cur.next = ListNode(p.val)
                self.cur = self.cur.next
            p = p.next
        return self.myhead


def test():
    # construct
    head = ListNode(0)
    p = head
    for i in range(12):
        p.next = ListNode(i//2)
        p = p.next

    # print origin
    p = head
    while p is not None:
        print(p.val, end='->')
        p = p.next
    print('\n')

    shead = Solution().deleteDuplicates(head)

    # print result
    sp = shead
    while sp is not None:
        print(sp.val, end='->')
        sp = sp.next
    print('\n')

if __name__ == '__main__':
    test()
