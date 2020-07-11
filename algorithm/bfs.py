def bfs(graph, s):
    queue = []
    queue.append(s)
    node_set = set()
    node_set.add(s)
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in node_set:
                queue.append(node)
                node_set.add(node)
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

    bfs(graph, 'a')