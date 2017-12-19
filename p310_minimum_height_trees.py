class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return [0]

        from collections import defaultdict
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        leaves = [v for v in range(n) if len(graph[v]) == 1]
        root, *leaves = leaves

        parent = {root: -1}
        children = defaultdict(list)
        seen = set()
        front = {root}
        while front:
            v = front.pop()
            seen.add(v)
            for u in graph[v]:
                if u not in seen:
                    parent[u] = v
                    children[v].append(u)
                    front.add(u)

        height = defaultdict(int)
        for v in leaves:
            u = v
            h = 1
            while u != -1:
                if height[u] >= h:
                    break
                height[u] = h
                h += 1
                u = parent[u]

        diameter = dict()
        max_diameters = []
        for v in range(n):
            dia = height[v]
            if len(children[v]) >= 2:
                dia = max(dia, 1 + sum(
                    sorted([height[u]
                            for u in children[v]], reverse=True)[:2]))
            diameter[v] = dia
            if not max_diameters:
                max_diameters.append((v, diameter[v]))
            elif max_diameters[-1][1] < dia:
                max_diameters = [(v, dia)]
            elif max_diameters[-1][1] == dia:
                max_diameters.append((v, dia))

        def find_path(v, h):
            path = [v]
            while children[v]:
                h -= 1
                for u in children[v]:
                    if height[u] == h:
                        path.append(u)
                        break
                v = u
            return path

        diameter_path = []
        for v, dia in max_diameters:
            if height[v] == dia:
                path = find_path(v, dia)
                diameter_path.append(path)
            else:
                (_, u1), (_, u2), *_ = sorted([(height[u], u) for u in children[v]],
                                   reverse=True)
                path1 = find_path(u1, height[u1])
                path2 = find_path(u2, height[u2])
                diameter_path.append(path1[::-1] + [v] + path2)
        # print('debug', edges, 'h:', height, max_diameters, diameter_path)
        middle = set()
        for path in diameter_path:
            middle.add(path[len(path) // 2])
            if len(path) % 2 == 0:
                middle.add(path[len(path) // 2 - 1])

        return list(middle)


fn = Solution().findMinHeightTrees
print(fn(1, []))
print(fn(2, [[0, 1]]))
print(fn(n=4, edges=[[1, 0], [1, 2], [1, 3]]))
print(fn(n=6, edges=[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))

from p310_minimum_height_trees_data import data
for n, edges in data:
    print(fn(n, edges))
