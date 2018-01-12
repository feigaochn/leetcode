class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set([tuple(int(c) for c in w) for w in deadends])
        # print(deadends)
        start = (0, 0, 0, 0)
        target = tuple(int(x) for x in target)
        if start in deadends or target in deadends:
            return -1
        seen = set()
        from collections import deque
        front = deque()
        front.append((start, 0))
        seen.add(start)

        def neighbor(lock):
            lock = list(lock)
            for i in range(len(lock)):
                lock[i] = (lock[i] + 1) % 10
                yield tuple(lock)
                lock[i] = (lock[i] - 2) % 10
                yield tuple(lock)
                lock[i] = (lock[i] + 1) % 10

        while front:
            top, d = front.popleft()
            if top == target:
                return d
            for new in neighbor(top):
                if new in deadends or new in seen:
                    pass
                else:
                    seen.add(new)
                    front.append((new, d + 1))
        return -1


sol = Solution().openLock

print(sol(["0201", "0101", "0102", "1212", "2002"], target="0202"))
print(sol(['8888'], '0009'))
print(sol(['0000'], '8888'))
print(sol(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], target="8888"))
