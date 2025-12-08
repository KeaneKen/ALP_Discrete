import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()

# Nodes - use strings for node names
graph.add_node('A')
graph.add_node('B')   
graph.add_node('C')   
graph.add_node('D')   
graph.add_node('E')   
graph.add_node('F') 

# Edges - use strings for node names
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'E')
graph.add_edge('D', 'E')
graph.add_edge('E', 'F')
graph.add_edge('C', 'F')

# Visualisasi
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16)
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
plt.show()

# Jalur Terpendek
shortest = nx.shortest_path(graph, source='A', target='F')
print(f"Shortest path from A to F: {shortest}")

# Visualisasi jalur terpendek
edges_in_path = [(shortest[i], shortest[i+1]) for i in range(len(shortest)-1)]
nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16)
nx.draw_networkx_edges(graph, pos, edgelist=edges_in_path, edge_color='red', width=3)
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
plt.show()

# Derajat setiap simpul
degrees = dict(graph.degree())
print(f"\nSemua derajat: {degrees}")