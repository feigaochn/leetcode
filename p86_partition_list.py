# Given a linked list and a value x, partition it such that
# all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each
# of the two partitions.
#
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.

from node.sllist import ListNode


class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode

    def partition(self, head, x):
        less_head = None
        less_tail = None
        more_head = None
        more_tail = None
        p = head
        while p is not None:
            if p.val < x:
                if less_head is None:
                    less_head = ListNode(p.val)
                    less_tail = less_head
                else:
                    less_tail.next = ListNode(p.val)
                    less_tail = less_tail.next
            else:
                if more_head is None:
                    more_head = ListNode(p.val)
                    more_tail = more_head
                else:
                    more_tail.next = ListNode(p.val)
                    more_tail = more_tail.next
            p = p.next
        if less_head is None:
            return more_head
        else:
            less_tail.next = more_head
            return less_head


def test():
    pass

if __name__ == '__main__':
    test()
