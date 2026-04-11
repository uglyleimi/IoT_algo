# 1. Зчитати N — кількість пар

# 2. Створити Union-Find (DSU)
#    - parent[x] = x  (кожен сам собі предок на старті)
#    - find(x) — повертає корінь племені x (з path compression)
#    - union(a, b) — об'єднує два племені в одне

# 3. Зчитати N пар і для кожної пари викликати union(a, b)
#    - після цього всі люди одного племені мають однаковий find()

# 4. Зібрати всіх унікальних людей
#    - пройтись по всіх числах що зустрічались
#    - непарне → хлопець, парне → дівчина

# 5. Для кожного племені порахувати кількість хлопців і дівчат

# 6. Порахувати відповідь за формулою:

# 7. Вивести answer




class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA != rootB:
            # Union by rank
            if self.rank[rootA] > self.rank[rootB]:
                self.parent[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.parent[rootA] = rootB
            else:
                self.parent[rootB] = rootA
                self.rank[rootA] += 1
                
             
def main():
    print("Enter the number of pairs:")
    N = int(input())
    uf = UnionFind(1000001)  
    people = set()
    for _ in range(N):
        a, b = map(int, input().split())
        uf.union(a, b)
        people.add(a)
        people.add(b)
        
        
    tribe_boys = {}
    tribe_girls = {}
    for person in people:
        root = uf.find(person)
        if person % 2 == 0: 
            tribe_girls[root] = tribe_girls.get(root, 0) + 1
        else:  
            tribe_boys[root] = tribe_boys.get(root, 0) + 1

    total_boys = sum(tribe_boys.values())
    total_girls = sum(tribe_girls.values())

    answer = total_boys * total_girls - sum(
    tribe_boys.get(t, 0) * tribe_girls.get(t, 0) for t in set(tribe_boys) | set(tribe_girls)
)
    print(answer)

if __name__ == "__main__":    main()
