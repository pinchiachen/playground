def BFS(graph, s):
    queue = []
    queue.append(s)
    nodeSet = set()
    nodeSet.add(s)
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in nodeSet:
                queue.append(node)
                nodeSet.add(node)
        print(vertex)

if __name__ == "__main__":
    graph = {
        'a': ['b', 'c'],
        'b': ['a', 'c', 'd'],
        'c': ['a', 'b', 'd', 'e'],
        'd': ['b', 'c', 'e', 'f'],
        'e': ['c', 'd'],
        'f': ['d'],
    }

    BFS(graph, 'a')