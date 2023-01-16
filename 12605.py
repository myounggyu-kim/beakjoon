import sys
input = sys.stdin.readline
for i in range(1,int(input())+1):
    a = list(input().split())
    print('Case #%d: %s' %(i,' '.join(a[::-1])))
