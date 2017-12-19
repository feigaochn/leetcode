class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        N = len(edges)
        cc = dict()  # connected components
        for i in range(N):
            cc[i + 1] = {i + 1}

        for u, v in edges:
            if cc[u] == cc[v]:
                return [u, v]
            update = cc[u] | cc[v]
            for w in update:
                cc[w] = update


fn = Solution().findRedundantConnection

print(fn([[1, 2], [1, 3], [2, 3]]))
print(fn([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
