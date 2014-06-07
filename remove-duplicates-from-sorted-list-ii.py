# author: Fei Gao
#
# Remove Duplicates From Sorted List II
#
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

from node.sllist import SinglyLinkedList


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head

        h = head
        n = head.next

        dump = False
        # while n is not None and n.val == h.val:
        while not n and n.val == h.val:
            n = n.next
            dump = True

        if dump:
            if n is None:
                return None
            else:
                return self.deleteDuplicates(n)
        else:
            h.next = self.deleteDuplicates(n)
            return h


def main():
    solver = Solution()
    for test in [[1,2,3,3,4,4,5], [1,1,1,2,3], [1,1,2,2], []]:
        sllist = SinglyLinkedList(test)
        print(test, sllist.values())
        sllist.head = solver.deleteDuplicates(sllist.head)
        print(sllist.values())
    pass


if __name__ == '__main__':
    main()
    pass
