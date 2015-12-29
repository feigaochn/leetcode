# Author: Fei Gao
# Date: 7/6/14


class ListNode:
    """singly-linked node
    """

    def __init__(self, x=None):
        """
        :rtype : object
        """
        self.val = self.next = None
        if isinstance(x, list):
            if len(x) == 1:
                self.val = x[0]
                self.next = None
            elif len(x) > 1:
                self.val = x[0]
                self.next = ListNode(x[1:])
        else:
            self.val = x

    def to_list(self):
        r = []
        p = self
        while p:
            r.append(p.val)
            p = p.next
        return r

    def __str__(self):
        return str(self.to_list())


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
        elif isinstance(x, ListNode):
            self.head = x
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
        # TODO:
        # 1. insertion sort
        # 2. O(n log n) time and O(1) space
        raise NotImplementedError

    def reverse(self):
        """In-place reverse
        """
        # TODO: reverse a part of list
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

    def __eq__(self, other):
        raise NotImplementedError

    @property
    def has_cycle(self):
        # TODO: return cycle start index and length
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

    def pop(self, index=0):
        """
        :param index:
        :return: LinkNode
        """
        if index < 0:
            return self.pop_from_end(-index)
        else:
            return self.pop_from_begin(index)

    def pop_from_end(self, n=1):
        """Remove the n-th node from end (starting from 1)
        In place, one pass
        :param n: n > 0
        :return:
        """
        # let ph be 1st, pn be n-th
        ph = self.head
        pn = self.head
        i = 1
        while pn.next is not None and i < n:
            pn = pn.next
            i += 1
        # print(i, pn)
        # len < n
        if i < n:
            raise IndexError('linked list index out of range')
        # len == n
        if i == n and pn.next is None:
            self.head = self.head.next
            return ph

        # len > n
        # let pn be (n+1)-st
        pn = pn.next
        # pn be last 1-st
        while pn.next is not None:
            pn = pn.next
            ph = ph.next
        # now ph is the last (n+1)-st
        ret = ph.next
        ph.next = ph.next.next
        return ret

    def pop_from_begin(self, n=0):
        """Remove the n-th node from start (starting from 0)
        In place, one pass
        :param n: n >= 0
        :return:
        """
        raise NotImplementedError
        # let ph be 0-th, pn be (n-2)-th
        ph = self.head
        pn = self.head
        i = 0
        while pn.next is not None and i < n - 2:
            pn = pn.next
            i += 1
        print(n, i, pn)
        return
        # len < n
        if i < n:
            raise IndexError('linked list index out of range')
        # len == n
        if i == n and pn.next is None:
            self.head = self.head.next
            return ph

        # len > n
        # let pn be (n+1)-st
        pn = pn.next
        # pn be last 1-st
        while pn.next is not None:
            pn = pn.next
            ph = ph.next
        # now ph is the last (n+1)-st
        ret = ph.next
        ph.next = ph.next.next
        return ret

    def merge(self, other):
        """ Merge two sorted linked list
        :param other: sorted link list
        :return: sorted link list
        """
        raise NotImplementedError

    def merge_k_sorted(self, others):
        """ Merge k sorted linked lists and return it as one sorted list
        """
        raise NotImplementedError

    def rotate(self, shift=0):
        """in place rotation
        :param shift:
        :return:
        """
