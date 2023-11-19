class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {v: [] for v in range(vertices)}

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

def dfs(graph, vertex, visited):
    visited[vertex] = True
    print(vertex, end=" ")

    for neighbor in graph.adjacency_list[vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = []
    
    visited.add(start)
    queue.append(start)
    
    while queue:
        current_vertex = queue.pop(0)
        print(current_vertex, end = " ")
        
        for neighbour in tree.adjacency_list[current_vertex]:
            if neighbour not in visited :
                visited.add(neighbour)
                queue.append(neighbour)

     # Example usage
if __name__ == "__main__":
    num_vertices = 7
    example_graph = Graph(num_vertices)
    example_graph.add_edge(0, 1)
    example_graph.add_edge(0, 2)
    example_graph.add_edge(1, 3)
    example_graph.add_edge(1, 4)
    example_graph.add_edge(2, 5)
    example_graph.add_edge(2, 6)

    print("Depth First Search (DFS):")
    visited_dfs = [False] * num_vertices
    for vertex in range(num_vertices):
        if not visited_dfs[vertex]:
            dfs(example_graph, vertex, visited_dfs)

    print("\nBreadth First Search (BFS):")
    bfs(example_graph, 0)