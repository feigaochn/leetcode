#!/usr/bin/env python3
# coding: utf-8

import sys


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.data = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        import random
        p = self.data
        ret = p.val
        i = 1
        while p.next:
            p = p.next
            i += 1
            if random.random() < 1.0 / i:
                ret = p.val
        return ret


def main(args):
    # Your Solution object will be instantiated and called as such:
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    obj = Solution(head)
    dis = {1: 0, 2: 0, 3: 0}
    for _ in range(300):
        dis[obj.getRandom()] += 1
    print(dis)

    return


if __name__ == '__main__':
    main(sys.argv[1:])
