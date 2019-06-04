#r
n,k=map(int,input().split())
l=[str(x) for x in input().split()]
b=l[k:]+l[:k]
print(' '.join(b))
