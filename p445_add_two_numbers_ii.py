from utils import ListNode, build_linked_list

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def get_len(l):
            count = 0
            while l is not None:
                l = l.next
                count += 1
            return count

        def helper(l1, l2, offset):
            if l1 is None:
                return None
            if offset == 0:
                result = ListNode(l1.val + l2.val)
                post = helper(l1.next, l2.next, 0)
            else:
                result = ListNode(l1.val)
                post = helper(l1.next, l2, offset-1)
            if post is not None and post.val > 9:
                result.val += 1
                post.val -= 10
            result.next = post
            return result

        size1 = get_len(l1)
        size2 = get_len(l2)

        head = ListNode(1)
        if size1 < size2:
            head.next = helper(l2, l1, size2 - size1)
        else:
            head.next = helper(l1, l2, size1 - size2)
        if head.next.val > 9:
            head.next.val -= 10
            return head
        else:
            return head.next


fn = Solution().addTwoNumbers

print(fn(build_linked_list([7,2,4,3]), build_linked_list([5,6,4])))
