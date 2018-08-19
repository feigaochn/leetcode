# Given a directed, acyclic graph of N nodes.  Find all possible paths from
# node 0 to node N-1, and return them in any order.

# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
# graph[i] is a list of all nodes j for which the edge (i, j) exists.


class Solution:

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict

        paths = defaultdict(set)  # (source, target, length) -> {(nodes)}

        n = len(graph)
        for s, ts in enumerate(graph):
            for t in ts:
                paths[(s, t, 2)].add((s, t))

        for l in range(3, n + 1):
            for l1 in range(2, l):
                l2 = l + 1 - l1
                for s in range(n):
                    for t in range(n):
                        for k in range(n):
                            for p1 in paths[(s, k, l1)]:
                                for p2 in paths[(k, t, l2)]:
                                    paths[(s, t, l)].add(p1 + p2[1:])
        results = []
        for l in range(2, n + 1):
            results.extend([list(p) for p in paths[(0, n - 1, l)]])
        return results


sol = Solution().allPathsSourceTarget
print(sol([[1, 2], [3], [3], []]))
big = [list(range(s + 1, 15)) for s in range(15)]
print(sol(big))
