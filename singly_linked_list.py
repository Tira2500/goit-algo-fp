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
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        """Сортування однозв'язного списку вставками (in-place)."""
        if not self.head or not self.head.next:
            return

        sorted_list_head = None  # Голова майбутнього відсортованого списку
        current = self.head

        while current:
            next_node = current.next  # Запам'ятовуємо наступний вузол
            
            # Вставка поточного вузла у новий відсортований підсписок
            if sorted_list_head is None or sorted_list_head.data >= current.data:
                current.next = sorted_list_head
                sorted_list_head = current
            else:
                search = sorted_list_head
                while search.next and search.next.data < current.data:
                    search = search.next
                current.next = search.next
                search.next = current
                
            current = next_node  # Переходимо далі

        self.head = sorted_list_head  # Оновлюємо голову списку


# Перевірка роботи другої частини
if __name__ == "__main__":
    print("--- Перевірка сортування вставками ---")
    unsorted_list = LinkedList()
    for val in [15, 3, 24, 8, 42, 1]:
        unsorted_list.insert_at_end(val)
        
    print("Невідсортований список:")
    unsorted_list.print_list()

    unsorted_list.insertion_sort()
    print("Відсортований список:")
    unsorted_list.print_list()