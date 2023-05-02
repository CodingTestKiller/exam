from sys import stdin

import sys

sys.setrecursionlimit(10000000)

input = stdin.readline

n, m = [int(x) for x in input().split()]
k = int(input())

matrix = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def set_traffic(matrix, x, y, depth, max_depth):
    matrix[x][y] = 1
    if depth > max_depth:
        return
    for dx, dy in moves:
        if x+dx < 0 or x+dx >= n:
            continue
        if y+dy < 0 or y+dy >= m:
            continue
        if matrix[x+dx][y+dy] == 0:
            set_traffic(matrix, x+dx, y+dy, depth+1, max_depth)
    

for _ in range(k):
    _x, _y, d = [int(x)-1 for x in input().split()]
    set_traffic(matrix, _x, _y, 0, d)

answers = []

def dfs(matrix, x, y, depth):
    if len(answers) > 0 and depth > min(answers):
        return
    if x == n-1 and y == m-1:
        answers.append(depth)
    if x+1 < n and matrix[x+1][y] == 0 and visited[x+1][y] == 0:
        visited[x+1][y] = 1
        dfs(matrix, x+1, y, depth+1)
        visited[x+1][y] = 0
    if y+1 < m and matrix[x][y+1] == 0 and visited[x][y+1] == 0:
        visited[x][y+1] = 1
        dfs(matrix, x, y+1, depth+1)
        visited[x][y+1] = 0
    if x-1 > 0 and matrix[x-1][y] == 0 and visited[x-1][y] == 0:
        visited[x-1][y] = 1
        dfs(matrix, x-1, y, depth+1)
        visited[x-1][y] = 0
    if y-1 > 0 and matrix[x][y-1] == 0 and visited[x][y-1] == 0:
        visited[x][y-1] = 1
        dfs(matrix, x, y-1, depth+1)
        visited[x][y-1] = 0

dfs(matrix, 0, 0, 0)
if answers:
    print('YES')
    print(min(answers))
else:
    print('NO')
