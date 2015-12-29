# Author: Fei Gao
# Date: 7/6/14

from node.sllist import *


def test_ListNode():
    l1 = ListNode(1)
    assert l1.val == 1
    assert l1.next == None

    l2 = ListNode([0, 1])
    assert l2.val == 0
    assert l2.next.val == 1
    assert l2.next.next == None
    assert l2.to_list() == [0, 1]


if __name__ == '__main__':
    # test_TreeNode()
    test_ListNode()
