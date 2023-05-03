from sys import stdin
input = stdin.readline

n, m, k, x = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
index = [[int(x) for x in input().split()] for _ in range(m)]

dp = [x for _ in range(n+1)]
dp2 = [0 for _ in range(n+1)]

for i, data in enumerate(arr):
    dp[i+1] = dp[i] + data
    if dp[i+1] < k:
        dp2[i+1] = dp2[i] + 1
    else:
        dp2[i+1] = dp2[i]


for data in index:
    print(dp2[data[1]-1] - dp2[data[0]-1])
