import sys
input = sys.stdin.readline

n,m = map(int,input().split())
snack = list(map(int,input().split()))

start = 1
end = sum(snack)//n

ans = 0
while start <= end:
    mid = (start+end) // 2
    total = 0 # 나눠줄수 있는양
    for i in snack:
        if i >= mid: 
            total += i//mid
        else:
            pass
    #print(mid,total)
    if total < n:
        end = mid - 1
    else: 
        start = mid + 1
        ans = max(ans,mid)
print(ans)
