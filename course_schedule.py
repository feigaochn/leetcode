# coding: utf-8

# author: Fei Gao
#
# Course Schedule
#
# There are a total of n courses you have to take, labeled from 0 to n - 1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
# For example:
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# click to show more hints.
# Hints:
# This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
# Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
# Topological sort could also be done via BFS.


class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        node_in = [set() for _ in range(numCourses)]
        node_out = [set() for _ in range(numCourses)]

        for n1, n2 in prerequisites:
            node_in[n2].add(n1)
            node_out[n1].add(n2)
        found = set()
        while True:
            # find a node with zero in-degree
            n = 0
            while n < numCourses:
                if len(node_in[n]) == 0 and n not in found:
                    break
                else:
                    n += 1
            # no such node
            if n == numCourses:
                break
            # find one
            found.add(n)
            for m in node_out[n]:
                node_in[m].remove(n)
            node_out[n] = set()

        return len(found) == numCourses


def main():
    solver = Solution()
    tests = [
        (2, [[1, 0]]),
        (2, [[0, 1], [1, 0]])
    ]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.canFinish(*test)
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
