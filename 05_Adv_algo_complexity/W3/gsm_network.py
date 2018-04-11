# python3
# reduce 3-coloring problem to an instance of SAT
"""
Input Format. first line----n: the number of vertices and edges in the graph. m: the number of vertices
Each of the next m lines contains two integers u and v — the numbers of vertices connected by an edge. 

Output Format. a boolean formula in the conjunctive normal form (CNF). 
If it is possible to color the vertices of the input graph in 3 colors such that any two vertices
connected by an edge are of different colors, the formula must be satisfiable. 
Otherwise, the formula must be unsatisfiable. 
"""
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]


def printEquisatisfiableSatFormula():
    print("{} {}".format(n + m*3, n*3)) # number of formulas, number of variables
    # each vertex has to be colored by some color
    for i in range(1, n+1):
        print("{} {} {} 0".format(i, i+n, i+n*2))
    # vertices connected by an edge must have different colors
    for edge in edges:
        fr, to = edge
        print('{} {} 0'.format(-fr, -to))
        print('{} {} 0'.format(-fr-n, -to-n))
        print('{} {} 0'.format(-fr-n*2, -to-n*2))

printEquisatisfiableSatFormula()
