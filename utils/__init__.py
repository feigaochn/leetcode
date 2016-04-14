#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def pre_order(self):
        return '[{}, {}, {}]'.format(self.val, self.left, self.right)

    def __str__(self):
        return self.pre_order()

    def __repr__(self):
        return self.__str__()


def build_binary_tree(lst: list):
    if not lst:
        return None
    root = TreeNode(lst.pop(0))
    nodes = [root]
    while lst:
        top = nodes.pop(0)
        val = lst.pop(0)
        if val is not None:
            top.left = TreeNode(val)
            nodes.append(top.left)
        if not lst:
            break
        val = lst.pop(0)
        if val is not None:
            top.right = TreeNode(val)
            nodes.append(top.right)

    return root


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