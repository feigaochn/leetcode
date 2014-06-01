# Definition for a binary tree node
class TreeNode:

    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
        self.dic = dict({})

    def print_mlr(self):
        print("Print tree in (mid -> left -> right):")
        if self is None:
            print("empty tree")
        else:

            def _print_mlr(root, indent=0):
                if root is None:
                    pass
                print((' '*indent+'{}').format(root.val))
                if root.left is not None:
                    indent += 2
                    print(' '*indent+'L:')
                    _print_mlr(root.left, indent)
                    print(' '*indent+':L')
                    indent -= 2
                if root.right is not None:
                    indent += 2
                    print(' '*indent+'R:')
                    _print_mlr(root.right, indent)
                    print(' '*indent+':R')
                    indent -= 2
                pass

            _print_mlr(self, 0)
            print("\nEND")

    def _build_dic(self):
        if self is None:
            pass
        else:
            def func(node, index):
                self.dic[index] = node.val
                if node.left is not None:
                    func(node.left, index*2+1)
                if node.right is not None:
                    func(node.right, index*2+2)
            func(self, 0)

    def to_dict(self):
        self._build_dic()
        return self.dic

    def to_list(self):
        self._build_dic()
        n = 1+max(self.dic.keys())
        lst = [None for i in range(n)]
        for key in self.dic.keys():
            lst[key] = self.dic[key]
        return lst

    def min_depth(self):
        """
        find minimum depth of self
        """
        # bfs
        depth = 1
        found_leaf = False
        cur_depth = [self]
        next_depth = []
        while True:
            next_depth = []
            for node in cur_depth:
                is_leaf = True
                if node.left is not None:
                    next_depth.append(node.left)
                    is_leaf = False
                if node.right is not None:
                    next_depth.append(node.right)
                    is_leaf = False
                if is_leaf is True:
                    found_leaf = True
                    break
            if found_leaf is True:
                break
            else:
                depth += 1
                cur_depth = next_depth
        return depth

    def max_depth(self):
        """
        find maximum depth of root
        """
        # bfs
        depth = 0
        cur_depth = [self]
        while len(cur_depth) != 0:
            next_depth = []
            for node in cur_depth:
                if node.left is not None:
                    next_depth.append(node.left)
                if node.right is not None:
                    next_depth.append(node.right)
            depth += 1
            cur_depth = next_depth
        return depth

    def build_from_list(self, lst):
        if lst is []:
            return TreeNode()
        n = len(lst)

        def build_children(node, idx):
            l_idx = idx*2+1
            r_idx = idx*2+2
            if l_idx < n and lst[l_idx] is not None:
                node.left = TreeNode(lst[l_idx])
                build_children(node.left, l_idx)
            if r_idx < n and lst[r_idx] is not None:
                node.right = TreeNode(lst[r_idx])
                build_children(node.right, r_idx)

        self.val = lst[0]
        build_children(self, 0)
        return self


class ListNode:

    """
    singly-linked list
    """

    def __init__(self, x):
        self.val = x
        self.next = None

    def build_from_list(self, lst):
        if lst is None or len(lst) is 0:
            self.val = None
        self.val = lst[0]
        p = self
        for i in lst[1:]:
            p.next = ListNode(i)
            p = p.next

    def to_list(self):
        result = []
        p = self
        while p is not None:
            result.append(p.val)
            p = p.next
        return result


def test_TreeNode():
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right = TreeNode(5)
    root1.right.right = TreeNode(6)
    print(root1.to_list())

    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    print(root2.to_list())

    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)
    print(root3.to_list())

    root4 = TreeNode()
    root4.build_from_list([2, 1, 4, None, None, 3, 5])
    print(root4.to_list())

    root5 = TreeNode()
    root5.build_from_list([1, 2, 3, 4])
    print(root5.to_list())

    print(root4.min_depth())


if __name__ == '__main__':
    test_TreeNode()
