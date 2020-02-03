from collections import Counter

inp = input()
n = input().split()
g = Counter(n)
j = dict(g)

print(min(j, key=lambda g: d[g]))
