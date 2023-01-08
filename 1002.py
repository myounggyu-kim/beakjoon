T = int(input())
while T>0:
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if (x1 == x2) & (y1 == y2) & (r1 == r2):
        print(-1)
    else:
        if r1 >= r2:
            R = r1
            r = r2
        else:
            R = r2
            r = r1
        D = (x1-x2)**2 + (y1-y2)**2
        d = D**(1/2)
        if d > R + r:
            print(0)
        elif d == R + r:
            print(1)
        elif R - r < d < R + r:
            print(2)
        elif d == R - r:
            print(1)
        else:
            print(0)
    T = T-1