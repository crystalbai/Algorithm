import collections
from heapq import *
def dijkstra(graph, start, end):
    vertices, edges = graph['vertices'], graph['edges']
    edges = list(edges)
    edges.sort()
    visited = set(start)
    adj = collections.defaultdict(list)
    dis = {}
    for i in edges:
        adj[i[1]].append(i[2])
        adj[i[2]].append(i[1])
        dis[(i[1], i[2])] =i[0]
        dis[(i[2], i[1])] = i[0]
    st = []
    for i in adj[start]:
        heappush(st,(dis[(start, i)], i))

    res = []
    while len(st)!= 0:
        node = heappop(st)
        if node[1] == end:
            return res, node[0]
        while len(st)>0 and node[1] in visited:
            node = heappop(st)
        if node[1] not in visited:
            res.append(node[1])
            visited.add(node[1])

            for e in adj[node[1]]:
                heappush(st, (node[0]+dis[(node[1],e)], e))



    return False






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
print dijkstra(graph, 'A', 'D')
