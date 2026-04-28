from graph.adjacency_list import load_graph
from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra
from algorithms.floyd_warshall import floyd_warshall
from utils.benchmark import measure_runtime

# graph yükle
graph = load_graph("data/istanbul_subway.txt")

# kullanıcıdan input al
start = input("Enter start station: ")
target = input("Enter target station: ")

# istasyon kontrolü
if start not in graph or target not in graph:
    print("Station name not found!")
else:
    print("\n===== QUERY =====")
    print(start, "->", target)

    # BFS
    (bfs_route, bfs_time) = measure_runtime(bfs, graph, start, target)

    print("\n=== BFS ===")
    print("Route:", " -> ".join(bfs_route))
    print("Stations:", len(bfs_route) - 1)
    print("Runtime:", bfs_time)

    # Dijkstra
    ((cost, route), dij_time) = measure_runtime(dijkstra, graph, start, target)

    print("\n=== Dijkstra ===")
    print("Route:", " -> ".join(route))
    print("Time:", cost, "minutes")
    print("Runtime:", dij_time)

    # Floyd-Warshall
    ((dist, stations, index), fw_time) = measure_runtime(floyd_warshall, graph)

    shortest_time = dist[index[start]][index[target]]

    print("\n=== Floyd-Warshall ===")
    print("Shortest Time:", shortest_time, "minutes")
    print("Runtime:", fw_time)

    # tablo
    print("\n=== Runtime Table ===")
    print("{:<20} {:<15}".format("Algorithm", "Runtime"))
    print("-" * 35)
    print("{:<20} {:<15.6f}".format("BFS", bfs_time))
    print("{:<20} {:<15.6f}".format("Dijkstra", dij_time))
    print("{:<20} {:<15.6f}".format("Floyd-Warshall", fw_time))

