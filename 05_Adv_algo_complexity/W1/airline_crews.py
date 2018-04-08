# python3

import queue


class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

    def available(self):
        return self.capacity - self.flow


# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even),
        # we should get id + 1 due to the described above scheme.
        # On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge
        # for backward - id is odd), id - 1 should be taken.
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def read_data():
    n, m = map(int, input().split())
    graph = FlowGraph(2 + n + m)
    # source : -1, sink: n + m, flight vertices: 0 ~ n-1, crew vertices: n ~ n+m-1
    for i in range(n):
        graph.add_edge(-1, i, 1) 

        clist = input().split()
        for idx in range(len(clist)):
            if int(clist[idx]) == 1:
                graph.add_edge(i, n + idx, 1)

    for i in range(m):
        graph.add_edge(n + i, n + m, 1)

    return graph, n, m


def find_path(graph, from_, to):
    visit = queue.Queue()
    visit.put((from_, [])) # vertex, edges consisting the path

    visited = set() # visited vertices

    while not visit.empty():
        (u, p) = visit.get()
        if u in visited: # ignore the visited vertex
            continue

        visited.add(u) # mark u as visited

        edges = graph.get_ids(u) # get edge ids starting from u

        for id in edges:
            edge = graph.get_edge(id) # get edge

            if edge.v in visited: # ignore visited vertex
                continue

            if edge.available() > 0: # capacity - flow > 0 (for either forward edge(cap- flow) or backedge(0- (-flow)))
                if edge.v == to: # reach the sink
                    p.append(id) # adding edge idx to the path
                    return p

                path = list(p) # not reach the sink yet
                path.append(id) # add edge idx to the path
                visit.put((edge.v, path)) # put (the end vertex, the path so far) to the queue

    return None # if not return before, no path to the sink


def find_bottleneck(graph, p):
    bottleneck = graph.get_edge(p[0]).available() # the first flow

    for e in p: # loop all edges along the path to find the bottleneck
        x = graph.get_edge(e).available()
        if x < bottleneck:
            bottleneck = x

    return bottleneck


def max_flow(graph, from_, to):
    flow = 0

    while True:
        p = find_path(graph, from_, to)
        if p is None: # no path to aug
            break

        bottleneck = find_bottleneck(graph, p)
        
        # update the residual graph
        for e in p:
            graph.add_flow(e, bottleneck)
            
        # add the flow of the new path
        flow += bottleneck

    return flow


def solve():
    graph, n, m = read_data()
    # find the max flow, update the residual graph
    max_flow(graph, -1, n + m)
    matching = [-1] * n

    # find the matches in the final residual graph
    # by checking which edges starting from flight vertices to crew vertices that have flow (== 1)
    for i in range(n):
        for j in graph.get_ids(i):
            edge = graph.get_edge(j)
            if edge.flow != 1 or edge.v < n:
                continue

            matching[i] = edge.v - n
            break

    line = [str(-1 if x == -1 else x + 1) for x in matching]
    print(' '.join(line))


# class MaxMatching:
#     def read_data(self):
#         n, m = map(int, input().split())
#         adj_matrix = [list(map(int, input().split())) for i in range(n)]
#         return adj_matrix

#     def write_response(self, matching):
#         line = [str(-1 if x == -1 else x + 1) for x in matching]
#         print(' '.join(line))

#     def find_matching(self, adj_matrix):
#         # Replace this code with an algorithm that finds the maximum
#         # matching correctly in all cases.
#         n = len(adj_matrix)
#         m = len(adj_matrix[0])
#         matching = [-1] * n
#         busy_right = [False] * m
#         for i in range(n):
#             for j in range(m):
#                 if adj_matrix[i][j] and matching[i] == -1 and (not busy_right[j]):
#                     matching[i] = j
#                     busy_right[j] = True
#         return matching

#     def solve(self):
#         adj_matrix = self.read_data()
#         matching = self.find_matching(adj_matrix)
#         self.write_response(matching)

if __name__ == '__main__':
    solve()
