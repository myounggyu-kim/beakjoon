n = int(input())
dp = [0]*(n+1)
if n ==1 :
    dp[1] = 1
else:
    dp[1] = 1
    dp[2] = 2
for i in range(3,n+1):
    if i%2 ==1:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1]+dp[i//2]
print(dp[n]%1000000000)