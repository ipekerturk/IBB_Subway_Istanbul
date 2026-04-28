# Istanbul Subway Shortest Path Analysis

This project compares multiple shortest path algorithms on the Istanbul subway network using real station connection data.

## Project Goal

To analyze how different algorithmic approaches perform on weighted graph shortest path queries.

## Graph Representation

- Adjacency List

## Algorithms Implemented

1. BFS  
   - Finds route with minimum number of stations

2. Dijkstra  
   - Finds fastest route using travel times

3. Floyd-Warshall  
   - Precomputes all-pairs shortest paths for fast repeated queries

## Dataset

Real Istanbul subway inspired station connections:

- Metro lines
- Marmaray
- Transfer stations

## Example Query

```text
Yenikapi -> Levent