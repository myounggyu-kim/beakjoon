T = int(input())
for _ in range(T):
    n = int(input())
    dp = [1,2,4]
    if n == 1:
        print(dp[0])
    elif n ==2:
        print(dp[1])
    elif n ==3:
        print(dp[2])
    else:
        for _ in range(n-3):
            dp[0],dp[1],dp[2] = dp[1],dp[2],dp[0]+dp[1]+dp[2]
        print(dp[-1])
    #정수 4는
    '''
    1에서 3이 가능한 방법 [1,1,1],[2,1],[1,2],[3] - 4
    2에서 2이 가능한 방법 [1,1][2] - 2
    3에서 1이 가능한 방법 [1] - 1
    '''
