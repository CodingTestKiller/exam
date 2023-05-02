from sys import stdin
from collections import Counter

input = stdin.readline

_ = input()
s = input()

res = Counter(s.strip())
print(min([res['H'], res['I'], res['A'], res['R'], res['C']]))
