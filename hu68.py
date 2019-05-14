#rubi
r=int(input())
s=list(map(int,input().split()))
print((s.index(min(s)))+1,end=" ")
print((s.index(max(s))+1))

