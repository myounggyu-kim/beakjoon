import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
op = list(map(int,input().split()))
Max = -int(1e9)
Min = int(1e9)

answer = A[0]

def dfs(depth):
    global answer
    global Min,Max

    if depth == N:
        if answer > Max:
            print(answer,Max)
            Max = answer
        if answer < Min:
            print(answer,Min)
            Min = answer
        return
    
    for i in range(4):
        tmp = answer
        if op[i] > 0:
            if i == 0:
                answer += A[depth]
            elif i == 1:
                answer -= A[depth]
            elif i == 2:
                answer *= A[depth]
            elif i == 3:
                if answer >= 0:
                    answer //= A[depth]
                else:
                    answer = (-answer // A[depth]) * -1
        
        op[i] -= 1
        dfs(depth+1)
        answer = tmp
        op[i] +=1


dfs(1)
print(Max)
print(Min)