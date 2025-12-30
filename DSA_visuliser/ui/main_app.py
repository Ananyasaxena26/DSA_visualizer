import sys
sys.path.append("C:/Users/Ananya/Desktop/DSA_visuliser")

import tkinter as tk
import time, math
from algorithms.sorting import bubble_sort
from algorithms.quick_sort import quick_sort_steps
from algorithms.tree import build_tree_level_order, bfs, inorder, preorder, postorder
from visuals.sort_visualizer import SortVisualizer
from visuals.tree_visualizer import TreeVisualizer
from visuals.graph_visualizer import GraphVisualizer

root = tk.Tk()
root.title("DSA Visualizer")
root.geometry("700x650")

# -------- SORTING USER INPUT --------
tk.Label(root, text="Enter array for sorting (comma separated):", font=("Arial", 11)).pack(pady=3)
sort_entry = tk.Entry(root, width=50)
sort_entry.pack()

tk.Label(root, text="Choose Sorting Algorithm:", font=("Arial", 11)).pack()
sort_algo = tk.StringVar()
sort_menu = tk.OptionMenu(root, sort_algo, "Bubble Sort", "Quick Sort")
sort_menu.pack()
sort_algo.set("Bubble Sort")

def launch_sort():
    arr = [int(x.strip()) for x in sort_entry.get().split(",") if x.strip().isdigit()]
    if not arr:
        print("Invalid array input!")
        return

    if sort_algo.get() == "Quick Sort":
        steps = quick_sort_steps(arr)
    else:
        steps = bubble_sort(arr)

    win = tk.Toplevel(root)
    win.title(sort_algo.get())
    sv = SortVisualizer(win, steps)
    sv.animate()

tk.Button(root, text="Start Sorting Visualization", command=launch_sort, font=("Arial", 10, "bold")).pack(pady=6)

# -------- TREE USER INPUT --------
tk.Label(root, text="Enter tree in Level Order (comma separated, use None for empty):", font=("Arial", 11)).pack(pady=3)
tree_entry = tk.Entry(root, width=50)
tree_entry.pack()

tk.Label(root, text="Choose Tree Traversal:", font=("Arial", 11)).pack()
tree_algo = tk.StringVar()
tree_menu = tk.OptionMenu(root, tree_algo, "BFS", "Inorder", "Preorder", "Postorder")
tree_menu.pack()
tree_algo.set("BFS")

# Add a speed slider for tree animation
tk.Label(root, text="Traversal Animation Speed:", font=("Arial", 11)).pack()
speed_slider = tk.Scale(root, from_=1, to=10, orient="horizontal")
speed_slider.pack()
speed_slider.set(5)

def launch_tree():
    values = [x.strip() for x in tree_entry.get().split(",")]
    if not values:
        print("Invalid tree input!")
        return

    tr = build_tree_level_order(values)

    # Get traversal order
    order = []
    if tree_algo.get() == "BFS":
        order = bfs(tr)
    elif tree_algo.get() == "Inorder":
        res=[]; inorder(tr,res); order=res
    elif tree_algo.get() == "Preorder":
        res=[]; preorder(tr,res); order=res
    elif tree_algo.get() == "Postorder":
        res=[]; postorder(tr,res); order=res

    print(f"{tree_algo.get()} Order:", order)

    win = tk.Toplevel(root)
    win.title("Tree Traversal Visualization")
    tv = TreeVisualizer(win, tr)
    tv.animate_traversal(order, speed_slider.get())

tk.Button(root, text="Start Tree Visualization", command=launch_tree, font=("Arial", 10, "bold")).pack(pady=6)

# -------- GRAPH USER INPUT --------
tk.Label(root, text="Enter number of nodes:", font=("Arial", 11)).pack(pady=3)
graph_nodes = tk.Entry(root, width=10)
graph_nodes.pack()

tk.Label(root, text="Enter graph edges (format: node: n1,n2) each on new line", font=("Arial", 11)).pack()
graph_text = tk.Text(root, width=50, height=8)
graph_text.pack()

def launch_graph():
    graph = {}
    try:
        n = int(graph_nodes.get().strip())
    except:
        print("Invalid node count!")
        return

    for i in range(1, n+1):
        graph[i] = []

    data = graph_text.get("1.0", tk.END).strip().split("\n")
    for line in data:
        if ":" in line:
            u, edges = line.split(":")
            u = int(u.strip())
            if edges.strip():
                graph[u] = [int(x.strip()) for x in edges.split(",") if x.strip().isdigit()]

    win = tk.Toplevel(root)
    win.title("Graph Visualization")
    gv = GraphVisualizer(win, graph)
    gv.render()

tk.Button(root, text="Render Graph Visualization", command=launch_graph, font=("Arial", 10, "bold")).pack(pady=10)

root.mainloop()
