class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None

    def __repr__(self):
        return f"({self.value}, p={self.priority})"


class BinaryTreePriorityQueue:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value, priority):
        new_node = Node(value, priority)

        if self.root is None:
            self.root = new_node
        else:
            self.root = self._insert_recursive(self.root, new_node)

        self.size += 1

    def _insert_recursive(self, current, new_node):
        if new_node.priority > current.priority:
            new_node.left = current
            return new_node
        else:
            if current.right is None:
                current.right = new_node
            else:
                current.right = self._insert_recursive(current.right, new_node)
            return current

    def pop(self):
        if self.root is None:
            raise IndexError("Черга порожня, нічого видаляти!")

        top = self.root
        self.root = self._merge(self.root.left, self.root.right)
        self.size -= 1

        return top.value, top.priority

    def _merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if left.priority >= right.priority:
            left.right = self._merge(left.right, right)
            return left
        else:
            right.right = self._merge(left, right.right)
            return right

    def peek(self):
        if self.root is None:
            raise IndexError("Черга порожня, нема на що дивитись!")

        return self.root.value, self.root.priority

    def view_all(self):
        all_nodes = []
        self._collect_all(self.root, all_nodes)
        all_nodes.sort(key=lambda node: node.priority, reverse=True)
        return [(node.value, node.priority) for node in all_nodes]

    def _collect_all(self, node, result):
        if node is None:
            return
        result.append(node)
        self._collect_all(node.left, result)
        self._collect_all(node.right, result)

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __bool__(self):
        return self.size > 0

    def print_tree(self):
        if self.root is None:
            print("(дерево порожнє)")
            return
        print(f"Корінь: {self.root}")
        self._print_recursive(self.root, prefix="", is_left=None)

    def _print_recursive(self, node, prefix, is_left):
        if node is None:
            return

        if is_left is True:
            connector = "├─[L]─ "
            child_prefix = prefix + "│      "
        elif is_left is False:
            connector = "└─[R]─ "
            child_prefix = prefix + "       "
        else:
            child_prefix = prefix

        if is_left is not None:
            print(f"{prefix}{connector}{node}")

        if node.left or node.right:
            self._print_recursive(node.left, child_prefix, True)
            self._print_recursive(node.right, child_prefix, False)


if __name__ == "__main__":
    pq = BinaryTreePriorityQueue()

    print("=" * 45)
    print("         ТЕСТУВАННЯ ЧЕРГИ З ПРІОРИТЕТАМИ")
    print("=" * 45)

    print("\n>>> Вставляємо елементи:\n")
    tasks = [
        ("помити посуд",    2),
        ("здати лабу",     10),
        ("подивитись серіал", 1),
        ("поїсти",          7),
        ("поспати",         5),
        ("вивчити білети",  9),
    ]
    for name, priority in tasks:
        pq.insert(name, priority)
        print(f"    + '{name}'  (пріоритет {priority})")

    print(f"\n    Розмір черги: {len(pq)}")

    print("\n>>> Хто перший у черзі? (peek)\n")
    val, pri = pq.peek()
    print(f"    '{val}'  з пріоритетом {pri}")

    print("\n>>> Усі елементи черги (від важливого до не дуже):\n")
    for val, pri in pq.view_all():
        bar = "█" * pri
        print(f"    [{pri:>2}] {bar:<10}  '{val}'")

    print("\n>>> Як виглядає дерево зсередини:\n")
    pq.print_tree()

    print("\n>>> Видаляємо по одному (pop):\n")
    while pq:
        val, pri = pq.pop()
        print(f"    Виконуємо: '{val}'  (пріоритет {pri})  |  залишилось: {len(pq)}")

    print("\n>>> Спроба взяти з порожньої черги:\n")
    try:
        pq.pop()
    except IndexError as e:
        print(f"    Помилка: {e}")

    try:
        pq.peek()
    except IndexError as e:
        print(f"    Помилка: {e}")

    print("\n    Все працює як треба!")