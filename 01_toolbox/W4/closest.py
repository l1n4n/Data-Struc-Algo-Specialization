#Uses python3
import sys
import math

def minimum_dist_sqance(x, y):
    """x is the list of x-coordinate
    y is the list of y-coordinate"""
    xy_list = list(zip(x, y))
    xP = sorted(xy_list, key=lambda x: x[0]) # xP is P(1) .. P(N) sorted by x coordinate
    yP = sorted(xy_list, key=lambda x: x[1]) # yP is P(1) .. P(N) sorted by y coordinate
    best = min_dist_sq(xP, yP)
    return math.sqrt(best)     
    

def min_dist_sq(xP, yP):
    N = len(xP)
    
    if N <= 3:
        return brute_force_dist_sq(xP)
    else:
        split = N // 2
        xL = xP[:split]
        xR = xP[split:]
        #xm = xL[-1][0]
        yL = []
        yR = []
        setxL = set(xL) # using set is fast than compare with xm
        for i in yP:
            if i in setxL:
                yL.append(i)
            else:
                yR.append(i)
        

    dL = min_dist_sq(xL, yL)
    dR = min_dist_sq(xR, yR)
    dmin = dL
    if dR < dL:
        dmin = dR
    
    dS = closest_split(xP, yP, dmin)
    if dS < dmin:
        dmin = dS
        
    return dmin

def brute_force_dist_sq(xP):
    N = len(xP)
    d = dist_sq(xP[0], xP[1])
    if N == 2:
        return d
    elif N == 3:
        for i in range(N - 1):
            for j in range(i + 1, N):
                if i != 0 and j != 1: # we have already caculated d
                    d_new = dist_sq(xP[i], xP[j])
                    if d_new < d:
                        d = d_new
    return d

def dist_sq(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2                        
            

def closest_split(xP, yP, dmin):
    N = len(xP)
    split = N // 2
    xL = xP[:split]
    xm = xL[-1][0]
    yS = []
    for x in yP:
        if xm - dmin < x[0] < xm + dmin:
            yS.append(x)
    nS = len(yS)
    d = dmin
    for i in range(nS - 1):
        for j in range(i + 1, min(i + 5, nS)): # no need to check 7
            d_cross = dist_sq(yS[i], yS[j])
            if d_cross < d:
                d = d_cross
    
    return d

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_dist_sqance(x, y)))
