import collections
import math


class Graph:
    ''' graph class inspired by https://gist.github.com/econchick/4666413
    '''

    def __init__(self):
        self.vertices = set()

        # makes the default value for all vertices an empty list
        self.edges = collections.defaultdict(list)
        self.weights = {}

    def add_vertex(self, value):
        self.vertices.add(value)

    def add_edge(self, from_vertex, to_vertex, distance):
        if from_vertex == to_vertex: pass  # no cycles allowed
        self.edges[from_vertex].append(to_vertex)
        self.weights[(from_vertex, to_vertex)] = distance

    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Edges: " + str(self.edges) + "\n"
        string += "Weights: " + str(self.weights)
        return string


def dijkstra(graph, start):
    # initializations
    S = set()

    # delta represents the length shortest distance paths from start -> v, for v in delta.
    # We initialize it so that every vertex has a path of infinity (this line will break if you run python 2)
    delta = dict.fromkeys(list(graph.vertices), math.inf)
    previous = dict.fromkeys(list(graph.vertices), None)

    # then we set the path length of the start vertex to 0
    delta[start] = 0

    # while there exists a vertex v not in S
    while S != graph.vertices:
        # let v be the closest vertex that has not been visited...it will begin at 'start'
        v = min((set(delta.keys()) - S), key=delta.get)

        # for each neighbor of v not in S
        for neighbor in set(graph.edges[v]) - S:
            new_path = delta[v] + graph.weights[v, neighbor]

            # is the new path from neighbor through
            if new_path < delta[neighbor]:
                # since it's optimal, update the shortest path for neighbor
                delta[neighbor] = new_path

                # set the previous vertex of neighbor to v
                previous[neighbor] = v
        S.add(v)

    return (delta, previous)


def shortest_path(graph, start, end):

    delta, previous = dijkstra(graph, start)

    path = []
    vertex = end

    while vertex is not None:
        path.append(vertex)
        vertex = previous[vertex]

    path.reverse()
    return path


G = Graph()
G.add_vertex('0')
G.add_vertex('1')
G.add_vertex('2')
G.add_vertex('3')
G.add_vertex('4')
G.add_vertex('5')

G.add_edge('0', '1', 1)
G.add_edge('0', '5', 2)
G.add_edge('1', '2', 1)
G.add_edge('1', '0', 1)
G.add_edge('1', '4', 2)
G.add_edge('2', '1', 1)
G.add_edge('2', '3', 2)
G.add_edge('3', '4', 1)
G.add_edge('3', '2', 2)
G.add_edge('4', '5', 1)
G.add_edge('4', '1', 2)
G.add_edge('4', '3', 1)
G.add_edge('5', '0', 2)
G.add_edge('5', '4', 1)

# print(G)

# print(dijkstra(G, 'a'))
# print(shortest_path(G, '2', '4'))