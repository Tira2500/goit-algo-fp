import heapq


def dijkstra(graph, start_vertex):
    # Ініціалізуємо відстані нескінченністю, для стартової — 0
    distances = {vertex: float("inf") for vertex in graph}
    distances[start_vertex] = 0

    # Словник для відстеження маршруту: зберігає, з якої вершини ми прийшли
    parents = {vertex: None for vertex in graph}

    # Черга з пріоритетами (Min-Heap)
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо знайшли коротший шлях — фіксуємо відстань ТА батька
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_vertex  # Запам'ятовуємо, що до neighbor ми прийшли з current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, parents


def get_path(parents, target_vertex):
    """Допоміжна функція для відновлення текстового маршруту від старту до цілі."""
    path = []
    current = target_vertex
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()
    return " -> ".join(path)


if __name__ == "__main__":
    # Наш тестовий граф
    test_graph = {
        "A": {"B": 4, "C": 2},
        "B": {"C": 5, "D": 10},
        "C": {"D": 3, "E": 8},
        "D": {"E": 2},
        "E": {}
    }

    start = "A"
    shortest_paths, vertex_parents = dijkstra(test_graph, start)

    print(f"--- Результати алгоритму Дейкстри (Старт з '{start}'): ---")
    for target in test_graph:
        path_str = get_path(vertex_parents, target)
        print(f"До '{target}': відстань = {shortest_paths[target]}, маршрут: {path_str}")