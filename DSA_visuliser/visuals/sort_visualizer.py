import tkinter as tk
import time

class SortVisualizer:
    def __init__(self, root, steps):
        self.root = root
        self.steps = steps
        self.canvas = tk.Canvas(root, width=600, height=300)
        self.canvas.pack()

    def draw(self, arr, i=None, j=None):
        self.canvas.delete("all")
        n = len(arr)
        bar_width = 600 // n
        max_val = max(arr)

        for idx, val in enumerate(arr):
            x0 = idx * bar_width + 5
            x1 = x0 + bar_width - 10
            h = int((val / max_val) * 250)
            y0 = 300 - h - 10
            y1 = 300 - 10

            if idx == i or idx == j:
                self.canvas.create_rectangle(x0, y0, x1, y1, width=3)
            else:
                self.canvas.create_rectangle(x0, y0, x1, y1)

            self.canvas.create_text((x0 + x1) // 2, y0 - 8, text=str(val), font=("Arial", 10, "bold"))

        self.root.update()

    def animate(self):
        for arr, i, j in self.steps:
            self.draw(arr, i, j)
            time.sleep(0.5)


