dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
cnt = []
while True:
    w, h = map(int,input().split())
    if w ==0 and h==0:
        break
    s = []
    for _ in range(h):
        s.append(list(map(int,input().split())))
    count = 0
    for j in range(w):
        for i in range(h):
            if s[i][j] ==1:
                count += 1
                s[i][j] =0
                queue =[[i,j]]
                while queue:
                    x,y = queue[0][0], queue[0][1]
                    del queue[0]
                    for k in range(8):
                        x1 = x + dx[k]
                        y1 = y + dy[k]
                        if 0<= x1 < h and 0<= y1 <w and s[x1][y1] ==1:
                            s[x1][y1] =0
                            queue.append([x1,y1])
    print(count)