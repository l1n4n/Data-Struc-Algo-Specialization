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
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


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


if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
