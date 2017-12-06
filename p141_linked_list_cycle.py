# author: Fei Gao
# date: Wed Jun  4 22:26:56 2014
#
# Linked List Cycle
#
# Given a linked list, determine if it has a cycle in it.
# Follow up:
# Can you solve it without using extra space?


class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None:
            return False
        elif head.next == head:
            return True
        h1 = head
        h2 = head
        end = False
        while not end:
            if h2.next and h2.next.next:
                h2 = h2.next.next
            else:
                end = True
                break
            h1 = h1.next
            if h1 == h2:
                break
        return not end


def main():
    solver = Solution()
    pass


if __name__ == '__main__':
    main()
    pass
