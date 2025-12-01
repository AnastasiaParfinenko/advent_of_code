import networkx as nx

def find_triangles_from_edges(graph):
    triangles = set()

    for u in graph.nodes:
        neighbors = set(graph.neighbors(u))
        for v in neighbors:
            for w in neighbors:
                if v != w and graph.has_edge(v, w):
                    triangles.add(tuple(sorted([u, v, w])))

    return triangles


def find_largest_clique(graph):
    return sorted(max(nx.find_cliques(graph), key=len))


def part12():
    with open('input23.txt', 'r') as file:
        edges = [line.strip().split('-') for line in file]

    graph = nx.Graph()
    graph.add_edges_from(edges)

    triangles = find_triangles_from_edges(graph)
    triangles_t = sum(any(word.startswith('t') for word in triangle)  for triangle in triangles)
    print(triangles_t)

    largest_clique = find_largest_clique(graph)
    print(','.join(largest_clique))


part12()
