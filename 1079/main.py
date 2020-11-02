import sys

a = [0 for i in range(100000)]
m = [0 for i in range(100000)]

m[1] = a[1] = 1

for i in range(2, 100000):
    if i % 2 == 0:
        a[i] = a[i // 2]
    else:
        a[i] = a[i // 2] + a[(i // 2) + 1]
    m[i] = max(m[i - 1], a[i])    
    
for i in map(int, sys.stdin.read().split()):
    if i == 0:
        break
    print(m[i])