"""
=============================================================================
COCS-221: Computer Science B | Lab 7: BST, Searching & Sorting, and Dijkstra
Task 3: Route Optimization Dijkstra's Algorithm (Student Solution)
=============================================================================
YOUR TASKS:
1. Implement `dijkstra(graph, start, end)` using Python's `heapq` library.
2. Implement the NetworkX & Matplotlib visualization script to plot the campus
   map and highlight the shortest path from 'Library' to 'Gym'.
=============================================================================
"""

import heapq
import networkx as nx
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Campus Graph Definition
# -----------------------------------------------------------------------------
graph = {
    "Library": {"Cafeteria": 200, "Lecture Hall": 150},
    "Cafeteria": {"Library": 200, "Gym": 300},
    "Lecture Hall": {"Library": 150, "Dorm": 100},
    "Gym": {"Cafeteria": 300},
    "Dorm": {"Lecture Hall": 100}
}


# -----------------------------------------------------------------------------
# 1. DIJKSTRA SHORTEST ROUTE IMPLEMENTATION
# -----------------------------------------------------------------------------
def dijkstra(graph, start, end):
    """
    Computes the shortest path and total distance from start to end 
    using Dijkstra's algorithm with a priority queue (heapq).
    """
    # Initialize distances with infinity and predecessors with None
    distances = {node: float('inf') for node in graph}
    previous_nodes = {node: None for node in graph}
    distances[start] = 0

    # Priority queue stores tuples of (current_distance, current_node)
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # If a shorter path to current_node was already found, skip
        if current_distance > distances[current_node]:
            continue

        # If we reached our destination, we can stop early
        if current_node == end:
            break

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Found a shorter path to neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    # Reconstruct the shortest path from end to start
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]

    return path, distances[end]


# -----------------------------------------------------------------------------
# 2. GRAPH VISUALIZATION WITH NETWORKX & MATPLOTLIB
# -----------------------------------------------------------------------------
def visualize_campus_map(graph, shortest_path):
    """
    Plots the campus map, adds edge weights, and highlights the shortest path.
    """
    G = nx.Graph()

    # Add edges and weights to NetworkX graph
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    # Define fixed 2D coordinate positions for campus locations
    pos = {
        "Library": (0, 0),
        "Cafeteria": (1, 0),
        "Lecture Hall": (0, 1),
        "Gym": (1, 1),
        "Dorm": (2, 1)
    }

    plt.figure(figsize=(8, 6))
    plt.title("Campus Map Network Visualization & Optimal Shortest Route (500m)", fontsize=12, fontweight='bold')

    # Draw all base nodes (light blue circles)
    nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='skyblue', edgecolors='black')

    # Draw all base edges (gray lines)
    nx.draw_networkx_edges(G, pos, width=2, edge_color='gray')

    # Draw node labels (bold names)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

    # Draw edge weight labels (distances in meters)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

    # Highlight shortest path edges and nodes in red
    path_edges = list(zip(shortest_path[:-1], shortest_path[1:]))

    nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_size=3000, node_color='lightcoral',
                           edgecolors='darkred')
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color='red')

    plt.axis('off')
    plt.tight_layout()
    plt.show()


# =============================================================================
# TEST HARNESS
# =============================================================================
if __name__ == "__main__":
    start_node = "Library"
    end_node = "Gym"

    # Compute shortest route
    path, total_distance = dijkstra(graph, start_node, end_node)

    # Print Terminal Output
    print(f"The shortest Path from {start_node} to {end_node} = {path}, Total Distance = {total_distance} meters")

    # Run visualization (Requires: pip install networkx matplotlib)
    visualize_campus_map(graph, path)