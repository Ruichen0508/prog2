
"""
Solutions to module 4
Review date:
"""

student = "Libra"
reviewer = "Ann"
import numpy as np
import math as m
import random as r
from concurrent.futures import ProcessPoolExecutor
import time
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
    count = 0
    for _ in range(sub_n):
        point = np.random.uniform(-1, 1, d)
        if np.sum(point ** 2) <= 1:
            count += 1
    return count
# Part 1: Parallelize the loop
def sphere_volume_parallel1(n, d, np):
    """
    Parallelizes the Monte Carlo simulation using ProcessPoolExecutor.
    Parallelizes the loop itself, running `sphere_volume` in separate processes.
    n: Number of random points
    d: Dimensions of the hypersphere
    np: Number of processes to use
    """
    with ProcessPoolExecutor(max_workers=np) as executor:
        futures = [executor.submit(count_inside_sphere, n // np, d) for _ in range(np)]
        total_inside_sphere = sum(future.result() for future in futures)

    volume_approx = (2 ** d) * (total_inside_sphere / n)
    return volume_approx

# Part 2: Parallelize data processing
def sphere_volume_parallel2(n, d, np):
    """
    Parallelizes the data processing by splitting the data into parts.
    Each process handles a portion of the random points.
    n: Number of random points
    d: Dimensions of the hypersphere
    np: Number of processes to use
    """
    start_time = pc()

    # Use ProcessPoolExecutor to split the data among processes
    with ProcessPoolExecutor(max_workers=np) as executor:
        futures = [executor.submit(sphere_volume, n // np, d) for _ in range(np)]
        results = [f.result() for f in futures]

    total_inside_sphere = sum(results)
    volume_approx = (2 ** d) * (total_inside_sphere / n)

    end_time = pc()
    print(f"Parallelized data processing approximation: {volume_approx}")
    print(f"Execution time for parallelized data processing: {end_time - start_time:.2f} seconds")

    return volume_approx

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11

    start = pc()
    for y in range(10):
        sphere_volume(n, d)
    stop = pc()
    print(f"[Part 1] Sequential time: {stop - start:.2f} seconds")

    # Part 2 - Parallelized loop
    n=100000
    d=11
    start = pc()
    sphere_volume(n, d)
    stop = pc()
    print(f"[Part 2] Parallelized loop time: {stop - start:.2f} seconds")

    # Part 3 - Parallelized data processing
    start = pc()
    sphere_volume_parallel2(n, d, 10)
    stop = pc()
    print(f"[Part 3] Parallelized data processing time: {stop - start:.2f} seconds")


if __name__ == '__main__':
	main()
