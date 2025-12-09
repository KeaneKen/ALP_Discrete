from Graf import Graf

G = Graf()

# Nodes
G.add_node(1)
G.add_node(2)   
G.add_node(3)   
G.add_node(4)   
G.add_node(5)   

# Edges
G.add_edge(1, 2, weight=4.5)
G.add_edge(1, 3, weight=3.2)
G.add_edge(2, 4, weight=2.7)
G.add_edge(3, 4, weight=1.8)
G.add_edge(1, 4, weight=6.7)
G.add_edge(3, 5, weight=2.7)

#Visualisasi
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16)
# labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# plt.show()
G.visualize_graph()

#Jalur Terpendek
# shortest = nx.shortest_path(G, source=1, target=5, weight='weight')
# print(f"Jalan terpendek dari 1 ke 5: {shortest}")
print(G.shortest_path(1, 5))

#Visualisasi jalur terpendek
# edges_in_path = [(shortest[i], shortest[i+1]) for i in range(len(shortest)-1)]
# nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16)
# nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='red', width=3)
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# plt.show()
G.visualize_shortest_path(1, 5)

# degrees = G.get_degrees()
# print(f"\nSemua derajat : {degrees}")

# print(f"\nApakah graf memiliki siklus? {G.has_cycle()}")
# print(f"Apakah graf terhubung? {G.is_connected()}")

# cycle = G.get_cycle_info()
# if cycle:
#     print(f"Siklus ditemukan: {cycle}")
# else:
#     print("Tidak ada siklus dalam graf")
