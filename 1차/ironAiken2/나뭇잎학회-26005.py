from sys import stdin
input = stdin.readline

n = int(input())
n *= n

if n == 1:
    print(0)
    exit()
if n % 2 == 0:
    print(n//2)
else:
    print(n//2 + 1)
