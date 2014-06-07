# Author: Fei Gao
# Date: 7/6/14


# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, x=None):
        self.left = None
        self.right = None
        self.dic = dict()
        if isinstance(x, (list, tuple)):
            self = self.build_from_list(list(x))
        else:
            self.val = x

    def print_mlr(self):
        print("Print tree in (mid -> left -> right):")
        if self is None:
            print("empty tree")
        else:

            def _print_mlr(root, indent=0):
                if root is None:
                    pass
                print((' ' * indent + '{}').format(root.val))
                if root.left is not None:
                    indent += 2
                    print(' ' * indent + 'L:')
                    _print_mlr(root.left, indent)
                    print(' ' * indent + ':L')
                    indent -= 2
                if root.right is not None:
                    indent += 2
                    print(' ' * indent + 'R:')
                    _print_mlr(root.right, indent)
                    print(' ' * indent + ':R')
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
                    func(node.left, index * 2 + 1)
                if node.right is not None:
                    func(node.right, index * 2 + 2)

            func(self, 0)

    def to_dict(self):
        self._build_dic()
        return self.dic

    def to_list(self):
        self._build_dic()
        n = 1 + max(self.dic.keys())
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
            l_idx = idx * 2 + 1
            r_idx = idx * 2 + 2
            if l_idx < n and lst[l_idx] is not None:
                node.left = TreeNode(lst[l_idx])
                build_children(node.left, l_idx)
            if r_idx < n and lst[r_idx] is not None:
                node.right = TreeNode(lst[r_idx])
                build_children(node.right, r_idx)

        self.val = lst[0]
        build_children(self, 0)
        return self

    def preorderTraversal(self):
        preorder = []
        if self is None:
            return preorder
        queue = [self]
        while len(queue) != 0:
            node = queue.pop(0)
            preorder.append(node.val)
            if node.right is not None:
                queue.insert(0, node.right)
            if node.left is not None:
                queue.insert(0, node.left)
        return preorder

    def __bool__(self):
        return self is not None

