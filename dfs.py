def DFS(graph, s):
    stack = []
    stack.append(s)
    nodeSet = set()
    nodeSet.add(s)
    while len(stack) > 0:
        vertex = stack.pop()
        nodes = graph[vertex]
        for node in nodes:
            if node not in nodeSet:
                stack.append(node)
                nodeSet.add(node)
        print(vertex)

def recursiveDFS(graph, s, queue=[]):
    queue.append(s)
    for i in graph[s]:
        if i not in queue:
            recursiveDFS(graph, i, queue)
    return queue

if __name__ == "__main__":
    graph = {
        'a': ['b', 'c'],
        'b': ['a', 'c', 'd'],
        'c': ['a', 'b', 'd', 'e'],
        'd': ['b', 'c', 'e', 'f'],
        'e': ['c', 'd'],
        'f': ['d'],
    }

    DFS(graph, 'a')

    print(recursiveDFS(graph, 'a'))