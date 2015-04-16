#!/bin/env python3

# author: Fei Gao
#
# Min Stack
#
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Show Tags


class MinStack:
    def __init__(self):
        self._stack = list()
        self._min = list()

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self._stack.append(x)
        self._min.append(x if not self._min else min(x, self._min[-1]))

    # @return nothing
    def pop(self):
        self._stack.pop()
        self._min.pop()

    # @return an integer
    def top(self):
        return self._stack[-1]


    # @return an integer
    def getMin(self):
        return self._min[-1]

