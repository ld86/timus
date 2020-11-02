import sys
import math

n = int(sys.stdin.read())

def foo(n):
    a = []

    if n == 0:
        return '10'

    if n == 1:
        return '1'

    for i in range(9, 1, -1):
        while n % i == 0:
            a.append(i)
            n = n // i

    if n != 1:
        return '-1'
    else:
        return ''.join(map(str, sorted(a)))

print(foo(n))