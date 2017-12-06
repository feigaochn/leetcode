#!/usr/bin/env python
# coding: utf-8


class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        hash = defaultdict(list)
        for path in paths:
            dirname, *files = path.split()
            for file in files:
                filename, content = file[:-1].split('(', 1)
                hash[content].append(dirname + '/' + filename)
        return [fs for fs in hash.values() if len(fs) > 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findDuplicate([]))
    print(sol.findDuplicate(
        ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)",
         "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
    ))
