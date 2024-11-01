
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math
import random as r
import matplotlib.pyplot as plt 

def approximate_pi(n):
    inside_circle = 0
    
    for _ in range(n):
        x, y = r.uniform(-1, 1), r.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_approximation = 4 * inside_circle / n
    return pi_approximation
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
