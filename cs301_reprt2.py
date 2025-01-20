import time

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Generate random graph
def generate_random_graph(n, p):
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if np.random.random() <= p:
                graph[i].append(j)
                graph[j].append(i)
    return graph

# Heuristic algorithm
def greedy_independent_set(graph):
    independent_set = set()
    while graph:
        vertex = min(graph, key=lambda v: len(graph[v]))
        independent_set.add(vertex)
        neighbors = graph[vertex]
        for neighbor in neighbors:
            if neighbor in graph:
                del graph[neighbor]
        del graph[vertex]
    return independent_set

# Measure runtime
def measure_runtime(algorithm, graph, runs=30, repeat=100):
    times = []
    for _ in range(runs):
        start_time = time.perf_counter()
        for _ in range(repeat):
            algorithm(graph.copy())
        end_time = time.perf_counter()
        times.append((end_time - start_time) / repeat)  # Average per repetition
    return np.mean(times), np.std(times)

# Confidence interval
def compute_confidence_interval(mean, std, n, confidence=0.9):
    t_value = t.ppf((1 + confidence) / 2, df=n-1)
    margin_of_error = t_value * (std / np.sqrt(n))
    return mean - margin_of_error, mean + margin_of_error

# Run experiments
def run_experiments():
    sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120,130, 140, 150, 160, 170, 180, 190, 200, 220, 230, 240, 250, 260, 270 ]  # Larger sizes
    p = 0.5
    runs = 30
    repeat = 50

    means = []
    margins = []
    for n in sizes:
        print(f"Running for input size: {n}")
        graph = generate_random_graph(n, p)
        mean_time, std_time = measure_runtime(greedy_independent_set, graph, runs, repeat)
        ci = compute_confidence_interval(mean_time, std_time, runs)
        means.append(mean_time)
        margins.append(ci[1] - mean_time)  # Margin of error
        print(f"n={n}, Mean Time={mean_time:.6f}, CI={ci}")

    # Plot runtime with confidence intervals
    plt.errorbar(sizes, means, yerr=margins, fmt='o-', label='Runtime with CI')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Average Runtime (seconds)')
    plt.title('Runtime Analysis with Confidence Intervals')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    run_experiments()

