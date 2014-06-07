# Author: Fei Gao
# Date: 7/6/14


class ListNode(object):
    """singly-linked node
    """
    def __init__(self, x=None):
        """
        :rtype : object
        """
        self.next = None
        self.val = x


class SinglyLinkedList(object):
    """
    singly-linked list
    """

    def __init__(self, x=None):
        """
        :param x:   None -> 0 length llist
                    list -> llist
                    others -> 1 length llist
        """
        self.len = 0
        self.head = None
        if isinstance(x, list):
            self.build_from_list(x)
        else:
            self.head = ListNode(x)

    def build_from_list(self, lst):
        if not lst:
            self.head = None
        else:
            self.head = ListNode(lst[0])
            p = self.head
            for val in lst[1:]:
                p.next = ListNode(val)
                p = p.next

    def __list__(self):
        result = []
        p = self.head
        while p:
            result.append(p.val)
            p = p.next
        return result

    def values(self):
        return self.__list__()

    def __bool__(self):
        return self.head is not None

    @property
    def __len__(self):
        """length of linked list
        """
        p = self.head
        n = 0
        while p is not None:
            n += 1
            p = p.next
        return n

    def sort(self):
        """In place sort
        """
        raise NotImplemented

    def reverse(self):
        """In-place reverse
        """
        p = self.head
        if not p or not p.next:
            return p
        pn = p.next
        p.next = None
        while pn:
            pnn = pn.next
            pn.next = p
            p = pn
            pn = pnn
        self.head = p

    @property
    def __repr__(self):
        return 'sll: ' + ' -> '.join(repr(v) for v in self.values())

    def __str__(self):
        return 'sll: ' + ' -> '.join(repr(v) for v in self.values())

    @property
    def has_cycle(self):
        head = self.head
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

    def unique(self):
        """In-place remove duplicates in a sorted singly linked list
        """
        if not self.head:
            return
        h = self.head
        p = h.next
        while p is not None:
            if p.val != h.val:
                h.next = p
                h = p
            p = p.next
        h.next = None
