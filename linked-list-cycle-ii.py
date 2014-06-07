# author: Fei Gao
#
# Linked List Cycle II
#
# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.
# Follow up:
# Can you solve it without using extra space?


class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None:
            return None
        elif head.next == head:
            return head
        h1 = head
        h2 = head
        end = False
        steps = 0
        m1 = 0
        m2 = 0
        while not end:
            if h2.next and h2.next.next:
                h2 = h2.next.next
            else:
                end = True
                break
            h1 = h1.next
            steps += 1
            if h1 == h2:
                if m1 == 0:
                    m1 = steps
                else:
                    m2 = steps
                    break

        if end:
            return None

        cyc_len = m2 - m1
        h1 = head
        h2 = head
        for i in range(cyc_len):
            h2 = h2.next
        while h1 != h2:
            h1 = h1.next
            h2 = h2.next
        return h1


def main():
    solver = Solution()
    pass


if __name__ == '__main__':
    main()
    pass
