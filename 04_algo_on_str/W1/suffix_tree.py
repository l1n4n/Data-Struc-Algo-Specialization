# python3
import sys

class SuffixTree(object):
    """Naive way to build a compressed suffix tree
    """
    # node_count = 0
    class Node(object):
        def __init__(self):
            self.id = SuffixTree.node_count  
            self.outedge_dict = {} # {first Symbol: edge} 
            # SuffixTree.node_count += 1 for debugging

    class Edge(object):
        def __init__(self, start):             
            self.start = start # start is the index of the first matching symbol
            self.length = 0 # s[start, start + length] = 'label'
            self.end_node = None

    def __init__(self, s):
        self.nodes = [] # keep the node population
        self.N = len(s)
        self.s = s
        self.root = SuffixTree.Node()

        self.nodes.append(self.root)

        new_edge = SuffixTree.Edge(0)
        new_edge.length = self.N        
        self.root.outedge_dict[s[0]] = new_edge


        for i in range(self.N):
            # start at root; we’ll walk down as far as we can go
            currentNode = self.root
            j = i
            while j < self.N:
                startSymbol = s[j]
                if startSymbol in currentNode.outedge_dict:
                    edge_to_match = currentNode.outedge_dict[startSymbol]
                    start_idx = edge_to_match.start
                    edge_length = edge_to_match.length
                    length = 1
                    # Walk along edge until we exhaust edge or until we mismatch                     
                    while length < edge_length and s[j + length] == s[start_idx + length]:
                        length += 1
                    if length == edge_length: # we exhausted the edge
                        if edge_to_match.end_node == None:
                            new_node = SuffixTree.Node()
                            self.nodes.append(new_node)  
                        currentNode = edge_to_match.end_node                        
                        j += length
                       
                    else: # we fall off the edge in the middle
                        original_length = edge_to_match.length # remember the original length, we are going to cut it into two segments
                        new_length = length
                        # shorten the edge that we fall off --> this is the up segment of the edge, this edge's end_node is going to be the split point
                        edge_to_match.length = new_length

                        # this node is going to be the end_point of the down segment of the edge_to_match
                        orphan_node = edge_to_match.end_node

                        # prepare two new starting index for two new EDGES 
                        old_start, new_start = start_idx + length, j + length 
                        # make the edge's end_point has two new outgoing edges
                        edgeOld = SuffixTree.Edge(old_start) # this is the down segment of the edge_to_match
                        edgeOld.length = original_length - new_length
                        edgeOld.end_node = orphan_node # adopt the edge_to_match's end_point

                        edgeNew = SuffixTree.Edge(new_start) # a new edge for the unmatched part
                        edgeNew.length = self.N - new_start # always set the wholly new edge's length to the longest possible, then we can cut it

                        split_node = SuffixTree.Node() # make a new node, its offsprings are the new two edges
                        split_node.outedge_dict[s[old_start]] = edgeOld 
                        split_node.outedge_dict[s[new_start]] = edgeNew
                        
                        edge_to_match.end_node = split_node                                                
                        self.nodes.append(split_node)                        
                        
                else:
                    new_edge = SuffixTree.Edge(j) # no match from the beginning, so make a wholly new edge
                    new_edge.length = self.N - j # set its length to be the longest possible
                    currentNode.outedge_dict[s[j]] = new_edge # add to the currentNode's outgoing edge dict


    def get_edges(self):
        self.result = []
        for node in self.nodes:
            if node and node.outedge_dict != {}:
                edge_list = list(node.outedge_dict.values())
                while edge_list:
                    edge = edge_list.pop()
                    begin, ending = edge.start, edge.start + edge.length
                    self.result.append(self.s[begin:ending])
        return self.result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    suftree = SuffixTree(text)
    result = suftree.get_edges()
    print("\n".join(result))