from node import TreeNode

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place

    def flatten(self, root):
        def gao(root):
            if root is None:
                return root, root
            elif root.left is None and root.right is None:
                return root, root
            elif root.left is None and root.right is not None:
                rhead, rtail = gao(root.right)
                root.left = None
                root.right = rhead
                rhead.left = None
                rtail.left = None
                rtail.right = None
                return root, rtail
            elif root.left is not None and root.right is None:
                lhead, ltail = gao(root.left)
                root.left = None
                root.right = lhead
                lhead.left = None
                ltail.left = None
                ltail.right = None
                return root, ltail
            elif root.left is not None and root.right is not None:
                lhead, ltail = gao(root.left)
                rhead, rtail = gao(root.right)
                root.left = None
                root.right = lhead
                lhead.left = None
                ltail.left = None
                ltail.right = rhead
                rhead.left = None
                rtail.left = None
                rtail.right = None
                return root, rtail

        gao(root)


solver = Solution()

root5 = TreeNode()
root5.build_from_list([1,2,3,4])
solver.flatten(root5)
print(root5.to_dict())

root4 = TreeNode()
root4.build_from_list([2,1,4,None,None,3,5])
solver.flatten(root4)
print(root4.to_dict())
