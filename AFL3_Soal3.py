import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Define the weighted graph
graph = nx.Graph()

# Vertices
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
graph.add_nodes_from(vertices)

# Edges with weights
edges = [
    ('A', 'B', 2),
    ('A', 'C', 5),
    ('B', 'D', 4),
    ('B', 'E', 6),
    ('C', 'F', 3),
    ('D', 'G', 2),
    ('E', 'F', 4),
    ('F', 'G', 1)
]

for u, v, weight in edges:
    graph.add_edge(u, v, weight=weight)

# a. Gambarkan Grafnya (Visualize the Graph)
print("=" * 50)
print("a. VISUALISASI GRAF")
print("=" * 50)

pos = nx.spring_layout(graph, seed=42)
plt.figure(figsize=(10, 8))
nx.draw(graph, pos, with_labels=True, node_color='lightblue', 
        node_size=1000, font_size=16, font_weight='bold')
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size=12)
plt.title("Graf Berbobot", fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()
plt.show()

# b. Breadth-First Search (BFS) dari simpul A
print("\n" + "=" * 50)
print("b. BREADTH-FIRST SEARCH (BFS) DARI SIMPUL A")
print("=" * 50)

def bfs(graph, start):
    visited = []
    queue = deque([start])
    visited_set = {start}
    
    while queue:
        vertex = queue.popleft()
        visited.append(vertex)
        
        # Get neighbors and sort alphabetically
        neighbors = sorted(graph.neighbors(vertex))
        for neighbor in neighbors:
            if neighbor not in visited_set:
                visited_set.add(neighbor)
                queue.append(neighbor)
    
    return visited

bfs_result = bfs(graph, 'A')
print(f"Urutan kunjungan BFS: {' -> '.join(bfs_result)}")

# c. Depth-First Search (DFS) dari simpul A (rekursif, urutan tetangga berdasarkan alfabet)
print("\n" + "=" * 50)
print("c. DEPTH-FIRST SEARCH (DFS) DARI SIMPUL A (REKURSIF)")
print("=" * 50)

def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = []
    
    visited.append(start)
    
    # Get neighbors and sort alphabetically
    neighbors = sorted(graph.neighbors(start))
    for neighbor in neighbors:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    
    return visited

dfs_result = dfs_recursive(graph, 'A')
print(f"Urutan kunjungan DFS: {' -> '.join(dfs_result)}")

# d. Algoritma Dijkstra dari simpul A
print("\n" + "=" * 50)
print("d. ALGORITMA DIJKSTRA DARI SIMPUL A")
print("=" * 50)

# 1. Jarak minimum dari A ke seluruh simpul
distances = nx.single_source_dijkstra_path_length(graph, 'A', weight='weight')
print("\n1. Jarak minimum dari A ke seluruh simpul:")
for vertex in sorted(distances.keys()):
    print(f"   A -> {vertex}: {distances[vertex]}")

# 2. Jalur terpendek dari A ke G
shortest_path = nx.shortest_path(graph, 'A', 'G', weight='weight')
shortest_distance = nx.shortest_path_length(graph, 'A', 'G', weight='weight')
print(f"\n2. Jalur terpendek dari A ke G:")
print(f"   Path: {' -> '.join(shortest_path)}")
print(f"   Total jarak: {shortest_distance}")

# Visualisasi jalur terpendek A ke G
print("\nVisualisasi jalur terpendek dari A ke G...")
plt.figure(figsize=(10, 8))
nx.draw(graph, pos, with_labels=True, node_color='lightblue', 
        node_size=1000, font_size=16, font_weight='bold')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size=12)

# Highlight the shortest path
edges_in_path = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]
nx.draw_networkx_edges(graph, pos, edgelist=edges_in_path, 
                       edge_color='red', width=3)
nx.draw_networkx_nodes(graph, pos, nodelist=shortest_path, 
                       node_color='lightcoral', node_size=1000)

plt.title(f"Jalur Terpendek dari A ke G (Jarak: {shortest_distance})", 
          fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()
plt.show()

print("\n" + "=" * 50)
print("SELESAI!")
print("=" * 50)
