#!/usr/bin/env python
# coding: utf-8

# p677

class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._kv = dict()  # type: dict
        self._prefix = dict()  # type: dict

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        dv = val - self._kv.get(key, 0)
        self._kv[key] = val
        for i in range(len(key)):
            prefix = key[:i + 1]
            self._prefix[prefix] = self._prefix.get(prefix, 0) + dv

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self._prefix.get(prefix, 0)


if __name__ == '__main__':
    # Your MapSum object will be instantiated and called as such:
    obj = MapSum()
    obj.insert("abc", 3)
    obj.insert("ab", 2)
    print(obj.sum("a"))
    obj.insert("apple", 3)
    print(obj.sum("ap"))
    obj.insert("app", 2)
    print(obj.sum("apple"))
