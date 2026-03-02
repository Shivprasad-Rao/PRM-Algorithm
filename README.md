# 🗺️ Interactive Pathfinding & Probabilistic Roadmap (PRM) Visualizer

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green.svg)
![License](https://img.shields.io/badge/License-MIT-purple.svg)

An interactive, user-driven pathfinding visualizer built in Python using Pygame. This project demonstrates advanced algorithmic logic by allowing users to draw complex obstacles on a canvas, pick start and end coordinates, and watch as the system computes a collision-free path using a **Probabilistic Roadmap (PRM)** methodology combined with a **Shortest Path (Dijkstra)** algorithm.

## ✨ Features

- **Dynamic Environment Generation:** Users can manually generate custom polygonal and circular obstacles in real-time.
- **Probabilistic Graph Building:** The algorithm intelligently scatters random nodes across the grid, strictly avoiding overlaps with user-defined obstacles (Collision Detection).
- **Line-of-Sight Edge Computation:** Nodes are connected into a traversable graph based on proximity (Euclidean distance) and line-of-sight checks against dynamically drawn bounding boxes.
- **Recursive Path Planning:** Implements a custom shortest-path algorithm to traverse the dynamically generated mesh to find the most optimal route.
- **Visual Feedback:** Shows the node generation, edge connection, and final path calculation in visually distinct, real-time steps.

## 🧠 Logic & Algorithmic Highlights

This project was built to showcase core Computer Science concepts practically applied to a 2D coordinate space:

*   **Computational Geometry:** Custom mathematical formulas calculate properties of dynamic triangles and track circle/rectangle collisions using Pygame's `collidepoint` and `clipline`.
*   **Graph Theory:** Maps visual coordinates to an Adjacency List (dictionary-based node-to-neighbor graph mapping with weighted distances). 
*   **Pathfinding Algorithm:** Instead of standard breadth-first search grid traversal, this uses an adapted **Dijkstra’s Algorithm**. It maps tentative distances recursively to find the absolute shortest edge-chain to the target.
*   **Fail-Safe Handling:** Implements exception handling for walled-off bounds—smoothly communicating to the user if a viable path cannot be found.

## 🕹️ Controls & Usage

**1. Obstacle Generation Phase**
*   **Left Mouse Button (LMB):** Span a Square/Rectangle.
*   **Right Mouse Button (RMB):** Drop a Circular obstacle.
*   **Middle Mouse Button (MMB):** Drop a Triangular obstacle.
*   `SPACE`: Confirm obstacles and proceed to the next phase.

**2. Node Selection Phase**
*   **Left Mouse Button:** Select your **Start** point.
*   **Left Mouse Button:** Select your **End** destination.

**3. Execution**
*   Watch as the software maps the traversable nodes (cyan), connects edges (blue), and calculates the optimal route (orange).
*   `ESC`: Exit the application safely at any point.
