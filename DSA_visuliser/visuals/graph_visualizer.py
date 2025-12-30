import tkinter as tk
import math

class GraphVisualizer:
    def __init__(self, root, graph):
        self.root = root
        self.graph = graph
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()

    def render(self):
        self.canvas.delete("all")

        # Ensure all nodes exist
        all_nodes = set(self.graph.keys())
        for u in self.graph:
            for v in self.graph[u]:
                all_nodes.add(v)
        for node in all_nodes:
            if node not in self.graph:
                self.graph[node] = []

        nodes = list(self.graph.keys())
        n = len(nodes)
        center_x, center_y, radius = 300, 200, 150
        pos = {}

        # Draw nodes in circle
        for i, node in enumerate(nodes):
            angle = 2 * math.pi * i / n
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            pos[node] = (x, y)
            self.canvas.create_oval(x-18, y-18, x+18, y+18)
            self.canvas.create_text(x, y, text=str(node), font=("Arial", 11, "bold"))

        # Draw edges
        for u in self.graph:
            for v in self.graph[u]:
                if v in pos:
                    x1, y1 = pos[u]
                    x2, y2 = pos[v]
                    self.canvas.create_line(x1, y1, x2, y2)

        self.root.update()
