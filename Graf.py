import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Graf:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node):
        return self.graph.add_node(node)
    
    def add_nodes_from(self, nodeList):
        return self.graph.add_nodes_from(nodeList)

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
    
    def shortest_distance(self, source, target):
        return nx.shortest_path_length(self.graph, source, target, weight='weight')
    
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
    
    def bfs(self, start):
        visited = []
        queue = deque([start])
        visited_set = {start}
        
        while queue:
            vertex = queue.popleft()
            visited.append(vertex)
            
            # Get neighbors and sort alphabetically
            neighbors = sorted(self.graph.neighbors(vertex))
            for neighbor in neighbors:
                if neighbor not in visited_set:
                    visited_set.add(neighbor)
                    queue.append(neighbor)
        
        return visited
    
    def dfs(self, start, visited=None):
        if visited is None:
            visited = []
        
        visited.append(start)
        
        # Get neighbors and sort alphabetically
        neighbors = sorted(self.graph.neighbors(start))
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
        
        return visited
    
    def dijkstra_distances(self, source):
        return nx.single_source_dijkstra_path_length(self.graph, source, weight='weight')