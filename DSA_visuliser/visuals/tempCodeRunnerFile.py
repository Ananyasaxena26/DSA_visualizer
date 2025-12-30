import tkinter as tk
import math
import time  # Added this import
from collections import deque

class GraphVisualizer:
    def __init__(self, root, graph):
        self.root = root
        self.graph = graph
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()

    def draw_graph(self, adj):
        self.canvas.delete("all")
        nodes = list(adj.keys())
        n = len(nodes)
        center_x, center_y, radius = 300, 200, 150
        pos = {}

        # place nodes in circle
        for i, node in enumerate(nodes):
            angle = 2 * math.pi * i / n
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            pos[node] = (x, y)
            self.canvas.create_oval(x-18, y-18, x+18, y+18)
            self.canvas.create_text(x, y, text=str(node), font=("Arial", 11, "bold"))

        # draw edges
        for u in adj:
            for v in adj[u]:
                if v in pos:
                    x1, y1 = pos[u]
                    x2, y2 = pos[v]
                    self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST)

        self.root.update()

    def render(self):
        self.draw_graph(self.graph)

    # Optional: visualize BFS step order
    def animate_bfs(self, start):
        order = []
        visited = set([start])
        q = deque([start])

        while q:
            u = q.popleft()
            order.append(u)
            for v in self.graph[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)

        for node in order:
            self.highlight_node(node)
            self.canvas.update()
            self.root.update()
            time.sleep(0.5)

    def highlight_node(self, node):
        # redraw graph and make visited node bold/large
        self.canvas.delete("all")
        self.draw_graph(self.graph)
