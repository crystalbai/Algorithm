parent = dict()
rank = dict()

def find(v):
    while parent[v] != v:
        parent[v] = parent[parent[v]]
        v = parent[v]
    return v
def makeset(vertice):
    parent[vertice] = vertice

def union(v1, v2):
    r1 = find(v1)
    r2 = find(v2)
    if r1 != r2:
        # if rank[r1]> rank[r2]:
        #     parent[v2] = v1
        # else:
        #     parent[v1] = v2
        #     if rank[r1] == rank[r2]:
        #         rank[v2]+=1
        parent[r2] = r1

def kruskal(graph):
    for v in graph['vertices']:
        makeset(v)

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for e in edges:
        weight, v1, v2 = e
        if find(v1)!= find(v2):
            union(v1, v2)
            minimum_spanning_tree.add(e)
    return minimum_spanning_tree


graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
        'edges': set([
            (1, 'A', 'B'),
            (5, 'A', 'C'),
            (3, 'A', 'D'),
            (4, 'B', 'C'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
        }
minimum_spanning_tree = set([
            (1, 'A', 'B'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
print kruskal(graph)
