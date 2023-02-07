import sys
from collections import deque
input = sys.stdin.readline
# BFS
X = int(input())
queue = deque([[X]])
while queue:
    a = queue.popleft()
    num = a[-1]
    if num < 1:
        continue
    if num == 1:
        print(len(a)-1)
        print(*a)
        break
    if num%2 == 0:
        b =a.copy()
        b.append(num//2)
        queue.append(b)
    if num%3 == 0:
        c = a.copy()
        c.append(num//3)
        queue.append(c)
    a.append(num-1)
    queue.append(a)