# 🚇 Istanbul Subway Shortest Path Analysis

This project analyzes and compares multiple shortest-path algorithms on a subway network dataset.

---

## 📌 Problem Description
The goal of this project is to efficiently answer shortest-path queries on a graph structure.

We explore how different algorithmic approaches affect:
- Execution time
- Memory usage
- Scalability

---

## 🧠 Algorithms Implemented

### 1. BFS (Breadth-First Search)
- Used for unweighted graphs
- Finds shortest path based on number of edges

### 2. Dijkstra’s Algorithm
- Works with weighted graphs
- Uses priority queue for optimal path finding

### 3. Floyd-Warshall Algorithm
- Computes shortest paths between all node pairs
- Uses dynamic programming approach

---

## ⚙️ Graph Representation
- Adjacency List is used for efficient storage and traversal

---

## 📊 Complexity Analysis

| Algorithm         | Time Complexity        | Space Complexity |
|------------------|----------------------|------------------|
| BFS              | O(V + E)             | O(V)             |
| Dijkstra         | O((V + E) log V)     | O(V)             |
| Floyd-Warshall   | O(V³)                | O(V²)            |

---

## 🧪 Experimental Results

| Algorithm         | Runtime (seconds) |
|------------------|------------------|
| BFS              | 0.00002          |
| Dijkstra         | 0.00005          |
| Floyd-Warshall   | 0.00120          |

---

## 🔍 Analysis & Discussion

- BFS is the fastest algorithm since it does not consider weights.
- Dijkstra is slightly slower due to priority queue operations.
- Floyd-Warshall is significantly slower because it computes all-pairs shortest paths with O(V³) complexity.

For small graphs, all algorithms perform efficiently.  
However, as graph size increases:
- Floyd-Warshall becomes impractical
- Dijkstra provides a good balance
- BFS is only suitable for unweighted graphs

---

## 📂 Project Structure

algorithm_final_project/
│
├── algorithms/        
├── data/              
├── graph/             
├── utils/             
├── main.py            
├── report.md          
└── README.md          

---

## ▶️ How to Run

python main.py

---

## 🎯 Learning Outcomes

This project demonstrates:
- Designing multiple algorithms for the same problem
- Understanding time vs space trade-offs
- Comparing theoretical vs experimental performance
- Making algorithmic decisions based on constraints