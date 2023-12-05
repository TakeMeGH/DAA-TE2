__author__ = "Andrea Rubbi"
import time

def bypassbranch(subset, i):#bypass a branch 
    for j in range(i-1, -1, -1):
        if subset[j] == 0:
            subset[j] = 1
            return subset, j+1

    return subset, 0

def nextvertex(subset, i, m):
    if i < m:
        subset[i] = 0
        return subset, i+1
    else:
        for j in range(m-1, -1, -1):
            if subset[j] == 0:
                subset[j] = 1
                return subset, j+1
                
    return subset, 0

def BB(universe,sets,costs):
    subset = [1 for x in range(len(sets))]#all sets in
    subset[0] = 0
    bestCost = sum(costs) #actually the worst cost 
    i = 1

    while i > 0:
        if i < len(sets):
            cost, tSet = 0, set()# t for temporary
            for k in range(i):
                cost += subset[k]*costs[k]#if 1 adds the cost to total
                if subset[k] == 1: tSet.update(set(sets[k]))#if 1 add the set to the cover

            if cost > bestCost:#if the cost is larger than the currently best one, no need of further investigation
                subset, i = bypassbranch(subset, i)
                continue
            for k in range(i, len(sets)): tSet.update(set(sets[k]))
            if tSet != universe:#that means that the set was essential at this point to complete the uni.
                subset, i = bypassbranch(subset, i)
            else:
                subset, i = nextvertex(subset, i, len(sets))
                
        else:
            cost, fSet = 0, set()# f for final
            for k in range(i):
                cost += subset[k]*costs[k]
                if subset[k] == 1: fSet.update(set(sets[k]))

            if cost < bestCost and fSet == universe:
                bestCost = cost
                bestSubset = subset[:]
            subset, i = nextvertex(subset, i , len(sets))

    return bestCost, bestSubset

def main(a,b,c,z=time.time()):
    m = a
    S = b 
    C = c
    F = set([x for x in range(1,m+1)])
    X=(BB(F,S,C))
    cost= X[0]
    sets= X[1]
    cover= []
    for x in range(len(sets)):
        if sets[x]==1:
            cover.append(S[x])
    print('covering sets: ',cover,'\n','total cost: ',cost,'$')
    print('time:',time.time()-z)

m1= 5
S1 = [[1,3],[2],[1,2,5],[3,5],[4],[5],[1,3],[2,4,5],[1,2],[2,3]]
P1 = [11,4,9,12,5,4,13,12,8,9]
m2 = 15
S2 = [[2, 7, 8, 10, 12, 13], [1, 3, 5, 8, 10, 11, 12, 15], [1, 2, 3, 4, 5, 6, 7, 12, 13], [2, 6, 7, 11, 12, 13], [9, 10, 12, 13], [1, 3, 7, 9, 11, 12, 13], [1, 3, 5, 6, 8, 9, 10, 11, 12, 13], [1, 3, 4, 5, 6, 7, 12, 14, 15], [1, 2, 3, 6, 11, 12], [1, 2, 4, 5, 7, 8], [5, 9, 10, 11, 15], [3, 5, 6, 7, 8, 9, 12, 13, 14], [1, 3, 4, 5, 6, 7, 9, 11, 13, 14, 15], [1, 3, 5, 6, 8, 12, 14], [2, 4, 7, 9, 10, 12, 14], [1, 3, 5, 6, 11, 15], [2, 3, 4, 5, 6, 8, 10, 11, 12, 13, 14, 15], [1, 2, 4, 6, 7, 11, 13, 14, 15], [1, 2, 8, 12, 13, 14], [1, 2, 6, 7, 8, 13], [1, 2, 3, 5, 7, 8, 10, 12, 14, 15], [4, 5, 7, 12, 15], [1, 2, 3, 5, 11, 14], [1, 6, 8, 11, 13], [1, 6, 7, 8, 9, 10, 13], [1, 2, 3, 4, 5, 9, 11, 15], [2, 3, 4, 7, 9, 11, 12], [1, 3, 4, 5, 8, 10, 11, 12, 13], [2, 8, 9, 10], [6, 11, 13], [2, 5, 6, 8, 9, 11, 12, 13, 15], [2, 4, 6, 7, 8, 9, 10, 11, 13, 15], [1, 2, 3, 4, 5, 7, 8, 10, 11], [1, 2, 6, 9, 11, 13, 14, 15], [1, 4, 9, 10, 11, 13, 15], [1, 2, 3, 4, 6, 8, 12, 14, 15], [4, 5, 7, 8, 10, 13, 14], [2, 4, 8, 9, 11, 14], [2, 3, 4, 5, 6, 7, 10, 11, 14], [1, 2, 4, 5, 6, 7, 9, 11, 13, 14, 15], [1, 2, 6, 7, 9, 10, 12, 15], [1, 3, 6, 9, 10, 15], [2, 3, 5, 7, 8, 9, 11], [2, 3, 4, 5, 8, 10, 11, 12, 15], [1, 3, 4, 5, 6, 7, 9, 10, 12, 15]]
P2 = [16, 7, 16, 39, 29, 35, 19, 27, 27, 33, 38, 8, 41, 16, 12, 7, 41, 6, 34, 48, 23, 16, 31, 18, 35, 31, 41, 21, 50, 21, 12, 37, 35, 44, 48, 18, 14, 26, 22, 13, 29, 34, 28, 45, 50]
m3 = 5
S3 = [[1], [1, 2, 3, 4, 5], [2, 3], [2, 3, 4, 5], [1, 3, 4], [5], [1, 2, 4], [1, 3, 4, 5], [3, 5], [4, 5], [3], [2, 5], [4], [1, 5], [2], [1, 2, 4], [1, 3], [1, 3, 5], [2, 4, 5], [2], [1, 2, 5]]
P3 = [44, 44, 39, 24, 5, 30, 26, 42, 28, 12, 6, 45, 37, 33, 5, 42, 26, 6, 38, 11, 28]
m4 = 40
S4 = [[1, 3, 4, 6, 7, 9, 10, 15, 16, 18, 26, 31, 32, 35, 36, 38, 39, 40], [1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 17, 18, 19, 20, 23, 24, 25, 27, 31, 32, 37, 39, 40], [4, 7, 8, 10, 11, 14, 16, 17, 18, 20, 23, 24, 27, 28, 29, 34, 36, 37, 39, 40], [2, 3, 4, 7, 9, 11, 17, 20, 22, 25, 26, 27, 28, 32, 34, 35, 36, 37, 39, 40], [1, 2, 4, 6, 7, 10, 12, 13, 22, 23, 24, 26, 28, 30, 32, 33, 35, 36, 39], [1, 3, 4, 5, 6, 8, 9, 10, 12, 13, 16, 24, 25, 30, 34, 35, 36, 37, 38, 39], [2, 3, 5, 10, 11, 12, 14, 18, 20, 22, 24, 25, 27, 28, 30, 31, 33, 34, 40], [1, 3, 11, 12, 18, 19, 21, 22, 24, 25, 26, 30, 33, 35], [1, 2, 7, 9, 10, 11, 14, 16, 18, 20, 22, 25, 28, 33, 35, 38], [3, 4, 9, 10, 14, 15, 17, 18, 19, 23, 24, 26, 28, 29, 30, 32, 34, 35, 38, 39, 40], [1, 2, 3, 4, 5, 6, 7, 9, 10, 13, 14, 15, 16, 19, 20, 22, 23, 29, 30, 31, 36, 38, 39], [2, 4, 5, 7, 13, 14, 15, 17, 20, 23, 24, 25, 27, 28, 29, 30, 34, 35], [1, 2, 4, 8, 9, 11, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 31, 32, 33, 34, 35, 36, 37, 39, 40], [1, 4, 5, 6, 8, 10, 14, 17, 20, 21, 23, 24, 25, 29, 30, 40], [3, 5, 6, 10, 12, 14, 16, 17, 18, 19, 20, 22, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 37, 39], [2, 3, 5, 6, 7, 9, 14, 15, 16, 17, 20, 21, 23, 27, 28, 29, 31, 32, 34, 35, 39, 40], [2, 5, 7, 10, 11, 13, 14, 18, 20, 22, 23, 29, 32, 33, 34, 35, 38, 39], [1, 3, 6, 7, 8, 9, 10, 12, 13, 24, 29, 30, 33, 34, 35, 36, 37, 39, 40], [1, 2, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 20, 21, 26, 29, 30, 32, 33, 35, 36, 38, 39, 40], [3, 4, 7, 8, 11, 14, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 29, 30, 31, 33, 34, 36, 38, 39], [2, 3, 4, 6, 7, 9, 11, 13, 14, 15, 16, 19, 21, 24, 25, 26, 27, 28, 29, 30, 31, 33, 36, 39], [1, 2, 3, 6, 8, 10, 11, 13, 15, 16, 17, 19, 20, 21, 22, 25, 26, 34, 35, 36, 39, 40], [1, 2, 7, 12, 15, 17, 21, 24, 25, 27, 28, 30, 35, 37, 39, 40]]
P4 = [59, 68, 56, 50, 75, 95, 71, 66, 30, 28, 42, 50, 68, 34, 29, 52, 70, 85, 27, 40, 76, 82, 38]
m5 = 30
n5 = 23
S5 = [[2, 3, 4, 8, 9, 10, 11, 12, 15, 16, 18, 19, 22, 23, 24, 26, 27, 28, 29], [1, 2, 4, 5, 7, 8, 10, 11, 13, 16, 17, 19, 20, 21, 22, 23, 25, 27, 30], [1, 3, 9, 10, 16, 17, 18, 23, 24, 25, 26, 29, 30], [2, 4, 5, 6, 7, 10, 11, 12, 13, 14, 17, 20, 21, 22, 26, 27, 29, 30], [1, 6, 7, 11, 14, 17, 18, 23, 25, 26, 28, 29], [3, 5, 6, 7, 9, 10, 12, 13, 15, 16, 17, 18, 19, 21, 22, 24, 25, 26, 29], [2, 5, 6, 7, 8, 9, 10, 13, 17, 19, 20, 21, 23, 24, 25, 27, 28, 29, 30], [1, 5, 6, 8, 10, 19, 21, 24], [1, 3, 7, 8, 9, 10, 15, 19, 25, 26, 27, 30], [4, 5, 10, 11, 12, 13, 14, 16, 18, 20, 21, 22, 27, 28, 29], [1, 6, 7, 9, 17, 23, 26, 29, 30], [3, 4, 7, 8, 12, 13, 14, 15, 19, 21, 22, 24, 25, 27, 28, 29, 30], [1, 5, 6, 7, 8, 10, 15, 19, 21, 22, 27, 28, 29, 30], [1, 2, 4, 5, 6, 7, 8, 9, 11, 13, 14, 17, 19, 20, 23, 25, 26, 28, 30], [2, 3, 4, 9, 12, 15, 17, 20, 23, 26, 27, 28, 29], [4, 7, 8, 9, 11, 12, 13, 14, 15, 16, 19, 20, 25, 26, 27, 28, 29, 30], [1, 3, 5, 7, 8, 9, 18, 19, 20, 21, 22, 23, 26, 28, 29], [1, 3, 6, 7, 8, 10, 12, 13, 14, 16, 21, 23, 24, 25, 26, 27], [3, 5, 8, 9, 12, 13, 15, 18, 20, 21, 23, 24, 29], [1, 3, 4, 5, 8, 9, 10, 14, 15, 16, 18, 19, 20, 21, 22, 24, 26, 27], [2, 5, 8, 9, 12, 13, 14, 15, 17, 19, 20, 21, 24, 27, 28, 30], [2, 4, 8, 9, 12, 15, 16, 23, 24, 27, 28], [4, 5, 9, 10, 11, 12, 14, 15, 19, 22, 23, 27, 30]]
P5 = [60, 79, 49, 65, 88, 83, 38, 44, 54, 100, 65, 53, 43, 73, 63, 35, 65, 92, 74, 79, 67, 34, 95]
if __name__=='__main__':
    main(m1,S1,P1)
    main(m2,S2,P2)
    main(m3,S3,P3)
    main(m4,S4,P4)
    main(m5,S5,P5)