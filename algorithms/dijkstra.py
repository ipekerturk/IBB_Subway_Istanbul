import heapq

def dijkstra(graph, start, target):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))

    visited = set()

    while priority_queue:
        current_time, current_station, path = heapq.heappop(priority_queue)

        if current_station == target:
            return current_time, path

        if current_station in visited:
            continue

        visited.add(current_station)

        for neighbor, weight in graph[current_station]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (current_time + weight, neighbor, path + [neighbor])
                )

    return None, None