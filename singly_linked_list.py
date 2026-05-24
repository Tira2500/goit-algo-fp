class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Список порожній")

    def reverse(self):
        """Реверсування однозв'язного списку шляхом зміни посилань."""
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Запам'ятовуємо наступний вузол
            current.next = prev       # Розворачуємо вказівник назад
            prev = current            # Рухаємось вперед
            current = next_node
        self.head = prev              # Оновлюємо голову списку


# Перевірка роботи першої частини
if __name__ == "__main__":
    llist = LinkedList()
    for val in [10, 20, 30, 40]:
        llist.insert_at_end(val)
        
    print("Оригінальний список:")
    llist.print_list()

    llist.reverse()
    print("Після реверсування:")
    llist.print_list()