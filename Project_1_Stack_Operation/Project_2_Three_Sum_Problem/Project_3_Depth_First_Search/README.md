# Depth-First Search (DFS) Implementation

This project implements *Depth-First Search (DFS)* using an adjacency list to traverse a graph starting from a given vertex.

## Problem Statement

Given a graph represented as an adjacency list, implement a DFS traversal starting from a specified vertex. DFS explores as far as possible along each branch before backtracking.

### Example Input Graph

The graph is represented as an adjacency list in Python:

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

