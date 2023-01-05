graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'D': [('G', 1)],
    'E': [('D', 6)],
    'G': None
}
heuristicValues = {
    'A': 11,
    'B': 6,
    'C': 99,
    'D': 1,
    'E': 7,
    'G': 0,
}
parents = {}
openList = []
closedList = []
g = {}


def h(n):
    return heuristicValues.get(n, None)


def getNeighbors(n):
    return graph.get(n, None)


def aStar(startNode, stopNode):
    parents[startNode] = startNode
    g[startNode] = 0
    openList.append(startNode)
    while len(openList) > 0:  # missed while loop
        n = None
        for v in openList:
            if n is None or g[n] + h(n) > g[v] + h(v):
                n = v

        if n is None:
            return n

        if n == stopNode:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(n)
            path.reverse()
            return path

        for node, weight in getNeighbors(n):
            parents[node] = n

            if node not in [openList, closedList]:
                openList.append(node)
                g[node] = g[n] + weight

            else:
                if g[node] > g[n] + weight:
                    g[node] = g[n] + weight
                    if node in closedList:
                        closedList.remove(node)
                        openList.append(node)

        openList.remove(n)
        closedList.append(n)


res = aStar('A', 'G')

if res is None:
    print('No solution exists')
else:
    print('Path found: \n {}'.format(res))
