import collections
from heapq import *
def prime(graph):
    vertices, edges = graph['vertices'], graph['edges']
    edges = list(edges)
    edges.sort()
    visited = set([edges[0][1]])
    adj = collections.defaultdict(list)
    dis = {}
    for i in edges:
        adj[i[1]].append(i[2])
        adj[i[2]].append(i[1])
        dis[(i[1], i[2])] =i[0]
        dis[(i[2], i[1])] = i[0]
    st = [edges[0]]
    for e in adj[edges[0][1]]:
        heappush(st, (dis[edges[0][1], e], edges[0][1], e))

    res = []
    while st!= 0:

        node = heappop(st)
        while len(st) > 0 and node[2] in visited:
            node = heappop(st)
        if len(st) == 0 and node[2] in visited:
            return res
        visited.add(node[2])
        res.append(node)
        for e in adj[node[2]]:
            heappush(st, (dis[node[2], e], node[2], e))

    return res






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
print prime(graph)
