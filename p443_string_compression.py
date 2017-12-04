#!/usr/bin/env python
# coding: utf-8

"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.
"""


class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        p_char, count, p_head = 0, 0, 0
        while p_head < len(chars):
            if chars[p_head] == chars[p_char]:
                count += 1
                p_head += 1
            else:
                p_char += 1
                if count > 1:
                    for c in str(count):
                        chars[p_char] = c
                        p_char += 1

                chars[p_char] = chars[p_head]
                count = 0
        p_char += 1
        if count > 1:
            for c in str(count):
                chars[p_char] = c
                p_char += 1
        print(chars[:p_char])
        return p_char


if __name__ == '__main__':
    sol = Solution().compress
    print(sol(["a", "a", "b", "b", "c", "c", "c"]), '?= 6')
    print(sol(["a"]), '?= 1')
    print(sol(["a","b","b","b","b","b","b","b","b","b","b","b","b"]), '?= 4')
