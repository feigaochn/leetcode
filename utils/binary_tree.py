"""
Common utilities on binary tree
"""

__all__ = ["null", "TreeNode", "build_binary_tree"]

null = None


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def pre_order(self):
        return "[{}, {}, {}]".format(self.val, self.left, self.right)

    def tree2str(self, t):
        if t is None:
            return ""
        s = str(t.val)
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        if left and right:
            return "{}({})({})".format(s, left, right)
        if not left and right:
            return "{}({})({})".format(s, left, right)
        if left and not right:
            return "{}({})".format(s, left)
        return s

    def __str__(self):
        # return self.pre_order()
        return self.tree2str(self)

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
