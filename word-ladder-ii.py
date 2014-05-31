import itertools

# TODO

class SimpleGraph(object):
    """ Simple graph: undirected, loop-less graph.
    dict of sets:
    {1 : {2, 3}, 2 : {1}, 3 : {1}}
    """

    def __init__(self, graph_dict={}):
        """ initializes a graph object
        """
        self.__graph_dict = {}
        for vertex in graph_dict:
            self.add_vertex(vertex)
            for neighbor in graph_dict[vertex]:
                self.add_vertex(neighbor)
                if vertex != neighbor:
                    self.add_edge({vertex, neighbor})

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbor in self.__graph_dict[vertex]:
                if {vertex, neighbor} not in edges:
                    edges.append({vertex, neighbor})
        return edges

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = set()

    def add_edge(self, edge):
        """
        Assume edge is of type set, tuple or list;
        between two vertices can be multiple edges!
        """
        v1, v2 = tuple(edge)
        if v1 in self.__graph_dict:
            self.__graph_dict[v1].add(v2)
        else:
            self.__graph_dict[v1] = {v2}
        if v2 in self.__graph_dict:
            self.__graph_dict[v2].add(v1)
        else:
            self.__graph_dict[v2] = {v1}

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += '\nedges: '
        for edge in self.edges():
            res += str(edge) + ' '
        return res

    def find_path(self, start_vertex, end_vertex, path=[]):
        """Find a path from start_vertex to end_vertex in graph"""
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to end_vertex in graph
        """
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.__graph_dict:
            return []
        paths = []
        for vertex in self.__graph_dict[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_vertex, path)
                for p in extended_paths:
                    paths.append(p)
        return paths

    def vertex_degree(self, vertex):
        return len(self.__graph_dict[vertex])

    def find_isolated_vertices(self):
        isolated = []
        for vertex in self.__graph_dict:
            if len(self.__graph_dict[vertex]) == 0:
                isolated.append(vertex)
        return isolated

    def min_degree(self):
        return self.degree_sequence()[-1]

    def max_degree(self):
        return self.degree_sequence()[0]

    def degree_sequence(self):
        """ calculate degree sequence
        """
        seq = [len(self.__graph_dict[vertex]) for vertex in self.__graph_dict]
        seq.sort(reverse=True)
        return seq

    def erdoes_gallai(self, dseq):
        """ checks if the condition of the Erdoes-Gallai inequality is fullfilled.
        A non-increasing sequence [d_1, ..., d_n] is the degree sequence of a simple graph if and only if the sum is even and for any $k \in \{1, ..., n\}$
        \[
        \sum_{i=1}^{k} d_i \le k(k-1) + \sum_{i=k+1}^{n} \min(d_i, k)
        \]
        """
        fullfilled = True
        dseq.sort(reverse=True)
        if sum(dseq) % 2 == 1:
            fullfilled = False
            return fullfilled
        n = len(dseq)
        for k in range(1, n + 1):
            if sum(dseq[:k]) > k * (k - 1) + sum(map(min, zip(dseq[k:], [k] * (n - k)))):
                fullfilled = False
                return fullfilled
        return fullfilled

    def density(self):
        V = len(self.__graph_dict.keys())
        E = len(self.edges())
        return 2.0 * E / (V * (V - 1))

    def is_connected(self):
        """ not concern efficiency
        """
        vertices = self.__graph_dict.keys()
        if len(vertices) < 2:
            return True
        met1 = {list(vertices)[0]}
        while True:
            met2 = met1
            for v in met1:
                met2 = met2.union(self.__graph_dict[v])
            if met1 == met2:
                break
            else:
                met1 = met2
                met2 = set({})
        return True if len(met1) == len(vertices) else False

    def diameter(self):
        v = self.__graph_dict.keys()
        pairs = [(v1, v2) for v1 in v for v2 in v if v1 < v2]
        return len(max([min(self.find_all_paths(s, e), key=len)
                        for (s, e) in pairs], key=len)) - 1


class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dic):
        if start == end:
            return [start]
        dis = lambda x, y: sum([0 if xx == yy else 1 for (xx, yy) in zip(x, y)])
        graph = SimpleGraph()
        graph.add_vertex(start)
        graph.add_vertex(end)
        if dis(start, end) == 1:
            graph.add_edge((start, end))
        for word in dic:
            graph.add_vertex(word)
            if dis(start, word) == 1:
                graph.add_edge((start, word))
            if dis(end, word) == 1:
                graph.add_edge((end, word))
        for (w1, w2) in itertools.product(dic, dic):
            if dis(w1, w2) == 1:
                graph.add_edge((w1, w2))
        paths = graph.find_all_paths(start, end)
        # print(paths)
        paths.sort(key=len)
        if len(paths) == 0:
            return []
        else:
            result = []
            for path in paths:
                if len(path) == len(paths[0]):
                    result.append(path)
                else:
                    break
            return result
        pass


if __name__ == "__main__":
    start = "hit"
    end = "cog"
    dic = ["hot", "dot", "dog", "lot", "log"]
    answer = [
        ["hit", "hot", "dot", "dog", "cog"],
        ["hit", "hot", "lot", "log", "cog"]
    ]
    print(Solution().findLadders(start, end, dic))

    start, end, dic = "cat", "fin", ["ion", "rev", "che", "ind", "lie", "wis", "oct", "ham", "jag", "ray", "nun", "ref", "wig", "jul",
                   "ken", "mit", "eel", "paw", "per", "ola", "pat", "old", "maj", "ell", "irk", "ivy", "beg", "fan",
                   "rap", "sun", "yak", "sat", "fit", "tom", "fin", "bug", "can", "hes", "col", "pep", "tug", "ump",
                   "arc", "fee", "lee", "ohs", "eli", "nay", "raw", "lot", "mat", "egg", "cat", "pol", "fat", "joe",
                   "pis", "dot", "jaw", "hat", "roe", "ada", "mac"]
    print(Solution().findLadders(start, end, dic))

