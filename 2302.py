import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
pick = []
dp = [0]*(41)
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2]

for i in range(m):
    pick.append(int(input()))
seat = 0
ans = 1
for i in range(1,n+1):
    if i in pick:
        ans *= dp[seat] 
        seat = 0
    elif i == n:
        seat += 1
        ans *= dp[seat]
    else:
        seat += 1
print(ans)
