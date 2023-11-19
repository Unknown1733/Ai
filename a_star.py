class AStarAlgorithm:
    def __init__(self, graph):
        self.graph = graph

    def neighbors(self, v):
        return self.graph[v]

    def h(self, n):
        H= {
            'A': 11,
            'B': 6,
            'C': 5,
            'D': 7,
            'E': 3,
            'F': 6,
            'G': 5,
            'H': 3,
            'I': 1,
            'J': 0
        }
        return H[n]

    def run(self, start_node, goal_node):
        open_set=set([start_node]);
        close_set=set([]);

        g={};
        g[start_node]=0;

        parents={};
        parents[start_node]=start_node;

        while len(open_set) > 0:
            n=None;

            for m in open_set:
                if n==None or g[m]+self.h(m) < g[n]+self.h(n):
                    n=m;

            if(n==None):
                print("Path doesn't exists");
                return n;

            if(n==goal_node):
                path=[]

                while parents[n]!=n:
                    path.append(n)
                    n=parents[n]

                path.append(start_node)
                path.reverse()
                print(f"Path:{path}")
                return path

            for (m,weight) in self.neighbors(n):
                if(m not in open_set and m not in close_set):
                    open_set.add(m)
                    parents[m]=n
                    g[m]=g[n]+weight
                else:
                    if g[n]+weight < g[m]:
                        g[m]=g[n]+weight
                        parents[m]=n

                        if(m in close_set):
                            close_set.remove(m)
                            open_set.add(m)

            open_set.remove(n);
            close_set.add(n);

        print("Path not found!")
        return None


graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
    'J': [('E', 5), ('I', 3)],
}
a_start = AStarAlgorithm(graph)
a_start.run('A', 'J')