from collections import deque

def bfs(graph, start, target):
    queue = deque()
    queue.append((start, [start]))

    visited = set()

    while queue:
        current_station, path = queue.popleft()

        if current_station == target:
            return path

        if current_station not in visited:
            visited.add(current_station)

            for neighbor, weight in graph[current_station]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None