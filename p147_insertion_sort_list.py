from utils import ListNode, build_linked_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return head
        new_head = head
        remain = head.next
        new_head.next = None
        while remain:
            cur = remain
            remain = remain.next
            p = new_head
            if p.val > cur.val:
                cur.next = new_head
                new_head = cur
            else:
                pre = p
                p = p.next
                while p:
                    if p.val > cur.val:
                        break
                    else:
                        pre, p = p, p.next
                pre.next = cur
                cur.next = p
        return new_head


fn = Solution().insertionSortList
root = build_linked_list([3, 2, 1])
print(root)
print(fn(root))

root = build_linked_list(list(range(5000, 0, -1)))
print(fn(root).val)
