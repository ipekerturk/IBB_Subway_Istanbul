def floyd_warshall(graph):
    stations = list(graph.keys())
    n = len(stations)

    index = {stations[i]: i for i in range(n)}

    dist = [[float("inf")] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u in graph:
        for v, weight in graph[u]:
            i = index[u]
            j = index[v]
            dist[i][j] = weight

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist, stations, index