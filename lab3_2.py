import sys


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    @classmethod
    def load_from_file(cls, path):
        f = open(path, "r")
        items = []
        for line in f:
            for item in line.split():
                items.append(item)
        f.close()

        if len(items) == 0 or items[0] == "n":
            return None

        root = cls(int(items[0]))
        queue = [root]
        idx = 1

        while len(queue) > 0 and idx < len(items):
            node = queue.pop(0)
            if idx < len(items):
                if items[idx] != "n":
                    node.left = cls(int(items[idx]))
                    queue.append(node.left)
                idx += 1
            if idx < len(items):
                if items[idx] != "n":
                    node.right = cls(int(items[idx]))
                    queue.append(node.right)
                idx += 1

        return root

    def invert_tree(self):
        temp = self.left
        self.left = self.right
        self.right = temp
        if self.left is not None:
            self.left.invert_tree()
        if self.right is not None:
            self.right.invert_tree()

    def show(self):
        rows = []
        cur = [self]
        while any(n is not None for n in cur):
            rows.append(cur)
            next_row = []
            for n in cur:
                if n is not None:
                    next_row.append(n.left)
                    next_row.append(n.right)
                else:
                    next_row.extend([None, None])
            cur = next_row

        depth = len(rows)
        for i in range(depth):
            sp = 4 * 2 ** (depth - 1 - i)
            child_sp = sp // 2

            line = ""
            for node in rows[i]:
                if node is not None:
                    line += ("(" + str(node.val) + ")").center(sp)
                else:
                    line += " " * sp
            print(line)

            if i < depth - 1:
                next_sp = child_sp
                sline = ""
                for node in rows[i]:
                    left_chunk  = [" "] * child_sp
                    right_chunk = [" "] * child_sp
                    if node is not None:
                        if node.left is not None:
                            label = "(" + str(node.left.val) + ")"
                            center = (next_sp - len(label)) // 2 + len(label) // 2
                            if 0 <= center < child_sp:
                                left_chunk[center] = "/"
                        if node.right is not None:
                            label = "(" + str(node.right.val) + ")"
                            center = (next_sp - len(label)) // 2 + len(label) // 2
                            if 0 <= center < child_sp:
                                right_chunk[center] = "\\"
                    sline += "".join(left_chunk) + "".join(right_chunk)
                print(sline)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "tree.txt"

    root = BinaryTree.load_from_file(path)

    print("До інвертування:")
    root.show()

    root.invert_tree()

    print("\nПісля інвертування:")
    root.show()