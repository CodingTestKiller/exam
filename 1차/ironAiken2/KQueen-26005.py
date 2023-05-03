from sys import stdin
input = stdin.readline

n, k = [int(x) for x in input().split()]
white = [int(x) for x in input().split()]
black = [[int(x) for x in input().split()] for _ in range(k)]
move = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

now = False
future = False

for data in black:
    if data[0] == white[0] or data[1] == white[1] or abs(data[0] - white[0]) == abs(data[1] - white[1]):
        now = True
        break

flag = 0

for step in move:
    flag2 = False

    nx = white[0] + step[0]
    ny = white[1] + step[1]
    if nx > n or ny > n or nx < 1 or ny < 1:
        continue

    for data in black:
        if data[0] == nx or data[1] == ny or abs(data[0] - nx) == abs(data[1] - ny):
            flag2 = True
            break

    if flag2 == False:
        flag += 1

if flag == 0:
    future = True

if now == True:
    if future == True:
        print("CHECKMATE")
    else:
        print("CHECK")
else:
    if future == True:
        print("STALEMATE")
    else:
        print("NONE")
