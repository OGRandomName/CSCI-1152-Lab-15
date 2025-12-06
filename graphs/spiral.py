"""
Program: Lab15_kcherry8.py
Author: Kenneth Cherry
Purpose: Plot a spiral using parametric equations with matplotlib.
Date: December 5, 2025
"""

import math
import matplotlib.pyplot as plt

def generate_spiral_points(num_points=1000, spacing=0.1):
    """
    Generate x and y coordinates for a spiral.
    num_points: number of points to calculate
    spacing: controls how tightly the spiral winds
    """
    x_vals = []
    y_vals = []
    for i in range(num_points):
        angle = i * spacing
        radius = i / 50.0  # controls how far the spiral expands
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        x_vals.append(x)
        y_vals.append(y)
    return x_vals, y_vals

def plot_spiral():
    x_vals, y_vals = generate_spiral_points()
    plt.figure(figsize=(8, 8))
    plt.plot(x_vals, y_vals, color="purple", linewidth=2, linestyle="--")
    plt.title("Spiral Plot")
    plt.axis("equal")  # keep aspect ratio square
    plt.show()

if __name__ == "__main__":
    plot_spiral()
