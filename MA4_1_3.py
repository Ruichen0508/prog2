import numpy as np
import math as m
import random as r
from concurrent.futures import ProcessPoolExecutor
import time

# Performance counter for timing
pc = time.perf_counter

def sphere_volume(n, d):
    """
    Monte Carlo method to approximate the volume of a d-dimensional hypersphere.
    n: Number of random points
    d: Dimensions of the hypersphere
    """
    inside_sphere = 0
    for _ in range(n):
        point = [r.uniform(-1, 1) for _ in range(d)]
        if sum(x**2 for x in point) <= 1:
            inside_sphere += 1
    return inside_sphere

def hypersphere_exact(d):
    """
    Calculates the exact volume of a d-dimensional hypersphere with radius 1.
    Uses the formula Vd = (pi^(d/2)) / Gamma((d/2) + 1)
    """
    return (m.pi ** (d / 2)) / m.gamma((d / 2) + 1)

def count_inside_sphere(sub_n, d):
    """
    Count the points inside the d-dimensional hypersphere for a subset of points.
    """
    count = 0
    for _ in range(sub_n):
        point = np.random.uniform(-1, 1, d)
        if np.sum(point ** 2) <= 1:
            count += 1
    return count

# Part 1: Parallelize the loop
def sphere_volume_parallel1(n, d, num_processes):
    """
    Parallelizes the Monte Carlo simulation using ProcessPoolExecutor.
    Parallelizes the loop itself, running `count_inside_sphere` in separate processes.
    n: Number of random points
    d: Dimensions of the hypersphere
    num_processes: Number of processes to use
    """
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        futures = [executor.submit(count_inside_sphere, n // num_processes, d) for _ in range(num_processes)]
        total_inside_sphere = sum(future.result() for future in futures)

    volume_approx = (2 ** d) * (total_inside_sphere / n)
    return volume_approx

# Part 2: Parallelize data processing
def sphere_volume_parallel2(n, d, num_processes):
    """
    Parallelizes the data processing by splitting the data into parts.
    Each process handles a portion of the random points.
    n: Number of random points
    d: Dimensions of the hypersphere
    num_processes: Number of processes to use
    """
    start_time = pc()
    
    # Use ProcessPoolExecutor to split the data among processes
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        futures = [executor.submit(count_inside_sphere, n // num_processes, d) for _ in range(num_processes)]
        total_inside_sphere = sum(f.result() for f in futures)
    
    volume_approx = (2 ** d) * (total_inside_sphere / n)
    end_time = pc()
    print(f"Parallelized data processing approximation: {volume_approx}")
    print(f"Execution time for parallelized data processing: {end_time - start_time:.2f} seconds")

    return volume_approx

def main():
    n = 1000000  # Number of random points
    d = 8  # Dimensions
    num_processes = 4  # Number of processes to use, ideally matches CPU core count

    # Sequential execution
    start = pc()
    sequential_result = sphere_volume(n, d)
    stop = pc()
    sequential_time = stop - start
    print(f"[Sequential] Approx Volume: {sequential_result}, Time: {sequential_time:.2f} seconds")

    # Parallel execution for Part 1
    start = pc()
    parallel_result1 = sphere_volume_parallel1(n, d, num_processes)
    stop = pc()
    parallel_time1 = stop - start
    print(f"[Parallel Part 1] Approx Volume: {parallel_result1}, Time: {parallel_time1:.2f} seconds")

    # Parallel execution for Part 2
    start = pc()
    parallel_result2 = sphere_volume_parallel2(n, d, num_processes)
    stop = pc()
    parallel_time2 = stop - start
    print(f"[Parallel Part 2] Approx Volume: {parallel_result2}, Time: {parallel_time2:.2f} seconds")

    # Print speedup
    print(f"Speedup Part 1: {sequential_time / parallel_time1:.2f}x")
    print(f"Speedup Part 2: {sequential_time / parallel_time2:.2f}x")

if __name__ == '__main__':
    main()
