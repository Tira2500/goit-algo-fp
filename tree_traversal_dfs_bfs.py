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
    """Будує повне бінарне дерево на основі масиву купи (патерн із завдання 4)."""
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


def generate_color_gradient(step, total_steps, base_color=(18, 50, 120)):
    """
    Генерує HEX-колір, який плавно змінюється від темного відтінку до світлого.
    base_color: стартовий темний колір у форматі RGB.
    """
    if total_steps <= 1:
        return f"#{base_color[0]:02X}{base_color[1]:02X}{base_color[2]:02X}"
        
    # Розраховуємо коефіцієнт освітлення (від 0.0 до 1.0)
    factor = step / (total_steps - 1)
    
    # Плавно рухаємо кожен RGB канал у бік максимального освітлення
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
            # Спочатку кладемо правого, потім лівого, 
            # щоб лівий вискочив зі стеку ПЕРШИМ (класичний Pre-order DFS)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return order


def get_bfs_order(root):
    """Обхід у ширину (BFS) з використанням ЧЕРГИ."""
    if not root:
        return []

    order = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        order.append(node)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Рекурсивне додавання ребер для NetworkX (побудова скелета дерева)."""
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
    """Малює дерево та розфарбовує вузли відповідно до порядку обходу."""
    if not root:
        return

    # 1. Отримуємо порядок обходу вузлів
    if traversal_type == "DFS":
        nodes_order = get_dfs_order(root)
        base_rgb = (20, 40, 80)     # Сині відтінки для DFS
    else:
        nodes_order = get_bfs_order(root)
        base_rgb = (80, 20, 40)     # Червоно-пурпурні відтінки для BFS

    total_nodes = len(nodes_order)
    
    # Створюємо мапу відповідності: ID вузла -> його унікальний HEX колір
    color_map = {}
    for step, node in enumerate(nodes_order):
        color_map[node.id] = generate_color_gradient(step, total_nodes, base_rgb)

    # 2. Побудова графа NetworkX
    G = nx.DiGraph()
    positions = {}
    G = add_edges(G, root, positions)

    # Збираємо кольори для відображення у правильному порядку вершин NetworkX
    node_colors = [color_map[node_id] for node_id in G.nodes()]
    labels = {node_id: G.nodes[node_id]['label'] for node_id in G.nodes()}

    # 3. Малювання за допомогою Matplotlib
    plt.figure(figsize=(10, 7))
    plt.title(f"Візуалізація обходу дерева: {traversal_type}\n(Від темних відтінків до світлих)")
    nx.draw(
        G,
        pos=positions,
        labels=labels,
        arrows=False,
        node_size=2200,
        node_color=node_colors,
        font_size=11,
        font_weight="bold",
        font_color="black"
    )
    plt.show()


if __name__ == "__main__":
    # Масив бінарної купи для генерації структури дерева
    heap_data = [1, 3, 5, 10, 8, 14, 20, 25, 30, 35, 40, 45, 50, 55, 60]

    print("Будуємо структуру дерева з масиву купи...")
    tree_root = build_heap_tree(heap_data)

    print("\n[КРОК 1] Відкриваємо візуалізацію для DFS (у глибину зі стеком)...")
    print("Закрийте вікно графіка, щоб перейти до наступного обходу.")
    visualize_traversal(tree_root, "DFS")

    print("\n[КРОК 2] Відкриваємо візуалізацію для BFS (в ширину з чергою)...")
    visualize_traversal(tree_root, "BFS")
    print("\nУсі обходи успішно візуалізовані!")