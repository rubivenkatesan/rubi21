#rubi
n=int(input())
l=list(map(int,input().split()))
t=[]
if n%2==0:
    for i in range(n//2):
        m1=max(l)
        t.append(m1)
        l.remove(m1)
        m2=min(l)
        t.append(m2)
        l.remove(m2)
    print(*t)
else:
    for i in range(n//2):
        m1=max(l)
        t.append(m1)
        l.remove(m1)
        m2=min(l)
        t.append(m2)
        l.remove(m2)
    t.append(l[0])
    print(*t)
