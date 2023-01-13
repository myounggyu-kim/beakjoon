S = list(str(input()))
l = len(S)
a = []
for i in range(l):
    for j in range(l-1,i-1,-1):
        print(j)
        a.append(''.join(S[i:j+1]))
print(a)
print(len(set(a)))