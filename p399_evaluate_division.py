class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict
        division = defaultdict(dict)
        for (up, down), ratio in zip(equations, values):
            division[up][down] = ratio
            if abs(ratio) > 1e-3:
                division[down][up] = 1.0 / ratio

        result = []
        for up, down in queries:
            if up not in division or down not in division:
                result.append(-1.0)
            elif up in division and down in division[up]:
                result.append(division[up][down])
            else:
                # bfs
                frontier = set(division[up].keys())
                while frontier:
                    mid = frontier.pop()
                    for mid2 in division[mid]:
                        if mid2 not in division[up]:
                            division[up][mid2] = division[up][mid] * division[
                                mid][mid2]
                            frontier.add(mid2)
                            if mid2 == down:
                                frontier.clear()
                                break
                result.append(division[up][down]
                              if down in division[up] else -1.0)

        return result


fn = Solution().calcEquation

print(
    fn(equations=[["a", "b"], ["b", "c"]],
       values=[2.0, 3.0],
       queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))

print(
    fn([["a", "b"], ["c", "d"]], [1.0, 1.0],
       [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]]))
