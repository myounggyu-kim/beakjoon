n,k = map(int,input().split())
tri = []
tri.append([1])
tri.append([1,1])
for i in range(2,n):
    tri.append([1]*(i+1))
    for j in range(1,i):
        tri[i][j] = tri[i-1][j-1] + tri[i-1][j]
print(tri[n-1][k-1])

