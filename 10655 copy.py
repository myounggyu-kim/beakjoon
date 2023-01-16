#택시 기하학
def dis(x1,y1,x2,y2):
    distance = abs(x1-x2) + abs(y1-y2)
    return distance


N = int(input())
x=[]
y=[]
for _ in range(N):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
#최고 높은수...
total_dis = 0
for i in range(N-1):
    total_dis += dis(x[i],y[i],x[i+1],y[i+1])
min_num = total_dis

for j in range(1,N-1):
    road = total_dis - dis(x[j-1],y[j-1],x[j],y[j]) -dis(x[j],y[j],x[j+1],y[j+1]) + dis(x[j-1],y[j-1],x[j+1],y[j+1])
    print(road)
    if road < min_num:
        min_num = road
    

    
print(min_num)