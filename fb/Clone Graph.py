# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.m = dict()
    def cloneGraph(self, node):
        if node == None:
            return None
        res = UndirectedGraphNode(node.label)
        if node.label in self.m.keys():
            return self.m[node.label]
        self.m[node.label] = res
        for i in node.neighbors:
            res.neighbors.append(self.cloneGraph(i))

        return res