n = int(input())
cost = [0, 0, 0]
r,g,b = map(int,input().split())
cost[0], cost[1], cost[2] = r,g,b
for _ in range(n-1):
    r,g,b = map(int,input().split())
    r += min(cost[1],cost[2])
    g += min(cost[0],cost[2])
    b += min(cost[0],cost[1])
    cost[0], cost[1], cost[2] = r,g,b
print(min(cost))
