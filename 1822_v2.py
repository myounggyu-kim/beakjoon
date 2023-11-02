A_Num,B_Num = map(int,input().split())
# list보다 set이 시간이 더 짧다
A = list(map(int,input().split()))
B = list(map(int,input().split()))
for i in B:
    if i in A:
        A.remove(i)

print(len(A))
if A:
    print(*A)