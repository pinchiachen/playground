def dijkstra(matrix, n, start):
    # Initialize book
    book = [0] * (n + 1) # 1-indexed
    book[start] = 1

    # Initialize dis
    dis = [0] * (n + 1) # 1-indexed
    for end in range(1, n+1):
        dis[end] = 0 if end == start else matrix[start][end]

    # Dijkstra algorithm
    for _ in range(n-1):
        # Find unbook edge u which is nearest to start vertex
        min_dis = float('inf')
        u = -1
        for vertex in range(1, n+1):
            if book[vertex] == 0 and dis[vertex] < min_dis:
                u = vertex
                min_dis = dis[vertex]
        if u == -1: break
        book[u] = 1
        # Update dis[v]
        for v in range(1, n+1):
            if matrix[u][v] == float('inf'): continue
            dis[v] = min(dis[v], dis[u] + matrix[u][v])
    return dis

if __name__ == "__main__":
    inf = float('inf')
    matrix = [
        [ inf, inf, inf, inf, inf, inf, inf ],
        [ inf, 0,   1,   12,  inf, inf, inf ],
        [ inf, inf, 0,   9,   3,   inf, inf ],
        [ inf, inf, inf, 0,   inf, 5,   inf ],
        [ inf, inf, inf, 4,   0,   13,  15  ],
        [ inf, inf, inf, inf, inf, 0,   4   ],
        [ inf, inf, inf, inf, inf, inf, 0   ],
    ] # 1-indexed
    n = 6
    start = 1
    print(dijkstra(matrix, n, start))