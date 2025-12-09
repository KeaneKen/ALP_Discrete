# ALP Matemarika Diskrit - Teori Graf

## Overview
Projek ini merupakan bentuk implementasi teori graf dalam Python. Beberapa operasi dari teori tersebut telah diubah menjadi *methods* yang siapa digunakan untuk melakukan beberapa operasi dalam teori graf. Semua *method* ini digabung dalam sebuah class `Graf` yang pada dasarnya menggunakan library lain, yaitu *etworkX*, *matplotlib.pyplot*, dan *deque*.

## Class Methods

### `__init__`
Sebagai inisialisasi untuk sebuah variabel menjadi objek *networkX* agar bisa diproses sebagai graf.
```
graph = Graf()
```

### `add_node`
Digunakan untuk menambah sebuah *node*, atau titik, atau simpul dalam sebuah Graf. Semua simpul **harus dalam tipe data yang sama** agar berkeja.
```
G = Graf()

# Nodes angka
G.add_node(1)
G.add_node(2)   
G.add_node(3)   


graph = Graf()

# Nodes huruf
graph.add_node('A')
graph.add_node('B')   
graph.add_node('C')
```

### `add_nodes_from`
Sama seperti *method* sebelumnya, tetapi jika mau menyimpan semua simpulnya dalam sebuah list terdahulu. *Method* ini akan menambah semua simpul dari list
```
graph = Graf()

# Vertices
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
graph.add_nodes_from(vertices)
```

### `add_edge`
[Description]

### `visualize_graph`
[Description]

### `shortest_path`
[Description]

### `shortest_distance`
[Description]

### `visualize_shortest_path`
[Description]

### `get_degrees`
[Description]

### `has_cycle`
[Description]

### `is_connected`
[Description]

### `get_cycle_info`
[Description]

### `bfs`
[Description]

### `dfs`
[Description]

### `dijkstra_distances`
[Description]


## Installation
[Add installation instructions here]

## Anggota Kelompok
1. Andi Tubagus Faatih Keane (0806022410015)
2. Britney Glory Chen (0806022410020)
3. Exsel Octavia Gosal (0806022410003)
4. Keihan Pradika Muzaki (0806022410011)