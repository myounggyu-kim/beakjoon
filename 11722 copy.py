n = int(input())
a = list(map(int,input().split()))
dp = [1]*n
min = a[-1]
for i in range(n-1,0,-1):
    print(i-1)
    if a[i-1] > min:
        min =  a[i-1]
        dp[i-1] = dp[i] +1
    else:
        dp[i-1] =dp[i]
print(dp)