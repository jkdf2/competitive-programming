from sys import stdin
from collections import deque
from heapq import *

def main():
    first_line = stdin.readline().split(" ")
    num_vertices = int(first_line[0])
    num_edges = int(first_line[1])


    # Graph construction - edges
    vertices = dict()
    lines = stdin.readlines()
    for line in lines:
        line = line.split(" ")
        a = int(line[0])
        b = int(line[1])
        cost = int(line[2])
        try:
            vert_a = vertices[a]
        except KeyError:
            vert_a = Vertex(a)
            vertices[a] = vert_a
        try:
            vert_b = vertices[b]
        except KeyError:
            vert_b = Vertex(b)
            vertices[b] = vert_b
        vert_a.edges.append(Edge(vert_a, vert_b, cost))
        vert_b.edges.append(Edge(vert_b, vert_a, cost))

    # All vertices now represented in graph
    try:
        goal = vertices[num_vertices]
    except KeyError:
        # No edges exist to goal
        print(-1)
        return

    heap = []
    root = vertices[1]
    heappush(heap, Edge(root, root, 0))

    # now we try to get from root to goal
    while len(heap) > 0:
        cur_edge = heappop(heap)
        if cur_edge.to_vertex == goal:
            path = deque([cur_edge.to_vertex.name])
            parent_vertex = cur_edge.parent
            while parent_vertex != root:
                path.appendleft(parent_vertex.name)
                parent_vertex = parent_vertex.parent
            path.appendleft(root.name)
            print(" ".join(str(name) for name in path))
            return
        if not cur_edge.to_vertex.visited:
            cur_edge.to_vertex.visited = True
            cur_edge.to_vertex.parent = cur_edge.parent
            for neighbor_edge in cur_edge.to_vertex.edges:
                if not neighbor_edge.to_vertex.visited:
                    heappush(heap, Edge(neighbor_edge.parent, neighbor_edge.to_vertex,
                                cur_edge.cost + neighbor_edge.cost))

    # Failed to find goal
    print(-1)

class Vertex:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.edges = []
        self.parent = None

    def __eq__(self, other):
        try:
            return self.name == other.name
        except:
            return False

    def __repr__(self):
        return "Vertex {} with {} neighbors".format(self.name, len(self.edges))

class Edge:
    def __init__(self, parent, to_vertex, cost):
        self.parent = parent
        self.to_vertex = to_vertex
        self.cost = cost

    def __eq__(self, other):
        try:
            return self.cost == other.cost
        except:
            return False

    def __repr__(self):
        return "Edge from vertex {} to vertex {} with cost {}".format(self.parent.name, self.to_vertex.name, self.cost)

    def __gt__(self, other):
        return self.cost > other.cost

main()
