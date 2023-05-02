from sys import stdin

n, k = [int(x) for x in input().split()]
board = [[False]*n for _ in range(n)]

r, c = [int(x)-1 for x in input().split()]

for _ in range(k):
    _x, _y = [int(x)-1 for x in input().split()]
    board[_x][_y] = True

    for i in range(n):
        board[_x][i] = True
        board[i][_y] = True
    
    diag1 = _x+_y
    diag2 = _x-_y
    diag3 = _y-_x

    for i in range(n):
        for j in range(n):
            if i+j == diag1:
                board[i][j] = True
            if i-j == diag2:
                board[i][j] = True
            if j-i == diag3:
                board[i][j] = True

moves = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

cnt = 0
for dx, dy in moves:
    if board[r+dx][c+dy] == 1:
        cnt += 1

if cnt == 8:
    if board[r][c]:
        print('CHECKMATE')
    else:
        print('STALEMATE')
else:
    if board[r][c]:
        print('CHECK')
    else:
        print('NONE')