from sys import stdin
input = stdin.readline
n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split(' '))))
b = a.copy()
for i in range(n):
    for j in range(n):
        if i==0 and j==0:
            b[i][j] = a[i][j]
        elif i==0 and j!=0:
            b[i][j] = b[i][j-1] + a[i][j]
        elif j==0 and i!=0:
            b[i][j] = b[i-1][j] + a[i][j]
        else:
            b[i][j] = b[i-1][j] + b[i][j-1] - b[i-1][j-1] + a[i][j]

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    if x1 == 1 and y1 ==1:
        ans = b[x2-1][y2-1]
    elif x1 ==1 and y1 != 1:
        ans = b[x2-1][y2-1] - b[x2-1][y1-2]#y1-1
    elif x1 != 1 and y1==1:
        ans = b[x2-1][y2-1] - b[x1-2][y2-1] #x1-1
    else:
        ans = b[x2-1][y2-1] - b[x2-1][y1-2] - b[x1-2][y2-1] + b[x1-2][y1-2]
    print(ans)