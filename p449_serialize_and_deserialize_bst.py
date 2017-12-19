from utils import TreeNode, build_binary_tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, t):
        """Encodes a tree to a single string.

        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''
        s = str(t.val)
        left = self.serialize(t.left)
        right = self.serialize(t.right)
        if left or right:
            return '{}({})({})'.format(s, left, right)
        else:
            return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        try:
            left_bound = data.index('(')
        except ValueError:
            return TreeNode(int(data))

        right_bound = 0
        counter = 0
        while right_bound < len(data):
            if data[right_bound] == '(':
                counter += 1
            elif data[right_bound] == ')':
                counter -= 1
                if counter == 0:
                    right_bound += 1
                    break
            right_bound += 1
        val = int(data[:left_bound])
        left_data = data[left_bound+1:right_bound-1]
        right_data = data[right_bound+1:-1]
        node = TreeNode(val)
        node.left = self.deserialize(left_data)
        node.right = self.deserialize(right_data)
        return node


# Your Codec object will be instantiated and called as such:
root = build_binary_tree([1, 2, 3, 4, 5, 6])
codec = Codec()
s = codec.serialize(root)
print(s)
print(codec.deserialize("1(2)(3)"))
print(codec.deserialize(s))
