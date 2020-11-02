import sys

n, k = sys.stdin.read().split()
n = int(n)
answer = 1
while n > 0:
    answer *= n
    n -= len(k)
print(answer)