import uuid
import networkx as nx
import matplotlib.pyplot as plt


class HeapNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для побудови графа networkx


def build_heap_tree(heap_array):
    """
    Перетворює звичайний масив, який представляє купу, 
    у зв'язну структуру об'єктів HeapNode.
    """
    if not heap_array:
        return None

    # Створюємо вузол для кожного елемента масиву
    nodes = [HeapNode(key) for key in heap_array]
    n = len(heap_array)

    # Зшиваємо вузли посиланнями left та right за індексами бінарної купи
    for i in range(n):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < n:
            nodes[i].left = nodes[left_index]
        if right_index < n:
            nodes[i].right = nodes[right_index]

    return nodes[0]  # Повертаємо корінь дерева


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Рекурсивно додає вершини та ребра дерева в граф NetworkX для візуалізації."""
    if node is not None:
        graph.add_node(node.id, color="skyblue", label=node.val)
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


def draw_tree(tree_root):
    """Візуалізує дерево за допомогою matplotlib та networkx."""
    if not tree_root:
        print("Дерево порожнє.")
        return

    tree_graph = nx.DiGraph()
    positions = {}
    tree_graph = add_edges(tree_graph, tree_root, positions)

    colors = [node[1]['color'] for node in tree_graph.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree_graph.nodes(data=True)}

    plt.figure(figsize=(10, 7))
    plt.title("Візуалізація структури бінарної купи")
    nx.draw(
        tree_graph, 
        pos=positions, 
        labels=labels, 
        arrows=False, 
        node_size=2500, 
        node_color=colors, 
        font_size=12, 
        font_weight="bold"
    )
    plt.show()


if __name__ == "__main__":
    # Створюємо масив, який уже є коректною мін-купою (Min-Heap)
    # Кожен батько менший або дорівнює за своїх дітей
    min_heap = [1, 3, 5, 10, 8, 14, 20, 25, 30]

    print("Будуємо дерево з масиву купи...")
    root = build_heap_tree(min_heap)

    print("Відкриваємо вікно візуалізації...")
    draw_tree(root)