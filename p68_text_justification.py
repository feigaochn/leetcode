class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words:
            return [' ' * maxWidth]
        lines = [[]]
        for word in words:
            if not lines[-1]:
                lines[-1].append(word)
            elif (sum(map(len, lines[-1])) + len(lines[-1]) + len(word)
                    <= maxWidth):
                lines[-1].append(word)
            else:
                lines.append([word])
        ans = []
        for line in lines:
            nw = len(line)
            space = maxWidth - sum(len(w) for w in line)
            if nw == 1:
                ans.append(line[0] + ' ' * space)
                continue
            each, remain = divmod(space, nw-1)
            s = ""
            for i, w in enumerate(line):
                if i < remain:
                    s += w + ' ' * (each + 1)
                elif i < nw - 1:
                    s += w + ' ' * each
                else:
                    s += w
            ans.append(s)
        last = ans.pop()
        ws = ' '.join(last.strip().split())
        ans.append(ws + ' ' * (maxWidth - len(ws)))

        return ans


fn = Solution().fullJustify
print(
    [(p, len(p)) for p in fn(["This", "is", "an", "example", "of", "text", "justification."], 16)])
