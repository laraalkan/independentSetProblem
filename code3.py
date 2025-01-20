
#for question 7- experiment

import random
from itertools import combinations
import time

# Brute Force Algorithm (from previous code)
def generate_random_graph(n, p):
    graph = {i: [] for i in range(n)}  # Initialize adjacency list
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() <= p:
                graph[i].append(j)
                graph[j].append(i)
    return graph

def is_independent_set(graph, subset):
    for i, j in combinations(subset, 2):
        if j in graph[i]:
            return False
    return True

def find_max_independent_set(graph):
    n = len(graph)
    max_set = []
    for r in range(n + 1):
        for subset in combinations(range(n), r):
            if is_independent_set(graph, subset) and len(subset) > len(max_set):
                max_set = subset
    return max_set

# Heuristic Algorithm (e.g., greedy approach)
def heuristic_independent_set(graph):
    n = len(graph)
    independent_set = []
    vertices = list(range(n))
    for vertex in vertices:
        if all(neighbor not in independent_set for neighbor in graph[vertex]):
            independent_set.append(vertex)
    return independent_set

# Experiment function
def experiment(n, p):
    graph = generate_random_graph(n, p)

    # Brute-force approach
    start_time = time.perf_counter()
    max_set_bf = find_max_independent_set(graph)
    bf_time = time.perf_counter() - start_time
    max_size_bf = len(max_set_bf)

    # Heuristic approach
    start_timeh = time.perf_counter()
    max_set_h = heuristic_independent_set(graph)
    heuristic_time = time.perf_counter() - start_timeh
    max_size_h = len(max_set_h)

    # Calculate relative error
    relative_error = (max_size_h - max_size_bf) / max_size_bf * 100

    return max_size_bf, max_size_h, relative_error, bf_time, heuristic_time

# Run experiments for different n and p
def run_experiments():
    for n in [5, 8, 10, 12, 16, 18, 20, 22 ,24]:
        for p in [0.2, 0.5, 0.8]:
            bf_size, heuristic_size, error, bf_time, heuristic_time = experiment(n, p)
            print(f"n={n}, p={p}")
            print(f"Brute Force Size: {bf_size}, Heuristic Size: {heuristic_size}")
            print(f"Relative Error: {error:.2f}%")
            print(f"Brute Force Time: {bf_time:.4f}s, Heuristic Time: {heuristic_time:.4f}s")
            print("="*40)

if __name__ == "__main__":
    run_experiments()

