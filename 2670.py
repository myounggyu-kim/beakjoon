n = int(input())
dp = [1] * n
if n == 1:
    x = float(input())
    dp[0] = x
else:
    x = float(input())
    dp[0] = x
    for i in range(1,n):
        x = float(input())
        dp[i] = max(x*dp[i-1],x)
print(dp)
print("{:.3f}".format(max(dp)))