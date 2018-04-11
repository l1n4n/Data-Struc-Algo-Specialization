# python3
# n, m = map(int, input().split())
# edges = [ list(map(int, input().split())) for i in range(m) ]
"""
Here x[i, j] the ith position in the Hamiltonian path is occupied by node j
https://www.csie.ntu.edu.tw/~lyuu/complexity/2011/20111018.pdf
The Clauses of R(G) and Their Intended Meanings
1. Each node j must appear in the path.
• x1j ∨ x2j ∨ · · · ∨ xnj for each j.
2. No node j appears twice in the path.
• ¬xij ∨ ¬xkj for all i, j, k with i != k.
3. Every position i on the path must be occupied.
• xi1 ∨ xi2 ∨ · · · ∨ xin for each i.
4. No two nodes j and k occupy the same position in the path.
• ¬xij ∨ ¬xik for all i, j, k with j != k.
5. Nonadjacent nodes i and j cannot be adjacent in the path.
• ¬xki ∨ ¬xk+1,j for all (i, j) !∈ G and k = 1, 2, . . . , n − 1
"""

n, m = map(int, input().split())
nodes = range(1, n + 1)

clauses = []
C = 1 # counter for the permutations, xij
hash_all = {}


for i in nodes:
    for j in nodes:
        if i != j:
            hash_all[(i, j)] = 0 # initialize all edges (0)

for _ in range(m):
    u, v = map(int, input().split())
    hash_all[(u, v)] = 1
    hash_all[(v, u)] = 1 # get edges

def varnum(i, j):
    global n
    x =  i * n + j
    global C
    if not x in hash_all: # hash the permutations as new variables xij (key: i * n + j, value: permutation id)
        hash_all[x] = C
        C += 1
    return x


#each node j must appear in the path
for j in nodes:
    clauses.append([varnum(i, j) for i in nodes])

#no node j appears twice in the path
for i in nodes:
    for k in nodes:
        if i < k:
            for j in nodes:
                clauses.append([-varnum(i, j), -varnum(k, j)])


#every position i on the path must be occupied
for i in nodes:
    clauses.append([varnum(i, j) for j in nodes])


#no two nodes j and k occupy the same postion in the path
for j in nodes:
    for k in nodes:
        if j < k:
            for i in nodes:
                clauses.append([-varnum(i, j), -varnum(i, k)])


#Nonadjacent nodes i and j cannot be adjacent in the path.
for i in nodes:
    for j in nodes:
        if (i, j) in hash_all:
            if hash_all[(i, j)] == 0:
                for k in range(1, n):
                    clauses.append([-varnum(k, i), -varnum(k + 1, j)])

print (len(clauses), C - 1) # number of formulas, number of variables
for x in clauses:
    for y in x:
        p = hash_all[abs(y)] # get the veriable(a permutation id) from the hash table
        if y < 0:
            p *= -1
        print (p , end = " ")
    print (0)

# def printEquisatisfiableSatFormula():
#     print("3 2")
#     print("1 2 0")
#     print("-1 -2 0")
#     print("1 -2 0")

# printEquisatisfiableSatFormula()
