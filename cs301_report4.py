
#for question 8- Black Box Testing
import random
from itertools import combinations
import time

# 1. Helper function to check if the independent set is valid
def is_independent_set(graph, independent_set):
    """
    Checks whether the given independent set is valid (no two vertices are adjacent).
    """
    for i, j in combinations(independent_set, 2):  # Check all pairs in the set
        if j in graph[i]:  # If there is an edge between two vertices, not independent
            return False
    return True

# 2. Function to generate a random graph
def generate_random_graph(n, p):
    graph = {i: [] for i in range(n)}  # Initialize adjacency list
    for i in range(n):
        for j in range(i + 1, n):  # Check all pairs (i, j)
            if random.random() <= p:  # Add edge with probability p
                graph[i].append(j)
                graph[j].append(i)
    return graph

# 3. Simple heuristic: Greedy selection of vertices with the least neighbors
def heuristic_independent_set(graph):
    n = len(graph)
    independent_set = []
    vertices = list(range(n))
    
    for vertex in vertices:
        # Check if vertex can be added to the independent set
        if all(neighbor not in independent_set for neighbor in graph[vertex]):
            independent_set.append(vertex)  # Add the vertex to the independent set
            
    return independent_set

# 4. Functional Testing - Black Box Testing
def black_box_testing():
    # List of test cases with (n, p) pairs (n: number of vertices, p: edge probability)
    test_cases = [
        (5, 0.2), (5, 0.5), (5, 0.8),  
        (8, 0.2), (8, 0.5), (8, 0.8),
        (10, 0.2), (10, 0.5), (10, 0.8),
        (15, 0.2), (15, 0.5), (15, 0.8), 
        (20, 0.2), (20, 0.5), (20, 0.8),  
        (25, 0.2), (25, 0.5), (25, 0.8),
        (30, 0.2), (30, 0.5), (30, 0.8),
        (40, 0.2), (40, 0.5), (40, 0.8),
    ]
    
    for n, p in test_cases:
        # Generate random graph
        graph = generate_random_graph(n, p)
        print(f"Testing graph with n={n}, p={p}")
        
        # Apply your heuristic algorithm (assuming `heuristic_independent_set` is defined)
        heuristic_set = heuristic_independent_set(graph)
        
        # Validate if the heuristic set is independent
        assert is_independent_set(graph, heuristic_set), f"Test failed for n={n}, p={p}! Heuristic set is not independent."
        
        # Print success message for this test case
        print(f"Test passed for n={n}, p={p}. Heuristic set is independent.")
        
        # Optional: Print the results for verification
        print(f"Independent Set: {heuristic_set}")
        print("-" * 40)

# 5. Performance Testing (did not print for this context but can be useful)
def performance_testing():
    sizes = [5, 10, 15, 20, 25, 30]
    probabilities = [0.1, 0.5, 0.9]
    
    for n in sizes:
        for p in probabilities:
            graph = generate_random_graph(n, p)
            start_time = time.time()
            heuristic_set = heuristic_independent_set(graph)  # Assuming you have this heuristic
            end_time = time.time()
            print(f"n={n}, p={p} => Heuristic Time: {end_time - start_time:.6f} seconds")

# Run the tests
print("Running Black Box Tests...")
black_box_testing()


