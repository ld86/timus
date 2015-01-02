import sys
import math

a = reversed(map(int, sys.stdin.read().split()))
print("\n".join(map(lambda x: "{:.4f}".format(math.sqrt(x)), a)))
