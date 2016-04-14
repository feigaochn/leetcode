"""
Common utilities on linked list
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_list(self):
        vals = []
        p = self
        while p:
            vals.append(p.val)
            p = p.next
        return vals

    def __str__(self):
        return str(self.to_list())

    def __repr__(self):
        return self.__str__()


def build_linked_list(lst: list):
    if not lst:
        return None
    head = p = ListNode(lst[0])
    for v in lst[1:]:
        p.next = ListNode(v)
        p = p.next
    return head


def reverse(head: ListNode):
    p = head
    if not p or not p.next:
        return p
    pn = p.next
    p.next = None
    while pn:
        pnn = pn.next
        pn.next = p
        p = pn
        pn = pnn
    return p


def len(head: ListNode):
    """length of linked list
    """
    p = head
    n = 0
    while p is not None:
        n += 1
        p = p.next
    return n