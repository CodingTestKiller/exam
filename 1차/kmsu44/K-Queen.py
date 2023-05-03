import sys
input = sys.stdin.readline

n, k = map(int, input().split())
R, C = map(int, input().split())


def check(a, b, r, c, d, u):
    if (a-b) < 0:
        tmp = abs(a-b) + n-1
    else:
        tmp = abs(a-b)
    if r == a or c == b or d == tmp or u == a+b:
        return True
    return False


L = {}
x = [-1, -1, -1,  0, 0, 1, 1, 1]
y = [1, 0, -1, 1,  -1, 1, 0, -1]
for i in range(8):
    dx, dy = R + x[i], C + y[i]
    if 1 <= dx <= n and 1 <= dy <= n:
        L[dx, dy] = True

flagA = 0
for _ in range(k):
    r, c = map(int, input().split())
    if (r - c) < 0:
        tmp = abs(r-c) + n-1
    else:
        tmp = abs(r-c)
    d = tmp
    u = r+c
    if check(R, C, r, c, d, u):
        flagA = 1
    for a, b in L:
        if L[a, b]:
            if check(a, b, r, c, d, u):
                L[a, b] = False

flagB = 0
cnt = 0
for i in L:
    if L[i]:
        flagB = 0
        cnt += 1
if cnt == 0:
    flagB = 1


if flagA == 1:
    if flagB == 0:
        print("CHECK")
    else:
        print("CHECKMATE")
else:
    if flagB == 1:
        print("STALEMATE")
    else:
        print("NONE")
