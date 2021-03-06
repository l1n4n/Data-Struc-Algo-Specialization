### Dynamic programming algorithm for 3-partition problem<br>
- Extending 2-partition solution
    - see [here](https://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/) and [here](https://www.ideserve.co.in/learn/set-partition-problem-dynamic-programming)
    - for 2-partition problem, creat a 2D array $M_2$: $x$ for the target sum (total // 2); $y$ for the subsets starting from the empty set and add one each time.
    - $M_2[i][j] = 1$ means that the first $j$th numbers of A has a subset summing up to $i$
    - initialize $M_2[0][j] = 1$ for every $j$ in range(len($A$) + 1) since it means that every subset can have a subset with the sum $0$.
    - if $M_2[i][j - 1] = 1$ :
        - $M_2[i][j] = 1$
        - $M_2[i + A[j-1]][j] = 1$, where $A[j-1]$ means the $j$th number in $A$
- Extending to 3D matrix:
    - $M_3[x][y][z] = 1$ means that the first $z$th item has two disjoint subsets, one summing up to $x$ and the other summing up to $y$.
    - initialize $M_3[0][0][z] = 1$ for every $z$ in range(len($A$) + 1)
    - if $M_3[x][y][z - 1] = 1$:
        - $M_3[x][y][z] = 1$
        - $M_3[x + A[z-1]][y][z] = 1$, where $A[z-1]$ means the $z$th number in $A$
        - $M_3[x][y + A[z-1]][z] = 1$, where $A[z-1]$ means the $z$th number in $A$    
    - Note:
        - looping starts from $0$ for $x$ and $y$, since one of the subsets can summing up to $0$
        - check if $x + A[z - 1] <=$ total//3 before assigning the next cell, similarly for $y + A[z - 1]$
