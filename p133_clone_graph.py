# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    def __str__(self):
        return "({} -> {})".format(self.label,
                                   [nb.label for nb in self.neighbors])

    def __repr__(self):
        return self.__str__()


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None

        old_labels = dict()
        frontier = [node]
        old_labels[node.label] = node
        while frontier:
            top = frontier.pop()
            for nb in top.neighbors:
                if nb.label not in old_labels:
                    old_labels[nb.label] = nb
                    frontier.append(nb)

        new_labels = dict()
        for v in old_labels:
            new_labels[v] = UndirectedGraphNode(v)
        for v in old_labels:
            for nb in old_labels[v].neighbors:
                new_labels[v].neighbors.append(new_labels[nb.label])
        return new_labels[node.label]


def main():
    graph = [0, 1, 2]
    for i in range(3):
        graph[i] = UndirectedGraphNode(i)
    graph[0].neighbors = [graph[1], graph[2]]
    graph[1].neighbors = [graph[0], graph[2]]
    graph[2].neighbors = [graph[0], graph[1], graph[2]]

    fn = Solution().cloneGraph
    node = fn(graph[0])
    print(node, node.neighbors[0], node.neighbors[1])


if __name__ == '__main__':
    main()
