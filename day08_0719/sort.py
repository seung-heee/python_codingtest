import sys
import bisect

si = sys.stdin.readline
n = int(si())
store = sorted(map(int, si().split()))
m = int(si())
wish = list(map(int, si().split()))

for x in wish:
    idx = bisect.bisect_left(store, x)

    if store[idx] == x:
        print("yes", end=" ")
    else:
        print("no", end=" ")
