# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: implement stack using queues
#
# Implement the following operations of a stack using queues.
# 
# push(x) -- Push element x onto stack.
# 
# pop() -- Removes the element on top of the stack.
# 
# top() -- Get the top element.
# 
# empty() -- Return whether the stack is empty.
# 
# Notes:
# 
# You must use only standard operations of a queue -- which means only push to
# back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may
# simulate a queue by using a list or deque (double-ended queue), as long as
# you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top
# operations will be called on an empty stack).
# 
# Update (2015-06-11):
# The class name of the Java function had been updated to MyStack instead of
# Stack.
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# all test cases.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# 
# Stack
# Design
# 
# Show Similar Problems
# 
#  (E) Implement Queue using Stacks


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        

    def pop(self):
        """
        :rtype: nothing
        """
        

    def top(self):
        """
        :rtype: int
        """
        

    def empty(self):
        """
        :rtype: bool
        """
        # TODO
        return


def main():
    solver = Solution()
    tests = [
        (('param',), 'result'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.__init__(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
