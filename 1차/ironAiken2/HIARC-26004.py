from sys import stdin
input = stdin.readline

n = int(input())
arr = [str(x) for x in input().rstrip()]
dic = {'H': 0, 'I': 0, 'A': 0, 'R': 0, 'C': 0}

if len(arr) < 5:
    print(0)
    exit()

for data in arr:
    try:
        dic[data] += 1
    except:
        continue

ans = 100000

for data in dic:
    if dic[data] < ans:
        ans = dic[data]

print(ans)
