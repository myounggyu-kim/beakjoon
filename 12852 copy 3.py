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
        queue.append(a+[num//2])
    if num%3 == 0:
        queue.append(a+[num//3])
    queue.append(a+[num-1])