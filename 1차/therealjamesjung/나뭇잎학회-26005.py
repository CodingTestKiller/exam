from sys import stdin

input = stdin.readline

n = int(input())

if n == 1:
    print(0)
elif n % 2 ==0:
    print(int(n*n/2))
else:
    print(n * (n // 2) + ((n // 2) + 1))