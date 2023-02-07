T = int(input())
for _ in range(T):
    n = int(input())
    dp = [[1,0,0],[0,1,0],[1,1,1]]
    if n == 1:
        print(1)
    elif n == 2:
        print(1)
    elif n== 3:
        print(3)
    else:
        for _ in range(n-3):
            a = dp[2][1]+dp[2][2]
            b = dp[1][0]+dp[1][2]
            c = dp[0][0]+dp[0][1]
            dp[0],dp[1],dp[2] = dp[1],dp[2],[a,b,c]
        print(dp[2][0]+dp[2][1]+dp[2][2])