# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: implement queue using stacks
#
# Implement the following operations of a queue using stacks.
# 
# push(x) -- Push element x to the back of queue.
# 
# pop() -- Removes the element from in front of queue.
# 
# peek() -- Get the front element.
# 
# empty() -- Return whether the queue is empty.
# 
# Notes:
# 
# You must use only standard operations of a stack -- which means only push to
# top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may
# simulate a stack by using a list or deque (double-ended queue), as long as
# you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek
# operations will be called on an empty queue).
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
#  (E) Implement Stack using Queues


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.data.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.data.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        return self.data[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.data) == 0


def main():
    pass


if __name__ == '__main__':
    main()
    pass
