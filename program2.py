graph = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1)], [('H', 1)]],
    'C': [[('J', 1)]],
    'D': [[('E', 1), ('F', 1)]],
    'G': [[('I', 1)]],
}
h = {
    'A': 1,
    'B': 6,
    'C': 12,
    'D': 10,
    'E': 4,
    'F': 4,
    'G': 5,
    'H': 7,
    'I': 1,
    'J': 1
}
status = {}
parents = {}

def getS(n):
    return status.get(n, 0)

def getH(n):
    return h.get(n, None)

def getNeighbors(n):
    return graph.get(n, [])

def getMinimumCostChild(n):
    minimumCost = 999
    minimumCostChild = []

    for listOfTuples in getNeighbors(n):
        cost = 0
        childNodes = []
        for node, weight in listOfTuples:
            cost += weight
            childNodes.append(node)

        if cost < minimumCost:
            minimumCost = cost
            minimumCostChild = childNodes.copy()

    return 0 if minimumCost == 999 else minimumCost, minimumCostChild

solution = {}

def aoStar(n, backTracking):
    if getS(n) >= 0:
        minimumCost, childrenList = getMinimumCostChild(n)
        h[n] = minimumCost
        status[n] = len(childrenList)
        solved = True

        for child in childrenList:
            parents[child] = n
            if getS(child) != -1:
                solved = False

        if solved:
            status[n] = -1
            solution[n] = childrenList

        if n != startNode:
            aoStar(parents[n], True)

        if not backTracking:
            for child in childrenList:
                status[child] = 0
                aoStar(child, False)

startNode = 'A'
aoStar(startNode, False)
print(solution)