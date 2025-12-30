import tkinter as tk
import time, math

class TreeVisualizer:
    def __init__(self, root, tree_root):
        self.root = root
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()
        self.tree_root = tree_root
        self.pos = {}

    def draw_tree(self, node, x, y, dx):
        if not node:
            return

        # Save position of each node
        self.pos[node.val] = (x, y)

        # Draw node
        self.canvas.create_oval(x-15, y-15, x+15, y+15, tags=str(node.val))
        self.canvas.create_text(x, y, text=str(node.val), font=("Arial", 10, "bold"))

        if node.left:
            self.canvas.create_line(x, y+15, x-dx, y+60-15)
            self.draw_tree(node.left, x-dx, y+60, dx//2)

        if node.right:
            self.canvas.create_line(x, y+15, x+dx, y+60-15)
            self.draw_tree(node.right, x+dx, y+60, dx//2)

    def render(self):
        self.canvas.delete("all")
        self.pos = {}
        self.draw_tree(self.tree_root, 300, 50, 120)
        self.root.update()

    def animate_traversal(self, order, speed=5):
        self.render()  # Draw tree once

        for val in order:
            self.highlight_node(val)
            time.sleep(1.5 / speed)

    def highlight_node(self, val):
        # Reset all nodes to normal first
        for node_val, (x, y) in self.pos.items():
            self.canvas.itemconfig(str(node_val), width=1)

        # Highlight current visited node
        x, y = self.pos[val]
        self.canvas.itemconfig(str(val), width=4)  # thicker border to highlight
        self.canvas.create_text(300, 350, text=f"Visited: {val}", font=("Arial", 12, "bold"), tags="visited")
        self.root.update()
