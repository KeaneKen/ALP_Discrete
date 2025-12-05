import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()

# Nodes
graph.add_node(1)
graph.add_node(2)   
graph.add_node(3)   
graph.add_node(4)   
graph.add_node(5)   

# Edges
graph.add_edge(1, 2, weight=4.5)
graph.add_edge(1, 3, weight=3.2)
graph.add_edge(2, 4, weight=2.7)
graph.add_edge(3, 4, weight=1.8)
graph.add_edge(1, 4, weight=6.7)
graph.add_edge(3, 5, weight=2.7)

#Visualisasi
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16)
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
plt.show()

#Jalur Terpendek
shortest = nx.shortest_path(graph, source=1, target=5, weight='weight')
print(f"Jalan terpendek dari 1 ke 5: {shortest}")

#Visualisasi jalur terpendek
edges_in_path = [(shortest[i], shortest[i+1]) for i in range(len(shortest)-1)]
nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16)
nx.draw_networkx_edges(graph, pos, edgelist=edges_in_path, edge_color='red', width=3)
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
plt.show()