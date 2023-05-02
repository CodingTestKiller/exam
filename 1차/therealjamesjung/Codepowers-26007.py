from sys import stdin

input = stdin.readline

n, m, x, k = [int(x) for x in input().split()]

scores = [int(x) for x in input().split()]
scores = [k] + scores

for i in range(1, len(scores)):
    scores[i] += scores[i-1]

cnt = [0] * (n+1)

for i in range(1, len(scores)):
    tmp = 0
    if scores[i] < x:
        tmp = 1
    cnt[i] = cnt[i-1] + tmp

res = []

for _ in range(m):
    s, e = [int(x)-1 for x in input().split()]
    res.append(cnt[e] - cnt[s])

[print(r) for r in res]