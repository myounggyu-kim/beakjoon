M, N, K = map(int,input().split())
S = [[0] * N for i in range(M)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cnt =[] #카운트
for _ in range(K):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            S[i][j] = 1 
#사각형의 안에 부분을 1로 채운다.
for i in range(M):
    for j in range(N):
        if S[i][j] == 0:
            count = 1
            S[i][j] = 1
            queue = [[i, j]]
            while queue:
                x,y = queue[0][0], queue[0][1]
                del queue[0]
                for k in range(4):
                    x1 = x + dx[k]
                    y1 = y + dy[k]
                    if 0<= x1 < M and 0<= y1 < N and S[x1][y1] == 0:
                        S[x1][y1] = 1
                        count += 1
                        queue.append([x1, y1])
            cnt.append(count)
print(len(cnt))
cnt.sort()
for i in cnt:
    print(i, end=' ')