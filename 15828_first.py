from collections import deque
N = int(input())
d = deque()
while True:
    a = int(input())
    if a>0:
        if len(d)+1<= N: #(+1)의 의미 들어오는 a데이터 
            print(len(d),N)
            d.append(a)
        else:
            pass
    elif a ==0:
        d.popleft()
    elif a==-1:
        break
    else: #음수
        print('error')

if len(d) !=0:
    while d:
        print(d.popleft(),end=' ')
else:
    print('empty')

