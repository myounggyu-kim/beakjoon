import sys
input = sys.stdin.readline
n = int(input())
dp_max = [0]*3
dp_min = [0]*3
dp_max_temp = [0]*3
dp_min_temp = [0]*3
for i in range(n):
    a,b,c = map(int,input().split())
    #가장 왼쪽
    dp_max_temp[0] =  a + max(dp_max[0],dp_max[1])
    dp_min_temp[0] =  a + min(dp_min[0],dp_min[1])
    #중앙
    dp_max_temp[1] =  b + max(dp_max[0],dp_max[1],dp_max[2])
    dp_min_temp[1] =  b + min(dp_min[0],dp_min[1],dp_max[2])
    #가장 오른쪽
    dp_max_temp[2] =  c + max(dp_max[1],dp_max[2])
    dp_min_temp[2] =  c + min(dp_min[1],dp_min[2])
    for j in range(3):
        dp_max[j] = dp_max_temp[j]
        dp_min[j] = dp_min_temp[j]
print(max(dp_max),min(dp_min))