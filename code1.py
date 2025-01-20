
import random


# Random graph generator
def generate_random_graph(n, p):
    graph = {i: [] for i in range(n)}  # Initialize adjacency list
    for i in range(n):
        for j in range(i + 1, n):  # Check all pairs (i, j)
            if random.random() <= p:  # Add edge with probability p
                graph[i].append(j)
                graph[j].append(i)
    return graph


# Greedy heuristic for finding an independent set
def greedy_independent_set(graph):
    independent_set = set()  # Initialize an empty set
    while graph:  # Continue until the graph is empty
        # Select vertex with the fewest neighbors
        vertex = min(graph, key=lambda v: len(graph[v]))
        independent_set.add(vertex)  # Add the vertex to the independent set

        # Remove the vertex and its neighbors from the graph
        neighbors = graph[vertex]
        for neighbor in neighbors:
            if neighbor in graph:
                del graph[neighbor]
        del graph[vertex]
    return independent_set


def main():
    # Generate a random graph using parameters from Section 4
    n = int(input("Enter the number of vertices (n): "))
    p = float(input("Enter the edge probability (p between 0 and 1): "))
    random_graph = generate_random_graph(n, p)
    print("Generated Random Graph (Adjacency List):", random_graph)

    # Find an independent set using the heuristic algorithm
    independent_set = greedy_independent_set(random_graph)
    print("Independent Set Found by Heuristic Algorithm:", independent_set)


if __name__ == "__main__":
    main()


