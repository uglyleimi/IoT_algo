import math


def solve():
    with open("input.txt", "r") as f:
        w = int(f.readline())
        heights = list(map(int, f.readline().split()))

    n = len(heights)

    if n == 1:
        print("0.00")
        return

    INF = float("inf")
    dp = [[-INF] * (heights[i] + 1) for i in range(n)]

    for h in range(1, heights[0] + 1):
        dp[0][h] = 0.0

    for i in range(1, n):
        for h in range(1, heights[i] + 1):
            for ph in range(1, heights[i - 1] + 1):
                if dp[i - 1][ph] == -INF:
                    continue
                seg = math.sqrt((h - ph) ** 2 + w**2)
                val = dp[i - 1][ph] + seg
                if val > dp[i][h]:
                    dp[i][h] = val

    ans = max(dp[n - 1][h] for h in range(1, heights[n - 1] + 1))
    print(f"{ans:.2f}")


solve()
