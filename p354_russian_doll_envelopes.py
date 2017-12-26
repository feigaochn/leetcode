class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda p: (p[0], -p[1]))
        heights = [h for w, h in envelopes]

        def find_lis(a):
            if not a:
                return []
            p = [0 for _ in a]
            b = []
            b.append(0)

            i = 0
            while i < len(a):
                if a[b[-1]] < a[i]:
                    p[i] = b[-1]
                    b.append(i)
                    continue

                u = 0
                v = len(b) - 1
                while u < v:
                    c = (u + v) // 2
                    if a[b[c]] < a[i]:
                        u = c + 1
                    else:
                        v = c

                if a[i] < a[b[u]]:
                    if u > 0:
                        p[i] = b[u - 1]
                    b[u] = i

                i += 1

            u = len(b)
            v = b[-1]
            while u:
                u -= 1
                b[u] = v
                v = p[v]
            return b

        return len(find_lis(heights))


fn = Solution().maxEnvelopes
print(fn([[5, 4], [6, 4], [6, 7], [2, 3]]))
