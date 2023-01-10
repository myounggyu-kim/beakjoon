N = int(input())
a = []
collect_Answer = []
for _ in range(N):
    b = list(str(input()))
    a.append(b)
L = len(a[0])
if N ==1:
    for j in range(L):
        collect_word = a[0][j]
        collect_Answer.append(collect_word)
else:
    for j in range(L):
        for i in range(N-1):
            if a[i][j] == a[i+1][j]:
                collect_word = a[i+1][j]
            else:
                collect_word = "?"
                break
        collect_Answer.append(collect_word)
print(''.join(collect_Answer))