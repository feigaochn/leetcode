class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        def freeze(llist):
            return tuple(llist[0]) + tuple(llist[1])

        def unfreeze(ttuple):
            return [list(ttuple[:3]), list(ttuple[3:])]

        def is_goal(llist):
            return llist == [[1, 2, 3], [4, 5, 0]]

        def find_zero(llist):
            for r in range(len(llist)):
                for c in range(len(llist[r])):
                    if llist[r][c] == 0:
                        return r, c

        from collections import deque
        from copy import deepcopy
        queue = deque()
        seen = set()
        t = freeze(board)
        queue.append((t, 0))
        seen.add(t)
        while queue:
            front, step = queue.popleft()
            front = unfreeze(front)
            if is_goal(front):
                return step
            zr, zc = find_zero(front)
            if zr > 0:
                next = deepcopy(front)
                next[zr - 1][zc], next[zr][zc] = next[zr][zc], next[zr - 1][zc]
                fn = freeze(next)
                if fn not in seen:
                    seen.add(fn)
                    queue.append((fn, step + 1))
            if zr < 1:
                next = deepcopy(front)
                next[zr + 1][zc], next[zr][zc] = next[zr][zc], next[zr + 1][zc]
                fn = freeze(next)
                if fn not in seen:
                    seen.add(fn)
                    queue.append((fn, step + 1))
            if zc > 0:
                next = deepcopy(front)
                next[zr][zc - 1], next[zr][zc] = next[zr][zc], next[zr][zc - 1]
                fn = freeze(next)
                if fn not in seen:
                    seen.add(fn)
                    queue.append((fn, step + 1))
            if zc < 2:
                next = deepcopy(front)
                next[zr][zc + 1], next[zr][zc] = next[zr][zc], next[zr][zc + 1]
                fn = freeze(next)
                if fn not in seen:
                    seen.add(fn)
                    queue.append((fn, step + 1))
        return -1


sol = Solution().slidingPuzzle
print(sol([[1, 2, 3], [4, 0, 5]]))
print(sol([[1, 2, 3], [5, 4, 0]]))
print(sol([[4, 1, 2], [5, 0, 3]]))
