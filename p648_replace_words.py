#!/usr/bin/env python
# coding: utf-8


class Solution(object):
    def replaceWords(self, dicts, sentence):
        """
        :type dicts: List[str]
        :type sentence: str
        :rtype: str
        """
        import re
        pattern = re.compile(r'^({})'.format('|'.join(sorted(dicts, key=len))))
        outputs = []
        for word in sentence.split():
            match = re.match(pattern, word)
            if match:
                outputs.append(match.groups()[0])
            else:
                outputs.append(word)
        print(outputs)
        return ' '.join(outputs)


if __name__ == '__main__':
    sol = Solution()
    print(sol.replaceWords(
        dicts=["cat", "bat", "rat", 'ca'],
        sentence="the cattle was rattled by the battery"
    ))
