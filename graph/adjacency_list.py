def load_graph(filename):
    graph = {}

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            parts = line.split()

            source = parts[0]
            destination = parts[1]
            weight = int(parts[2])

            if source not in graph:
                graph[source] = []

            if destination not in graph:
                graph[destination] = []

            graph[source].append((destination, weight))
            graph[destination].append((source, weight))

    return graph