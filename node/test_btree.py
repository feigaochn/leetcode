

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
