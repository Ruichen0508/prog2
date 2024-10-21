
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as r
from functools import reduce
def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    inside_sphere = 0
    for _ in range(n):
        point = [r.uniform(-1, 1) for _ in range(d)]
        if sum(map(lambda x: x**2, point)) <= 1:
            inside_sphere += 1

    volume_approx = (2**d) * (inside_sphere / n)
    print(f"Approximate Volume of {d}-dimensional hypersphere with {n} points: {volume_approx}")
    return volume_approx

def hypersphere_exact(n,d):
    return (m.pi ** (d / 2)) / m.gamma((d / 2) + 1)
     
def main():
    n = 100000
    d = 2
    sphere_volume(n,d)


if __name__ == '__main__':
	main()
