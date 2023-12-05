import time
from GenerateTC import generate_dataset
import sys 
sys.setrecursionlimit(10**9)

from memory_profiler import memory_usage
from tqdm import tqdm

def BB(nodeCount, nodeSets : list, setsPrice : list):
    minCost = sum(setsPrice)
    resultSubset =  [x for x in range(len(nodeSets))]


    def findMin(index : int, currentCost : int, choosenIndex : list, currentSets : set):
        nonlocal minCost, resultSubset
        if index == len(nodeSets):
            if(len(currentSets) == nodeCount):
                if(minCost > currentCost):
                    minCost = currentCost
                    resultSubset = choosenIndex
        else:
            if(currentCost > minCost):
                return
            
            tempSets = currentSets.copy()
            for i in range(index + 1, len(nodeSets)):
                tempSets = tempSets.union(set(nodeSets[i]))
            if len(tempSets) == nodeCount:
                findMin(index + 1, currentCost, choosenIndex.copy(), currentSets.copy())

            tempSets = currentSets.copy()
            for i in range(index, len(nodeSets)):
                tempSets = tempSets.union(set(nodeSets[i]))

            if(len(tempSets) == nodeCount):
                copyChoosenIndex = choosenIndex.copy()
                copyChoosenIndex.append(index)

                copyCurrentSets = currentSets.copy()
                copyCurrentSets = copyCurrentSets.union(nodeSets[index])

                findMin(index + 1, currentCost + setsPrice[index], copyChoosenIndex, copyCurrentSets)

    findMin(0, 0, [], set())
    return minCost, resultSubset

def Greedy(nodeCount, nodeSets : list, setsPrice : list):
    currentSets = set()
    result = []
    price = 0
    while len(currentSets) != nodeCount:
        choosenSubset = max(nodeSets, key=lambda s: len(set(s) - currentSets)/setsPrice[nodeSets.index(s)])
        result.append(choosenSubset)
        price += setsPrice[nodeSets.index(choosenSubset)]
        currentSets = currentSets.union(set(choosenSubset))
    
    return price, result

def main(nodeCount, nodeSets, setsPrice):
    start_time = time.time()
    minCost, resultSubset=(Greedy(nodeCount, nodeSets, setsPrice))
    end_time = time.time()
    mem_usage = memory_usage((Greedy, (nodeCount, nodeSets, setsPrice)), interval=0.1, timeout=200)

    greedyTime = end_time - start_time
    greedyMem = max(mem_usage)

    start_time = time.time()
    minCost, resultSubset=(BB(nodeCount, nodeSets, setsPrice))
    end_time = time.time()
    mem_usage = memory_usage((BB, (nodeCount, nodeSets, setsPrice)), interval=0.1, timeout=200)

    BBTime = end_time - start_time
    BBMem = max(mem_usage)
    return (greedyTime, greedyMem), (BBTime, BBMem)

if __name__=='__main__':
    NUMBER_OF_ITERATION = 5
    resultTimeGreedy = [0, 0, 0]
    resultTimeBB = [0, 0, 0]

    resultMemoryGreedy = [0, 0, 0]
    resultMemoryBB = [0, 0, 0]

    number_of_element = [20, 200, 2000]
    number_of_subset = [20, 60, 250]
    for i in tqdm(range(NUMBER_OF_ITERATION)):
        for j in range(len(number_of_element)):
            tc = generate_dataset(number_of_element[j], number_of_subset[j])

            greedy, bb = main(tc[0],tc[1],tc[2])
            
            resultTimeGreedy[j] += greedy[0]
            resultMemoryGreedy[j] += greedy[1]

            resultTimeBB[j] += bb[0]
            resultMemoryBB[j] += bb[1]
    
    for j in range(len(resultTimeGreedy)):
        resultTimeGreedy[j] /= NUMBER_OF_ITERATION
        resultMemoryGreedy[j] /= NUMBER_OF_ITERATION

        resultTimeBB[j] /= NUMBER_OF_ITERATION
        resultMemoryBB[j] /= NUMBER_OF_ITERATION

        print(f"Number Of Element = {number_of_element[j]}, Number Of Subset = {number_of_subset[j]}")
        print(f"Greedy: Memory = {resultMemoryGreedy[j]} MiB, Time = {resultTimeGreedy[j]} ms")
        print(f"Branch&Bound: Memory = {resultMemoryBB[j]} MiB, Time = {resultTimeBB[j]} ms")
        print("="*100)
