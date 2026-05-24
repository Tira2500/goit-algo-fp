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

        sorted_list_head = None
        current = self.head

        while current:
            next_node = current.next
            
            if sorted_list_head is None or sorted_list_head.data >= current.data:
                current.next = sorted_list_head
                sorted_list_head = current
            else:
                search = sorted_list_head
                while search.next and search.next.data < current.data:
                    search = search.next
                current.next = search.next
                search.next = current
                
            current = next_node

        self.head = sorted_list_head


def merge_sorted_lists(list1, list2):
    """Об'єднує два відсортовані однозв'язні списки в один новий відсортований список."""
    dummy = Node()  # Тимчасовий вузол-заглушка для полегшення ітерації
    tail = dummy

    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data <= current2.data:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next

    # Приєднуємо залишок, якщо один зі списків закінчився раніше
    if current1:
        tail.next = current1
    elif current2:
        tail.next = current2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list


# Перевірка роботи всіх трьох компонентів
if __name__ == "__main__":
    # 1. Перевірка реверсування
    print("--- 1. Реверсування списку ---")
    llist = LinkedList()
    for val in [10, 20, 30, 40]:
        llist.insert_at_end(val)
    print("Оригінальний:")
    llist.print_list()
    llist.reverse()
    print("Реверсований:")
    llist.print_list()

    # 2. Перевірка сортування
    print("\n--- 2. Сортування вставками ---")
    unsorted_list = LinkedList()
    for val in [15, 3, 24, 8, 42, 1]:
        unsorted_list.insert_at_end(val)
    print("Невідсортований:")
    unsorted_list.print_list()
    unsorted_list.insertion_sort()
    print("Відсортований:")
    unsorted_list.print_list()

    # 3. Перевірка об'єднання двох відсортованих списків
    print("\n--- 3. Об'єднання двох відсортованих списків ---")
    l1 = LinkedList()
    l2 = LinkedList()
    for val in [2, 5, 9, 14]:
        l1.insert_at_end(val)
    for val in [1, 6, 8, 10, 12]:
        l2.insert_at_end(val)
        
    print("Список 1:")
    l1.print_list()
    print("Список 2:")
    l2.print_list()

    merged = merge_sorted_lists(l1, l2)
    print("Результат об'єднання:")
    merged.print_list()