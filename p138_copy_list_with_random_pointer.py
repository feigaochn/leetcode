# author: Fei Gao
#
# Copy List With Random Pointer
#
# A linked list is given such that each node contains an additional
# random pointer which could point to any node in the list or null.
# Return a deep copy of the list.


# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
        # copy
        p = head
        while p is not None:
            pp = p.next
            p.next = RandomListNode(p.label)
            p.next.next = pp
            p = p.next.next
        # point random
        p1 = head
        while p1 is not None:
            p2 = p1.next
            p2.random = p1.random.next if p1.random is not None else None
            p1 = p1.next.next
        # pick new nodes
        new_head = head.next
        p = head
        q = new_head
        while p.next.next is not None:
            p_next = p.next.next
            q_next = q.next.next
            p.next = p_next
            q.next = q_next
            p = p.next
            q = q.next
        p.next = None
        q.next = None
        return new_head


def main():
    solver = Solution()
    tests = []
    for test in tests:
        print(test)
        print(' ->')
        result = solver.copyRandomList(test)
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
