import networkx as nx
G1 = nx.Graph()
edges = [
    (0, 1), (0, 2), (1, 2),
    (3, 4), (4, 5), (5, 3),
    (6, 7), (7, 8), (8, 9), (6, 9)
]
G1.add_edges_from(edges)


print(" Задача 1 ")
print(f"1) Число вершин: {G1.number_of_nodes()}")
print(f"   Число ребер: {G1.number_of_edges()}")

components = list(nx.connected_components(G1))
largest_comp = max(components, key=len)
G_largest = G1.subgraph(largest_comp)

if nx.is_connected(G_largest):
    radius = nx.radius(G_largest)
    diameter = nx.diameter(G_largest)
    print(f"2) Главная компонента (вершин: {len(largest_comp)})")
    print(f"   Радиус: {radius}")
    print(f"   Диаметр: {diameter}")

print("3) Кратчайшие пути (первые 5 пар):")
all_paths_lengths = dict(nx.all_pairs_shortest_path_length(G1))

count = 0
for source, targets in all_paths_lengths.items():
    for target, length in targets.items():
        if source < target:
            print(f"   {source} -> {target}: {length}")
            count += 1
            if count >= 5:
                break
    if count >= 5:
        break
  import networkx as nx


G2 = nx.Graph()
edges = [
    (0, 1), (1, 2), (2, 0), 
    (3, 4),                 
    (5, 6), (6, 7), (5, 7)  
]
G2.add_edges_from(edges)

G2.add_node(8)


print(" Задача 2 ")
density = nx.density(G2)
components_count = nx.number_connected_components(G2)
print(f"1) Плотность графа: {density:.4f}")
print(f"   Число связных компонент: {components_count}")

source_vertex = 0
dfs_parents = dict(nx.dfs_predecessors(G2, source=source_vertex))
print(f"2) Словарь предшественников при DFS из вершины {source_vertex}:")
print(f"   {dfs_parents}")

K5 = nx.complete_graph(5)  
all_paths_2_to_4 = list(nx.all_simple_paths(K5, source=2, target=4))
print(f"3) Полносвязный граф K5: {K5.number_of_nodes()} вершин, {K5.number_of_edges()} ребер")
print(f"   Все простые пути из вершины 2 в вершину 4 (всего {len(all_paths_2_to_4)}):")
for path in all_paths_2_to_4:
    print(f"   {path}")
