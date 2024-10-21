
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
    # Write your code here
    inside_circle = 0
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []
    
    for _ in range(n):
        x, y = r.uniform(-1, 1), r.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    pi_approximation = 4 * inside_circle / n
    plt.figure(figsize=(5,5))
    plt.scatter(x_inside, y_inside, color='red', s=1, label="Inside Circle")
    plt.scatter(x_outside, y_outside, color='blue', s=1, label="Outside Circle")
    plt.legend()
    plt.title(f"Monte Carlo Approximation of π with {n} points")
    plt.savefig(f"monte_carlo_pi_{n}.png")
    plt.show()
    return pi_approximation
    #return
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
