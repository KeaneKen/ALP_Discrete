from Graf import Graf
# Define the weighted graph
graph = Graf()

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


graph.visualize_graph()

# b. Breadth-First Search (BFS) dari simpul A
print("\n" + "=" * 50)
print("b. BREADTH-FIRST SEARCH (BFS) DARI SIMPUL A")
print("=" * 50)

bfs_result = graph.bfs('A')
print(f"Urutan kunjungan BFS: {' -> '.join(bfs_result)}")

# c. Depth-First Search (DFS) dari simpul A (rekursif, urutan tetangga berdasarkan alfabet)
print("\n" + "=" * 50)
print("c. DEPTH-FIRST SEARCH (DFS) DARI SIMPUL A (REKURSIF)")
print("=" * 50)

dfs_result = graph.dfs('A')
print(f"Urutan kunjungan DFS: {' -> '.join(dfs_result)}")

# # d. Algoritma Dijkstra dari simpul A
print("\n" + "=" * 50)
print("d. ALGORITMA DIJKSTRA DARI SIMPUL A")
print("=" * 50)

# # 1. Jarak minimum dari A ke seluruh simpul
distances = graph.dijkstra_distances('A')
print("\n1. Jarak minimum dari A ke seluruh simpul:")
for vertex in sorted(distances.keys()):
    print(f"   A -> {vertex}: {distances[vertex]}")

# 2. Jalur terpendek dari A ke G
shortest_path = graph.shortest_path('A', 'G')
shortest_distance = graph.shortest_distance('A', 'G')
print(f"\n2. Jalur terpendek dari A ke G:")
print(f"   Path: {' -> '.join(shortest_path)}")
print(f"   Total jarak: {shortest_distance}")

# Visualisasi jalur terpendek A ke G
graph.visualize_shortest_path('A', 'G')

print("\n" + "=" * 50)
print("SELESAI!")
print("=" * 50)
