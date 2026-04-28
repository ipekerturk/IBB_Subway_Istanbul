# Final Project Report
## Comparative Algorithm Design and Complexity Analysis

## 1. Problem Description

The objective of this project is to efficiently answer shortest path queries on weighted graphs.

We modeled the Istanbul subway transportation network as a weighted graph where:

- Stations represent vertices
- Connections between stations represent edges
- Travel times (minutes) represent weights

The goal is to compare multiple shortest path algorithms and evaluate their efficiency under different assumptions and design strategies.

---

## 2. Dataset Description

The dataset was created using real Istanbul metro and railway inspired transportation connections.

Included lines:

- M2 Metro Line
- M4 Metro Line
- Marmaray Line
- Transfer stations between systems

This creates a realistic weighted transportation graph suitable for route optimization problems.

---

## 3. Graph Representation

We selected Adjacency List as the main graph representation.

### Why Adjacency List?

Advantages:

- Memory efficient for sparse graphs
- Fast traversal of neighboring stations
- Well suited for BFS and Dijkstra algorithms
- Easier to scale for larger transportation networks

Example:

Yenikapi -> [(Vezneciler,3), (Yenikapi-M,2)]

---

## 4. Implemented Algorithms

### 4.1 Breadth-First Search (BFS)

Used to find the route with the minimum number of stations.

Characteristics:

- Ignores edge weights
- Fast traversal
- Good when station count matters more than travel time

### 4.2 Dijkstra Algorithm

Used to find the fastest route using travel times.

Characteristics:

- Uses priority queue
- Handles positive weighted graphs efficiently
- Produces optimal shortest-time route

### 4.3 Floyd-Warshall Algorithm

Used to compute shortest paths between all station pairs.

Characteristics:

- Heavy preprocessing cost
- Very fast repeated shortest-path queries
- Useful when many route requests exist

---

## 5. Complexity Analysis

| Algorithm | Time Complexity | Space Complexity |
|----------|-----------------|------------------|
| BFS | O(V + E) | O(V) |
| Dijkstra | O((V + E) log V) | O(V) |
| Floyd-Warshall | O(V^3) | O(V^2) |

Where:

- V = number of vertices (stations)
- E = number of edges (connections)

---

## 6. Experimental Results

The system was extended with an interactive user input interface.

Users can enter any valid start and destination stations from the dataset, and the program computes routes dynamically.

Example usage:

Start station: Yenikapi  
Destination station: Levent

Observed outputs:

- BFS found the route with minimum number of stations.
- Dijkstra found the fastest route in minutes.
- Floyd-Warshall confirmed the shortest weighted distance.

Runtime measurements were collected for each algorithm and compared.

Example runtime comparison:

| Algorithm | Runtime (seconds) |
|----------|-------------------|
| BFS | Very Low |
| Dijkstra | Low |
| Floyd-Warshall | Higher (preprocessing) |
---

## 7. Comparative Discussion

### BFS

Best when:

- Edge weights are unimportant
- Minimum station count is preferred
- Fast simple traversal is needed

### Dijkstra

Best when:

- Realistic route planning is required
- Travel times matter
- Single-query shortest path is needed

### Floyd-Warshall

Best when:

- Many repeated shortest-path queries exist
- Preprocessing time is acceptable
- Instant future queries are desired

---

## 8. Trade-Off Analysis

This project demonstrates several important algorithmic trade-offs.

### Preprocessing Time vs Query Time

- Dijkstra computes routes on demand.
- Floyd-Warshall performs expensive preprocessing but answers future queries faster.

### Memory Usage vs Speed

- BFS and Dijkstra use lower memory.
- Floyd-Warshall stores a full distance matrix.

### Simplicity vs Optimal Weighted Routing

- BFS is simpler but ignores weights.
- Dijkstra is more advanced and more realistic.

---

## 9. Conclusion

This project showed that no single algorithm is optimal for every scenario.

- BFS is simple and efficient for unweighted or station-count problems.
- Dijkstra is the most practical solution for transportation route planning.
- Floyd-Warshall is powerful when many repeated queries are required.

Therefore, algorithm selection should depend on system requirements, graph size, memory limits, and query frequency.

---

## 10. Final Evaluation

By implementing and comparing multiple algorithms on the same real-world graph dataset, we gained practical understanding of:

- Graph modeling
- Complexity analysis
- Experimental benchmarking
- Algorithm design trade-offs
- Real-life route optimization systems