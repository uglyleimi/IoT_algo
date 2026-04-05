import os

def parse_input():
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    root_val = int(lines[0])
    children = {}
    for line in lines[1:]:
        parts = line.split(",")
        parent = int(parts[0])
        child = int(parts[1])
        if parent not in children:
            children[parent] = []
        children[parent].append(child)
    return root_val, children

def min_depth_bfs(root_val, children):
    queue = [(root_val, 0)]
    min_depth = float('inf')
    while queue:
        node, depth = queue.pop(0)
        if node not in children:
            min_depth = min(min_depth, depth)
        else:
            for child in children[node]:
                queue.append((child, depth + 1))
    return min_depth

# міняємо директорію ПЕРШИМ ділом
os.chdir(os.path.dirname(os.path.abspath(__file__)))

root_val, children = parse_input()
result = min_depth_bfs(root_val, children)

with open('output.txt', 'w') as f:
    f.write(str(result) + '\n')

print(f"minimum depth: {result}")

