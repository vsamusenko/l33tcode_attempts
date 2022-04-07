class Graph:
    def __init__(self, numNodes, edges):
        self.numNodes = numNodes
        self.data = [[] for _ in range(numNodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def removeEdge(self, n1, n2):
        if n1 == n2:
            print('Same Node as input doesn\'t make sense')
        if n1 >= len(self.data) or n2 >= len(self.data):
            print('One of the nodes index is out of range')
        for n in range(len(self.data)):
            if n == n1:
                if n2 in self.data[n]:
                    self.data[n].remove(n2)
            elif n == n2:
                if n1 in self.data[n]:
                    self.data[n].remove(n1)

    def addEdge(self, n1, n2):
        if n1 == n2:
            print('Same Node as input doesn\'t make sense')
        if n1 >= len(self.data) or n2 >= len(self.data):
            print('One of the nodes index is out of range')
        for n in range(len(self.data)):
            if n == n1:
                if n2 not in self.data[n]:
                    self.data[n].append(n2)
            elif n == n2:
                if n1 not in self.data[n]:
                    self.data[n].append(n1)

    def asmatrix(self):
        matrix = [[0] * self.numNodes for _ in range(self.numNodes)]
        for n in range(self.numNodes):
            for neigbours in self.data[n]:
                matrix[n][neigbours] = 1

        return '\n'.join('{}'.format(row) for row in matrix)

    def BFS(self, startnode):
        queue = []
        visited = [None] * self.numNodes
        parent = [None] * self.numNodes
        distance = [0] * self.numNodes

        visited[startnode] = True
        queue.append(startnode)
        idx = 0

        while idx < len(queue):
            current = queue[idx]
            idx += 1
            for neigbour in self.data[current]:
                if not visited[neigbour]:
                    parent[neigbour] = current
                    visited[neigbour] = True
                    distance[neigbour] = 1 + distance[current]
                    queue.append(neigbour)


        return queue, parent, distance

    def __repr__(self):
        return '\n' + '\n'.join(['{}: {}'.format(node, neighbours) for node, neighbours in enumerate(self.data)])


nodes = 5
edges = [(0, 1), (0, 4), (1, 4), (4, 3), (1, 2), (3, 2), (1, 3)]

graph1 = Graph(nodes, edges)

print(graph1)

print(graph1.BFS(3))


