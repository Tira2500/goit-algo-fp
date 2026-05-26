import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.id = str(uuid.uuid4())


def build_heap_tree(heap_array):
    if not heap_array:
        return None
    nodes = [TreeNode(key) for key in heap_array]
    n = len(heap_array)
    for i in range(n):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < n:
            nodes[i].left = nodes[left_index]
        if right_index < n:
            nodes[i].right = nodes[right_index]
    return nodes[0]


def generate_color_gradient(step, total_steps, base_color=(20, 40, 80)):
    if total_steps <= 1:
        return f"#{base_color[0]:02X}{base_color[1]:02X}{base_color[2]:02X}"
    factor = step / (total_steps - 1)
    r = int(base_color[0] + (240 - base_color[0]) * factor)
    g = int(base_color[1] + (245 - base_color[1]) * factor)
    b = int(base_color[2] + (255 - base_color[2]) * factor)
    return f"#{r:02X}{g:02X}{b:02X}"


def get_dfs_order(root):
    """Ітеративний обхід у глибину (DFS) з використанням СТЕКУ."""
    if not root:
        return []
    order = []
    stack = [root]
    visited = set()
    while stack:
        node = stack.pop()
        if node.id not in visited:
            visited.add(node.id)
            order.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return order


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)
        pos[node.id] = (x, y)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def visualize_traversal(root, traversal_type="DFS"):
    if not root:
        return
    
    nodes_order = get_dfs_order(root)
    base_rgb = (20, 40, 80)

    total_nodes = len(nodes_order)
    color_map = {node.id: generate_color_gradient(step, total_nodes, base_rgb) for step, node in enumerate(nodes_order)}

    G = nx.DiGraph()
    positions = {}
    G = add_edges(G, root, positions)

    node_colors = [color_map[node_id] for node_id in G.nodes()]
    labels = {node_id: G.nodes[node_id]['label'] for node_id in G.nodes()}

    plt.figure(figsize=(10, 7))
    plt.title(f"Візуалізація обходу дерева: {traversal_type}\n(Від темних відтінків до світлих)")
    nx.draw(G, pos=positions, labels=labels, arrows=False, node_size=2200, node_color=node_colors, font_size=11, font_weight="bold")
    plt.show()


if __name__ == "__main__":
    heap_data = [1, 3, 5, 10, 8, 14, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    tree_root = build_heap_tree(heap_data)
    
    print("[КРОК 1] Візуалізація DFS...")
    visualize_traversal(tree_root, "DFS")