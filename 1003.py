T = int(input())
def f(n):
    cnt_0 = [1, 0, 1]
    cnt_1 = [0, 1, 1]
    l = len(cnt_0)
    if l <= n:
        for i in range(l,n+1):
            cnt_0.append(cnt_0[i-1]+cnt_0[i-2])
            cnt_1.append(cnt_1[i-1]+cnt_1[i-2])
    print(cnt_0[n],cnt_1[n])

for i in range(T):
    f(int(input()))