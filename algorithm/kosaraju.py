## Kosaraju Algorithm
## Use to find strongly connected component in directed graph
## 1-indexed

N = 7 # N-1 nodes

def add_edge(graph, u, v):
    graph[u].append(v)

def reverse_graph(graph):
    r_graph = [[] for _ in range(N)]
    for u in range(1, N):
        for v in graph[u]:
            r_graph[v].append(u)
    return r_graph

def dfs(graph, u, res, visited):
    visited[u] = True
    res.append(u)
    for v in graph[u]:
        if not visited[v]:
            dfs(graph, v, res, visited)

def rdfs(graph, u, res, visited):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            rdfs(graph, v, res, visited)
    res.append(u)

def get_order(graph):
    visited = [False for _ in range(N)]
    reverse_order = []
    for idx in range(1, N):
        if not visited[idx]:
            rdfs(graph, idx, reverse_order, visited)
    return reverse_order[::-1]

def get_components(graph, order):
    visited = [False for _ in range(N)]
    components = []
    for idx in order:
        if not visited[idx]:
            tmp = []
            dfs(graph, idx, tmp, visited)
            components.append(tmp)
    return components

def build_graph(N):
    graph = [[] for _ in range(N)]
    add_edge(graph, 1, 3)
    add_edge(graph, 1, 2)
    add_edge(graph, 2, 4)
    add_edge(graph, 3, 4)
    add_edge(graph, 3, 5)
    add_edge(graph, 4, 1)
    add_edge(graph, 4, 6)
    add_edge(graph, 5, 6)
    return graph

def main():
    graph = build_graph(N) # [[], [3, 2], [4], [4, 5], [1, 6], [6], []]
    r_graph = reverse_graph(graph)
    order = get_order(r_graph)
    components = get_components(graph, order)
    print(components)

if __name__ == "__main__":
    main() # [[6], [5], [1, 3, 4, 2]] -> 3 components -> [6], [5], [1, 3, 4, 2]
