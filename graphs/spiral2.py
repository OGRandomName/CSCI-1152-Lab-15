"""
Program: Lab15_kcherry8.py
Author: Kenneth Cherry
Purpose: Plot a spiral using NumPy arrays and matplotlib for efficient computation and visualization.
Date: December 5, 2025
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_spiral(num_points=2000, spacing=0.08, growth=0.02):
    """
    Generate x and y coordinates for a spiral using NumPy.
    num_points: number of points to calculate
    spacing: controls how tightly the spiral winds
    growth: controls how far the spiral expands
    """
    theta = np.arange(num_points) * spacing
    r = np.arange(num_points) * growth
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

def plot_spiral():
    x, y = generate_spiral()
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, color="darkorange", linewidth=2.5, linestyle="-")
    plt.title("Spiral Plot (NumPy)")
    plt.axis("equal")
    plt.grid(alpha=0.3)
    plt.show()

if __name__ == "__main__":
    plot_spiral()
