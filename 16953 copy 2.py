import sys
from collections import deque
input = sys.stdin.readline
A,B = map(int,input().split())
#BFS사용
#[처음숫자,연산횟수]
queue = deque([[A,0]])
while queue:
    a = queue.popleft()
    number , count = a[0],a[1]
    if number > B:
        continue
        #아래 코드 실행하지 않고 건너뛰기
    if number == B:
        print(count+1)
        break
    queue.append([number*2,count+1])
    queue.append([number*10+1,count+1])
    print(queue)
else:
    print(-1)
