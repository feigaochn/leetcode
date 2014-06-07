# Author: Fei Gao
# Date: 7/6/14

from node.sllist import *


def test_ListNode():
    # tests = [list(range(n)) for n in range(5)] + [[(1, 2), (3, 4)]]
    # for test in tests:
    # print(test)
    # node = ListNode(test)
    #     print(node.values())
    #     print(len(node))

    # sll = SinglyLinkedList([5, 4, 3, 2, 1])
    # print(sll)
    # sll.reverse()
    # print(sll)

    # sll = SinglyLinkedList([1, 1, 2, 3, 3][:2])
    # print(sll)
    # sll.unique()
    # print(sll)

    data = list(range(5))
    for n in [0, 1, 2, 3, 4, 5, 6]:
        sll = SinglyLinkedList(data)
        print(sll)
        sll.pop(n)
        # print(sll)


if __name__ == '__main__':
    # test_TreeNode()
    test_ListNode()
