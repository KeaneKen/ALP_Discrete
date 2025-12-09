from Graf import Graf
graph = Graf()

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
# pos = nx.spring_layout(graph)
# nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16)
# labels = nx.get_edge_attributes(graph, 'weight')
# nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
# plt.show()
graph.visualize_graph()

# Derajat setiap simpul
degrees = graph.get_degrees()
print(f"\nDerajat setiap simpul: {degrees}")

# Cek siklus
print(f"\nApakah graf memiliki siklus? {graph.has_cycle()}")

# Cek konektivitas
print(f"Apakah graf terhubung? {graph.is_connected()}")

# Informasi siklus
cycle = graph.get_cycle_info()
print(f"Siklus dalam graf: {cycle if cycle else 'Tidak ada siklus'}")