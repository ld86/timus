import sys

n = int(sys.stdin.read())
if n == 0:
    print(1)
elif n > 0:
    print((n * (n + 1))//2)
else:
    n = -n
    print(1 - (n * (n + 1))//2)