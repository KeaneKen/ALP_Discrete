import networkx as nx
import matplotlib.pyplot as plt

class Graf:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node):
        return self.graph.add_node(node)

    def add_edge(self, origin, dest, weight=None):
        if weight is None:
            return self.graph.add_edge(origin, dest)
        else:
            return self.graph.add_edge(origin, dest, weight=weight)

    def visualize_graph(self):
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.show()

    def shortest_path(self, source, target):
        return nx.shortest_path(self.graph, source, target, weight='weight')
    
    def visualize_shortest_path(self, source, target):
        pos = nx.spring_layout(self.graph)
        path = self.shortest_path(source, target)
        edges_in_path = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16)
        nx.draw_networkx_edges(self.graph, pos, edgelist=edges_in_path, edge_color='red', width=3)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.show()
        
    def get_degrees(self):
        return dict(self.graph.degree())
    
    def has_cycle(self):
        try:
            nx.find_cycle(self.graph)
            return True
        except nx.NetworkXNoCycle:
            return False

    def is_connected(self):
        return nx.is_connected(self.graph)
    
    def get_cycle_info(self):
        if self.has_cycle():
            try:
                cycle = nx.find_cycle(self.graph)
                return cycle
            except nx.NetworkXNoCycle:
                return None
        return None