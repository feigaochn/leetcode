# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: reconstruct itinerary
#
# Given a list of airline tickets represented by pairs of departure and
# arrival airports [from, to], reconstruct the itinerary in order. All of the
# tickets belong to a man who departs from JFK. Thus, the itinerary must begin
# with JFK.
#
# Note:
#
# If there are multiple valid itineraries, you should return the itinerary
# that has the smallest lexical order when read as a single string. For
# example, the itinerary ["JFK", "LGA"] has a smaller lexical order than
# ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
#
# Example 1:
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
#     Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
#
# Example 2:
# tickets =
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
#     Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
#     Another possible reconstruction is
# ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating
# all test cases.
#
# Subscribe to see which companies asked this question
#
# Show Tags
#
# Depth-first Search
# Graph


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        fly = defaultdict(list)
        mark = {}
        for f, t in tickets:
            fly[f].append(t)
            mark[(f, t)] = False
        for f in fly:
            fly[f].sort()

        def dfs(path, result=None):
            if result:
                return result
            if len(path) == len(tickets) + 1:
                result = path[:]
                return result
            f = path[-1]
            l = len(fly[f])
            for i in range(l):
                t = fly[f].pop(i)
                r = dfs(path + [t], result)
                if r:
                    return r
                fly[f].insert(i, t)

        return dfs(['JFK'])


def main():
    solver = Solution()
    tests = [
        (([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],), ["JFK", "MUC", "LHR", "SFO", "SJC"]),
        (([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]],),
         ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]),
        (([["AXA", "EZE"], ["EZE", "AUA"], ["ADL", "JFK"], ["ADL", "TIA"], ["AUA", "AXA"], ["EZE", "TIA"],
           ["EZE", "TIA"], ["AXA", "EZE"], ["EZE", "ADL"], ["ANU", "EZE"], ["TIA", "EZE"], ["JFK", "ADL"],
           ["AUA", "JFK"], ["JFK", "EZE"], ["EZE", "ANU"], ["ADL", "AUA"], ["ANU", "AXA"], ["AXA", "ADL"],
           ["AUA", "JFK"], ["EZE", "ADL"], ["ANU", "TIA"], ["AUA", "JFK"], ["TIA", "JFK"], ["EZE", "AUA"],
           ["AXA", "EZE"], ["AUA", "ANU"], ["ADL", "AXA"], ["EZE", "ADL"], ["AUA", "ANU"], ["AXA", "EZE"],
           ["TIA", "AUA"], ["AXA", "EZE"], ["AUA", "SYD"], ["ADL", "JFK"], ["EZE", "AUA"], ["ADL", "ANU"],
           ["AUA", "TIA"], ["ADL", "EZE"], ["TIA", "JFK"], ["AXA", "ANU"], ["JFK", "AXA"], ["JFK", "ADL"],
           ["ADL", "EZE"], ["AXA", "TIA"], ["JFK", "AUA"], ["ADL", "EZE"], ["JFK", "ADL"], ["ADL", "AXA"],
           ["TIA", "AUA"], ["AXA", "JFK"], ["ADL", "AUA"], ["TIA", "JFK"], ["JFK", "ADL"], ["JFK", "ADL"],
           ["ANU", "AXA"], ["TIA", "AXA"], ["EZE", "JFK"], ["EZE", "AXA"], ["ADL", "TIA"], ["JFK", "AUA"],
           ["TIA", "EZE"], ["EZE", "ADL"], ["JFK", "ANU"], ["TIA", "AUA"], ["EZE", "ADL"], ["ADL", "JFK"],
           ["ANU", "AXA"], ["AUA", "AXA"], ["ANU", "EZE"], ["ADL", "AXA"], ["ANU", "AXA"], ["TIA", "ADL"],
           ["JFK", "ADL"], ["JFK", "TIA"], ["AUA", "ADL"], ["AUA", "TIA"], ["TIA", "JFK"], ["EZE", "JFK"],
           ["AUA", "ADL"], ["ADL", "AUA"], ["EZE", "ANU"], ["ADL", "ANU"], ["AUA", "AXA"], ["AXA", "TIA"],
           ["AXA", "TIA"], ["ADL", "AXA"], ["EZE", "AXA"], ["AXA", "JFK"], ["JFK", "AUA"], ["ANU", "ADL"],
           ["AXA", "TIA"], ["ANU", "AUA"], ["JFK", "EZE"], ["AXA", "ADL"], ["TIA", "EZE"], ["JFK", "AXA"],
           ["AXA", "ADL"], ["EZE", "AUA"], ["AXA", "ANU"], ["ADL", "EZE"], ["AUA", "EZE"]],), '?'),
    ]
    for params, expect in tests:
        print('-' * 5 + 'TEST' + '-' * 5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.findItinerary(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
