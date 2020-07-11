def dfs(graph, s):
    stack = []
    stack.append(s)
    node_set = set()
    node_set.add(s)
    while len(stack) > 0:
        vertex = stack.pop()
        nodes = graph[vertex]
        for node in nodes:
            if node not in node_set:
                stack.append(node)
                node_set.add(node)
        print(vertex)

def recursive_dfs(graph, s, queue=[]):
    queue.append(s)
    for i in graph[s]:
        if i not in queue:
            recursive_dfs(graph, i, queue)
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

    dfs(graph, 'a')

    print(recursive_dfs(graph, 'a'))